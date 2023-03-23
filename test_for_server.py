from requests import get

print(get('http://localhost:8080/api/jobs').json())
print('\n')
print(get('http://localhost:8080/api/jobs/1').json())
print('\n')
print(get('http://localhost:8080/api/jobs/1111').json())
print('\n')
print(get('http://localhost:8080/api/jobs/abs').json())
