import requests,getpass

BASE_URL = "http://localhost:8000/api/v1/"

AUTH_TOKEN_URL = f'{BASE_URL}token/'
username = input("Enter UserName ")
password = getpass.getpass("Enter Password ")
user = {
    'username':username,
    'password':password
}

auth_res = requests.post(AUTH_TOKEN_URL,json=user)
print(auth_res.json())
# GET all employees
token = auth_res.json()['access']

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get(f"{BASE_URL}employees/",headers=headers)

print(response.text)
# print(response.json())
