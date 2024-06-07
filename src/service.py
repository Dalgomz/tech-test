import repository

def auth_user(user_id, allowed_roles=[]):
	return repository.auth_user(user_id, allowed_roles)
	
def get_user_by_id(user_id):
	return repository.fetch_user_by_id(user_id)

def get_user_by_name(user_name):
	return repository.fetch_user_by_name(user_name)

def get_policy_by_user(user_id):
	return repository.fetch_policy_by_user(user_id)

def get_policy_owner(policy_name):
	return repository.fetch_policy_by_user(policy_name)
