import random
import time
from Endpoints.create_endpoint import CreateObject
from Endpoints.delete_endpoint import DeleteObject
from Endpoints.get_endpoint import GetObject
import os
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv('USER_NAME')
name_repository = f"{os.getenv('REPO_NAME')}{random.randint(0, 20)}"
token = os.getenv('TOKEN')


def test_create_repository():
    create_object = CreateObject()
    get_object = GetObject()

    payload = {"name": f"{name_repository}",
               "description": "This is Test repository",
               "homepage": "https://github.com",
               "private": False,
               "has_issues": True,
               "has_projects": True,
               "has_wiki": True
               }

    create_object.create_repository(payload=payload)
    assert get_object.check_response_name_repository(user_name, name_repository)


def test_delete_repository():
    create_object = CreateObject()
    get_object = GetObject()
    delete_object = DeleteObject()

    payload = {"name": f"{name_repository}",
               "description": "This is Test repository",
               "homepage": "https://github.com",
               "private": False,
               "has_issues": True,
               "has_projects": True,
               "has_wiki": True
               }
    create_object.create_repository(payload=payload)
    get_object.check_response_name_repository(user_name, name_repository)
    assert get_object.check_response_name_repository(user_name, name_repository)
    time.sleep(20)
    delete_object.delete_repository(user_name, name_repository)
    assert get_object.check_response_deleted_name_repository(user_name, name_repository)
