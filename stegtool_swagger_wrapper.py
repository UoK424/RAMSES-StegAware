import requests
import json

url = 'https://ramses.treelogic.com/auth/realms/ramses/protocol/openid-connect/token'

def authenticate (usrnm, password):
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = [
          ('client_id', 'desktopapps-cli'),
          ('username', usrnm),
          ('password', password),
          ('client_secret', 'e32d1260-4724-4148-aefd-d9df677ecd78'),
          ('grant_type', 'password'),
        ]
        
        r = requests.post(url, headers=headers, data=data)
        return r

def get_list (token,params):
        headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer '+str(token),
        }

        r = requests.get('https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/steganography', headers=headers, params=params)
        return r
	
def post_result (token, result):
        headers = {
        'Content-Type': 'application/json',
		'Authorization': 'Bearer '+str(token),
        'Accept': 'application/json'
        }
		
        r = requests.post('https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/steganography', headers=headers, data=json.dumps(result))
        return r

def delete_result (token,id):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+str(token),
        'Accept': 'application/json',
        }

        r = requests.delete('https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/steganography/'+str(id), headers=headers)
        return r
	
def get_result (token,id):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+str(token),
        'Accept': 'application/json',
        }

        r = requests.get('https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/steganography/'+str(id), headers=headers)
        return r
	
def update_result (token, result, id):
        headers = {
        'Content-Type': 'application/json',
		'Authorization': 'Bearer '+str(token),
        'Accept': 'application/json'
        }
		

        r = requests.post('https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/steganography/'+str(id), headers=headers, data=json.dumps(result))
        return r

def scan_list (token):
        exists = []
        f = 0
        while True:
            params = (('size',1000),('from',f),)
            e = get_list(token,params).content
            e = json.loads(e.decode())
            if e == []:
                break
            else:
                for i in e:
                    exists.append(i)
                    f = f+1
           
        return exists
                
                


