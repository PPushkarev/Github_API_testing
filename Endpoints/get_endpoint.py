import requests


class GetObject():

    def check_response_name_repository(self, user_name, name_repository):
        self.response = requests.get(f'https://api.github.com/users/{user_name}/repos')
        self.response_json = self.response.json()
        if isinstance(self.response_json, list):
            for response_name in self.response_json:
                if response_name['name'] == name_repository:
                    return True
        return False

    def check_response_deleted_name_repository(self, user_name, name_repository):
        self.response = requests.get(f'https://api.github.com/users/{user_name}/repos')
        self.response_json = self.response.json()
        if isinstance(self.response_json, list):
            for response_name in self.response_json:
                if response_name['name'] == name_repository:
                    return False
        return True
