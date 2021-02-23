import requests
import time
from datetime import datetime

GRAPHID = "graph1"
USERNAME = "neha"
TOKEN = "htgniuih3mkhu67gatnyu1"
pixela_endpoint = "https://pixe.la/v1/users"
#Create new pixela account
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Create a new graph definition
#POST - /v1/users/<username>/graphs
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": GRAPHID,
#     "name": "Cycling Graph",
#     "unit": "Miles",
#     "type": "float",
#     "color": "ajisai"
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
#https://pixe.la/v1/users/neha/graphs/graph1.html


#post to pixela data
today = time.strftime('%Y%m%d')   #str(date.today())
#today = datetime(year=2020, month=12, day=28)    #use to back update

# print(today)
#/v1/users/<username>/graphs/<graphID>
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
headers = {
     "X-USER-TOKEN": TOKEN
 }
update_graph_params = {
     "date": today,   #.strftime('%Y%m%d'),
#     "date": today.strftime('%Y%m%d'),
     "quantity": input("How many miles did you cycle today?")
 }

response = requests.post(url=update_graph_endpoint, json=update_graph_params, headers=headers)
print(response.text)

# #put = /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# today = datetime(year=2020, month=12, day=28)    #use to back update
# put_date = today.strftime('%Y%m%d')
# put_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{put_date}"
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# put_graph_params = {
#     "quantity": "4.20"
# }
# response = requests.put(url=put_graph_endpoint, json=put_graph_params, headers=headers)
# print(response.text)


#delete
#/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# today = datetime(year=2020, month=12, day=28)    #use to back update
# delete_date = today.strftime('%Y%m%d')
# delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{delete_date}"
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.delete(url=delete_graph_endpoint,  headers=headers)
# print(response.text)