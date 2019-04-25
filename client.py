import requests

auth_url = 'http://localhost:5000/api/login'
get_requests = ['http://localhost:5000/api/secret1', 'http://localhost:5000/api/secret2',
                'http://localhost:5000/api/secret3']


def auth(url):
    body = {
        "username": "guest",
        "password": "guest"
    }
    response = requests.post(url, json=body)
    return response.json()


def request(url, token):
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    if response.status_code == 401:
        return 'unauthorized'
    if response.status_code == 200:
        return response.text


if __name__ == '__main__':
    token = auth(auth_url)['access_token']
    for url in get_requests:
        while True:
            response = request(url, token)
            print(response)
            if response == 'unauthorized':
                token = auth(auth_url)['access_token']
            else:
                break
