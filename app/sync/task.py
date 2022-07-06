#import requests
import datetime
from celery import shared_task
#from core.celery import app
from safi.core import Session,Request
from app.sync.models import Queue
import json
import requests
from django.http import request
END_POINT="https://safibodesa.free.beeceptor.com/my/api/path"
@shared_task
def client_updates():
    safi=Session()
    updates=Queue.objects.filter(current_state='R')
    body=[]
    js=json
    for row in updates:
        cuenta_detalle=Request.Account('detail').add(CuentaAhoID=row.instrument_id)
        raw_data=safi.get(cuenta_detalle)
        body.append(raw_data)
        
    print (body)
    data=json.dumps(body,indent=4,default=default)
   # r=requests.post(url=END_POINT,data=body)
    #print(r)
    #print(r.text)

def default(object):
    if isinstance(object, (datetime.date, datetime.datetime)):
        return object.isoformat()