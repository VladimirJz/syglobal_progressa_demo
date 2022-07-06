from django.urls import path,include
from app.loans.views import ApplicationFormView

urlpatterns=[
    path('solicitud/',ApplicationFormView.as_view(),name='solicitud'),
]