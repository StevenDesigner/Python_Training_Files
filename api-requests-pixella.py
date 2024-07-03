import datetime
import requests


USERNAME="stevenprime"
TOKEN="123456789"
GRAPH_ID="graph1"

pixe_la_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixe_la_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixe_la_endpoint}/{USERNAME}/graphs"

graph_params={
    "id":"graph1",
    "name":"cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
today=datetime.datetime(year=2024,month=7,day=1)
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)
pixe_creation_endpoint =f"{pixe_la_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"9.74"
}

# response=requests.post(url=pixe_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

pixe_updation_endpoint =f"{pixe_la_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_dat={
    "quantity":"4.7"
}
# response=requests.put(url=pixe_updation_endpoint,json=update_dat,headers=headers)
# print(response.text)
delete_endpoint =f"{pixe_la_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)