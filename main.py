import requests
from datetime import datetime
USERNAME = "amandeoli"
TOKEN = "zs11edc1vgy2jnmki437891"
GRAPH_ID="graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_para = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
# response=requests.post(url=pixela_endpoint, json=user_para)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers={
    "X-USER-TOKEN":TOKEN

}
# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

##requests.post()

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime(year=2022, month=7,day=27)

print(today)
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"10.22",
}

response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)


