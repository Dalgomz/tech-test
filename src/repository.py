from fastapi import HTTPException
import requests
import pandas as pd

# This file is inteded for connecting directly to a database, however pandas library will be used as fetching the JSON from the api's to mimic SQL database tables

clients_api = 'https://run.mocky.io/v3/532e77dc-2e2d-4a0c-91fd-5ea92ff5d615'
policies_api = 'https://run.mocky.io/v3/289c72a0-8190-4a15-9a15-4118dc2fbde6'

def fetch_clients():
	resp = requests.get(clients_api, timeout=10, headers={'Content-Type': 'application/json'})
	return pd.read_json(resp.text)

def fetch_policies():
	resp = requests.get(policies_api, timeout=10, headers={'Content-Type': 'application/json'})
	return pd.read_json(resp.text)

def auth_user(user_id, allowed_roles):
	df = fetch_clients()
	user_roles = df[df["id"] == user_id]['role']
	if len(user_roles) > 0:
		return user_roles.values[0] in allowed_roles
	
	return False

def fetch_user_by_id(user_id):
	clients_df = fetch_clients()
	response = clients_df[clients_df["id"] == user_id].to_dict(orient="records")
	if len(response) > 0:
		return response[0]
	raise HTTPException(404, "Id Not Found")

def fetch_user_by_name(user_name):
	clients_df = fetch_clients()
	response = clients_df[clients_df["name"] == user_name].to_dict(orient="records")
	if len(response) > 0:
		return response[0]
	raise HTTPException(404, "Name Not Found")

def fetch_policies_by_username(username):
	# Can be achieved in a single query with a join using a real DB 
	clientId = fetch_user_by_name(username)['id']
	policies_df = fetch_policies()
	response = policies_df[policies_df["clientId"] == clientId].to_dict(orient="records")
	if len(response) > 0:
		return response
	raise HTTPException(404, "Policy Not Found")
	
def fetch_policy_owner(policy_number):
	# Can be achieved in a single query with a join using a real DB 
	policies_df = fetch_policies()
	client_id = policies_df[policies_df["id"] == policy_number]['clientId']
	if len(client_id) == 0:
		raise HTTPException(404, "Policy Not Found")
	
	return fetch_user_by_id(client_id.values[0])
