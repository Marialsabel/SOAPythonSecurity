#main

import json
##############################################################################################################################

import logging
import time
import multiprocessing
import requests

############################################################################################################################

page: str ="http://127.0.0.1:8090/autenticarusuario"
post_data={"usuario":"Maria", "clave":"1234"}
payload=json.dumps(post_data)
headers={'accept':'application/json','Content-Type':'application/json'}

################################################################################################################################

def multiprocessing_func():
    try:
        response = requests.request("POST",page,headers=headers,data=payload)
        if response.status_code==200:
            print("Solicitud HTTP POST Exitosa",response.text)
    except Exception as e:
        print("Solicitud Fallida")

if __name__=='__main__':
    multiprocessing_func()
            