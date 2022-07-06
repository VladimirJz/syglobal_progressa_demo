import os
from celery import Celery
#safi


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'core.settings')
app = Celery('app.sync')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
from safi.core import Request,Session
from safi.repository import Base


# Async task

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True)
def hello_world(self):
    print('Consulta a SAFI >>!')

@app.task(bind=True)
def client_updates(self):
    updates=Queue.objects.filter(current_state='R')
    print (updates)
    #safi=Session()
    #raw_data={}
    #updates=Request.
    #cuenta_detalle=Request.Account('detail').add(CuentaAhoID=pk,NumCon=option)
    #raw_data=safi.get(cuenta_detalle)
    #cliente=ClienteViewModel(raw_data)
    #serializer=()


    pass

