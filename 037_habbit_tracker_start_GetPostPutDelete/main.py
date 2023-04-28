import requests
import datetime

date_now = datetime.datetime.now().strftime("%Y%m%d")
pixela_base_url = 'https://pixe.la/'
pixela_register_url = 'v1/users'

pixela_register_payload = {
    'token': 'qwerasdfasdfqweff34f34f',
    'username': 'testuserqwe123',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
pixela_headers = {
    'X-USER-TOKEN': f"{pixela_register_payload['token']}",
}
register_response = requests.post(url=pixela_base_url + pixela_register_url, json=pixela_register_payload)
print(register_response.json())

'https://pixe.la/@testuserqwe123'

pixela_add_graph_url = f"/v1/users/{pixela_register_payload['username']}/graphs"

pixela_add_graph_payload = {
    'id': 'graph01',
    'name': 'meters_tracker',
    'unit': 'meters',
    'type': 'float',
    'color': 'momiji',
}


add_graph_response = requests.post(url=pixela_base_url + pixela_add_graph_url, json=pixela_add_graph_payload,
                                   headers=pixela_headers)
print(add_graph_response.json())

pixela_add_pixel_url = f"/v1/users/{pixela_register_payload['username']}/graphs/{pixela_add_graph_payload['id']}"

pixela_add_pixel_payload = {
    'date': f'{date_now}',
    'quantity': '54',
}

add_pixel_response = requests.post(url=pixela_base_url + pixela_add_pixel_url, json=pixela_add_pixel_payload,
                                   headers=pixela_headers)

print(add_pixel_response.json())


