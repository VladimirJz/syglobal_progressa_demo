from django.http import HttpResponse
import re
from django.shortcuts import render,redirect

# Create your views here.
from app.loans.forms import ApplicationForm
from django.views.generic.edit import FormView
from safi.core import Session,Request
from safi.repository import Base

class ApplicationFormView(FormView):
    safi=Session()
    template_name= 'loans/application.html'
    form_class=ApplicationForm
    success_url= '.'
    def post(self,request,*args,**kwargs):
        #print(request.POST.get('ClienteID'))
        context=self.get_context_data()
        form=ApplicationForm(request.POST)
        print(form['ClienteID'].value())
        Monto=form['MontoSolicitado'].value()
        ClienteID=form['ClienteID'].value()
        solicitud=Request.Loan('application').add(ClienteID=ClienteID,ProductCredID=9001,FechaReg='2022-07-05',PromotorID=1,NumCreditos=1,MontoSolicitado=Monto,PlazoID=31,TasaFija=30)
        print(solicitud)
        raw_data=self.safi.get(solicitud)
        print(raw_data)
        context['output']=raw_data
        #return redirect("solicitud")
        return HttpResponse(str(raw_data))
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        form=ApplicationForm(self.request.POST or None)
        context['form']=form
        return context