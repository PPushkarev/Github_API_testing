import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')


class CreateObject():
    def create_repository(self, payload):
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'{token}'
        }
        self.response = requests.post('https://api.github.com/user/repos', json=payload, headers=headers)
