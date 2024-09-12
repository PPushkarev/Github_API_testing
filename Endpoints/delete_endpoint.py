import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')


class DeleteObject():
    def delete_repository(self, user_name, name_repository):
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'{token}'
        }
        self.response = requests.delete(f"https://api.github.com/repos/{user_name}/{name_repository}", headers=headers)
