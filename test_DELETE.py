import datetime

from requests import get, post, delete

print(delete('http://localhost:8080/api/jobs/999999').json())
# новости с id = 999999 нет в базе

print(delete('http://localhost:8080/api/jobs/1').json())
print('\n')
print(get('http://localhost:8080/api/jobs/1').json())  # проверка что удалился
print('\n')
print(get('http://localhost:8080/api/jobs').json())
