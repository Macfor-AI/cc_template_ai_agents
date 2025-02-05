import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from crewai import Crew, Process
from app.ai_agents.crew import MainCrew

def main(name, company, summary, job_desc, industry, degree, field_of_study, headline, job_title, skills, research):
    
    
    input_data = "Crie uma variável com seus inputs"
    
    MainCrew().crew().kickoff(inputs=input_data)

if __name__ == '__main__':
    results = main()
    print(results)