import requests

properties = {'amount': 2,
              'type': 'boolean'}

response = requests.get(url='https://opentdb.com/api.php', params=properties)

question_data = response.json()['results']
