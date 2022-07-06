from curses.ascii import NUL
from urllib import response
from django.db import models
from django.db.models import CharField
# Create your models here.
INSTRUMENT_TYPES=[(1,'Cliente'),(1,'Cuenta'),(3,'Inversion'),(4,'Credito')]
STATUS_TYPES=[('R','Registrado'),('P','Procesado'),('E','Error')]
REQUEST_CHANELS=[(1,'SAFI_LIB'),(2,'SAFI_REST'),(3,'SYGLOBAL_REST')]
REQUEST_TYPES=[('in','Consulta'),('out','Envio')]

class Queue(models.Model):
    instrument=models.SmallIntegerField(choices=INSTRUMENT_TYPES)
    instrument_id= models.IntegerField(verbose_name='InstrumentoID')
    client_id=models.IntegerField(verbose_name='ClienteID')
    current_state=models.CharField(verbose_name='Status',max_length=10, choices=STATUS_TYPES)
    update_on=models.DateTimeField(verbose_name='Actualizado',auto_now=True)
    created_on=models.DateTimeField(verbose_name='Creado',auto_created=True)
    def __str__(self):
        return( str(self.instrument_id))

class LogRequest(models.Model):
    Queue=models.ForeignKey(Queue,on_delete=models.SET_NULL,null=True,blank=True)
    chanel=models.IntegerField(verbose_name='Canal',choices=REQUEST_CHANELS)
    type=models.CharField(verbose_name='Tipo', max_length=5 ,choices=REQUEST_TYPES)
    request=models.TextField(verbose_name='Peticion',max_length=3000)
    response=models.TextField(verbose_name='Respuesta')
    send_on=models.DateTimeField(verbose_name='Fecha Envio',auto_now_add=True)
