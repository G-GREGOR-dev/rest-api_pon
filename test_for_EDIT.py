import datetime

from requests import get, post, put

print(put('http://localhost:8080/api/jobs',
           json={'team_leader': 1000,
                 'id': 1,
                 'job': 'sybbotnik',
                 'work_size': 6,
                 'collaborators': '',
                 'is_finished': False}).json())  # корректное редактирование
print(put('http://localhost:8080/api/jobs',
           json={'team_leader': 1000,
                 'id': 10,
                 'job': 'sybbotnik',
                 'work_size': 6,
                 'collaborators': '',
                 'is_finished': False}).json())  # не существует элемента
print(put('http://localhost:8080/api/jobs',
           json={'team_leader': 1000,
                 'id': 'as',
                 'job': 'sybbotnik',
                 'work_size': 6,
                 'collaborators': '',
                 'is_finished': False}).json())  # id - string
print('\n')
