# introduction to API calls 
# real request from pypi.prg
import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r)
print(r.status_code)
print(r.json())

# fake or dummy request from JSON placeholder
r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(r)
print(r.json())