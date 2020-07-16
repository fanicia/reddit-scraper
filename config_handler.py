import yaml
import os.path
from dataclasses import dataclass


class ScrapingConfig:
    def __init__(self):
        with open('secrets.yml', encoding='utf-8') as file:
            documents = yaml.full_load(file)
            
            self.client_id = documents['client_id']
            self.client_secret = documents['client_secret']
            self.user_agent = documents['user_agent']

        