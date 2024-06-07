# tech-test
## Install dependencies
	pip install -r requirements.txt	

## Running server
Inside src folder, run 
``` 
fastapi dev main.py 
```

By default the servers listen to 127.0.0.1:8000, you can see the endpoints on ```http://127.0.0.1:8000/docs```

all the endpoints need a parameter *uid* to get the role authorization 

Example:
```
"/policies/user/{number}"
http://127.0.0.1:8000/users/name/Britney?uid=b34368f7-a94c-42ae-8532-53708a592df7
```

routes:
```
"/users/{id}"
"/users/name/{name}"
"/policies/list/{username}"
"/policies/user/{number}"
```
