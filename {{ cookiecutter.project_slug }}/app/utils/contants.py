from dotenv import load_dotenv
import structlog
import logging
import os

class Config():
    @staticmethod
    def load_environment():
        load_dotenv()
        required_vars = ['your', 'api', 'keys', 'here']
        
        for var in required_vars:
            if not os.getenv(var):
                raise ValueError(f"{var} não está definida no ambiente.")
        structlog.get_logger().info("Environment variables loaded successfully.")

    '''
    Vou criar mais constants depois, tais como logs e etc...
    '''
