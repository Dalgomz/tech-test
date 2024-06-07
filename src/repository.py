import requests
import pandas as pd

clients_api = 'https://run.mocky.io/v3/532e77dc-2e2d-4a0c-91fd-5ea92ff5d615'
policies_api = 'https://run.mocky.io/v3/289c72a0-8190-4a15-9a15-4118dc2fbde6'

def fetch_clients():
	resp = requests.get(clients_api, timeout=10, headers={'Content-Type': 'application/json'})
	return pd.read_json(resp.text)

def fetch_policies():
	resp = requests.get(policies_api, timeout=10, headers={'Content-Type': 'application/json'})
	return pd.read_json(resp.text)

def auth_user(user_id, allowed_roles):
	return True

def fetch_user_by_id(user_id):
	return {}

def fetch_user_by_name(user_name):
	return {}


def fetch_policy_by_user(user_id):
	return {}


def fetch_policy_owner(user_name):
	return {}
