import requests
from urllib.parse import quote


url = "https://dev212688.service-now.com/oauth_token.do"
username = 'admin'
password = 'hg+WnvVN1O9+'
client_id = 'be587054626d4e85acbd29bb9c3b180e'
client_secret = '3Ay&^O:[3p'

encoded_password = quote(password)


body = {
    'grant_type': 'password',
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': encoded_password
}

response = requests.post(url=url, data=body)

print(response.text)
# url = f"https://dev212688.service-now.com/login.do?user_name={username}&sys_action=sysverb_login&user_password={encoded_password}"
#
#
# response = requests.post(url)
#

#
# if response.status_code == 200:
#     response_url = response.url
#     if 'redirect' not in response_url:
#         print("Грешка при аутентикация: Invalid credentials.")
#     else:
#         print("Успешна аутентикация!")
#
# else:
#     print("Грешка при аутентикация:", response.status_code)
#
#
#
#
# url_table = "https://dev212688.service-now.com/api/now/table/cmdb_ci"
#
#
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }
#
# response = requests.get(url_table, auth=(username, password), headers=headers)
#
# if response.status_code == 200:
#     assets = response.json().get('result', [])
#     for asset in assets:
#         print(asset)
# else:
#     print("Failed:", response.status_code, response.text)
