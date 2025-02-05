'''
Este script é apenas um exemplo de como deve ser usado. Substitua, crie e desenvolva
conforme sua customização e uso
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from dotenv import load_dotenv
import warnings
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from langchain_openai import ChatOpenAI

warnings.filterwarnings('ignore')

load_dotenv()

@CrewBase
class MainCrew:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def create_llm(self):
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.1,
            frequency_penalty=0.9,
            api_key=self.api_key
        )
    
    @agent
    def general_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['general_analyst'],
            allow_delegation=False,
            llm=self.create_llm()
            )
    
    @task
    def general_report(self) -> Task:
        return Task(
            config=self.tasks_config['general_report'],
            agent=self.general_analyst(),
            output_file='data/agent_output/profile.txt'
            )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            name="Análise Profunda de Leads",
            process=Process.sequential, 
            language='português brasileiro'
            )
