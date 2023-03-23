import datetime

from requests import get, post

print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1000,
                 'id': 1000,
                 'job': 'AHBV',
                 'work_size': 6,
                 'collaborators': '',
                 'is_finished': False}).json())  # просто добавление
print('\n')
print(get('http://localhost:8080/api/jobs/1000').json())  # проверка что добавился
print('\n')
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1000,
                 'id': 1000,
                 'job': 'AHBV',
                 'work_size': 6,
                 'collaborators': '',
                 'is_finished': False}).json())  # ошибка на добавление существующего
print('\n')
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1000}).json())  # ошибка не все аргументы
print('\n')
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 'as',
                 'id': 'asd',
                 'job': 'AHBV',
                 'work_size': 6,
                 'collaborators': '',
                 'is_finished': False}).json())  # ошибка id - строка