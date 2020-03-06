import requests
from requests.exceptions import HTTPError


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print('{http_err}')
    except Exception as err:
        print('{err}')
    else:
        print('xD')


# nauka API, pobieranie danych z serwisu


response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'test+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')