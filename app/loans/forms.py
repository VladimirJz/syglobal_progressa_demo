from tkinter.tix import Form
from django import forms

PRODUCTS=[(9001,'Disposicion BODESA'),(9999,'OtrosProductos')]
PROMOTER=[(1,'Promotor Bodesa')]
PLAZOS=[(31,'Seis Meses'),(1,'Otros Plazos..')]
class ApplicationForm(forms.Form):
    ClienteID=forms.IntegerField()
    ProductoID=forms.ChoiceField(choices=PRODUCTS)
    PromotorID=forms.ChoiceField(choices=PROMOTER)
    MontoSolicitado=forms.DecimalField(max_digits=11,decimal_places=2)
    Plazo=forms.ChoiceField(choices=PLAZOS)

