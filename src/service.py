import repository

def auth_user(user_id, allowed_roles=[]):
	return repository.auth_user(user_id, allowed_roles)
	
def get_user_by_id(user_id):
	return repository.fetch_user_by_id(user_id)

def get_user_by_name(username):
	return repository.fetch_user_by_name(username)

def get_policies_by_username(username):
	return repository.fetch_policies_by_username(username)

def get_policy_owner(policy_name):
	return repository.fetch_policy_owner(policy_name)
