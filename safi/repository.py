from datetime import date
from datetime import date
from decimal import Decimal

import datetime

today = date.today()

class Base():
    Client=[
       {'routine':'CLIENTESCON',
        'option':1,
        'request':'retrieve',
        'output':'row',
       'parameters':
                    [{'order':'1',
                     'name':'ClienteID',
                     'type':'int',
                      'default':'0',
                     'required':'True' 
                    },
                     {'order':'2',
                     'name':'RFC',
                     'type':'varchar',
                      'default':"''",
                     'required':'True' 
                    },
                    {'order':'3',
                     'name':'CURP',
                     'type':'int',
                      'default':'0',
                     'required':'True' 
                    },
                                        
                    {'order':'3',
                     'name':'NumCon',
                     'type':'int',
                     'default':'1', 
                     'required':'True' 
                    },

                    ]
       },
        
       {'routine':'CLIENTESCON',
        'option':7,
        'request':'resume',
        'output':'row'
        },
        {
        'routine':'DIRECCLIENTELIS',
        'option':1,
        'request':'address',
        'output':'table',
       'parameters':
                    [{'order':1,
                     'name':'ClienteID',
                     'type':int,
                      'default':0,
                     'required':True 
                    },
                     {'order':2,
                     'name':'DirecComple',
                     'type':str,
                      'default':"",
                     'required':False 
                    },
                    {'order':3,
                     'name':'NumList',
                     'type':int,
                      'default':1,# Principal
                     'required':True 
                    },
                                        
                    ]
        }
        
    ]
    Account=[
       {'routine':'CUENTASAHOCON',
        'option':1,
        'request':'detail',
        'output':'row',
       'parameters':
                    [{'order':1,
                     'name':'CuentaAhoID',
                     'type':int,
                      'default':0,
                     'required':True 
                    },
                     {'order':2,
                     'name':'ClienteID',
                     'type':int,
                      'default':0,
                     'required':False 
                    },
                    {'order':3,
                     'name':'Mes',
                     'type':int,
                     'default':0,
                     'required':True 
                    },                                        
                    {'order':4,
                     'name':'Anio',
                     'type':int,
                     'default':0, 
                     'required':False 
                    },
                    {'order':5,
                     'name':'TipoCuenta',
                     'type':int,
                     'default':0, 
                     'required':False 
                    },
                    {'order':6,
                     'name':'NumCon',
                     'type':int,
                     'default':1, # Principal
                     'required':False 
                    },

                    ]
       },
    
      
    ]


    Loan=[
      
      {'routine':'SOLICITUDCREDITOALT',
        'option':0,
        'request':'application',
        'output':'message',
       'parameters':
                    [{'order':1,
                     'name':'ProspectoID',
                     'type':int,
                     'default':0,
                     'required':True 
                    },
                     {'order':2,
                     'name':'ClienteID',
                     'type':int,
                      'default':0,
                     'required':True 
                    },
                    {'order':3,
                     'name':'ProductCredID',
                     'type':int,
                      'default':0,
                     'required':True 
                    },
                                        
                    {'order':4,
                     'name':'FechaReg',
                     'type':date,
                     'default':datetime.date, 
                     'required':False 
                    },
                    {'order':5,
                     'name':'PromotorID',
                     'type':int,
                     'default':1, 
                     'required':True 
                    },

                    {'order':6,
                     'name':'TipoCredito',
                     'type':str,
                     'default':'N', # N=uevo
                     'required':False 
                    },
                    {'order':7,
                     'name':'NumCreditos',
                     'type':int,
                     'default':0, #
                     'required':False 
                    },
                    {'order':8,
                     'name':'Relacionado',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':9,
                     'name':'AporCliente',
                     'type':Decimal,
                     'default':0.00,
                     'required':False 
                    },

                    {'order':10,
                     'name':'MonedaID',
                     'type':int,
                     'default':1,
                     'required':False 
                    },
                    {'order':11,
                     'name':'DestinoCreditoID',
                     'type':int,
                     'default':20003,# Consumo
                     'required':False 
                    },
                    {'order':12,
                     'name':'Proyecto',
                     'type':str,
                     'default':"'Disposici??n de Cr??dito'",
                     'required':False 
                    },
                    {'order':13,
                     'name':'SucursalID',
                     'type':int,
                     'default':1,
                     'required':False 
                    },
                   {'order':14,
                     'name':'MontoSolicitado',
                     'type':Decimal,
                     'default':0.00,
                     'required':True 
                    },
                    {'order':15,
                     'name':'PlazoID',
                     'type':int,
                     'default':0,
                     'required':True 
                    },
                    {'order':16,
                     'name':'FactorMora',
                     'type':Decimal,
                     'default':0.00,
                     'required':False 
                    },
                    {'order':17,
                     'name':'ComApertura',
                     'type':Decimal,
                     'default':0.00,
                     'required':False 
                    },
                    {'order':18,
                     'name':'IVAComApertura',
                     'type':Decimal,
                     'default':0.00,
                     'required':False 
                    },
                    {'order':19,
                     'name':'TipoDispersion',
                     'type':str,
                     'default':'E',
                     'required':False 
                    },
                    {'order':20,
                     'name':'CalcInteres',
                     'type':int,
                     'default':1,# Saldos Insolutos
                     'required':False 
                    },
                    {'order':21,
                     'name':'TasaBase',
                     'type':Decimal,
                     'default':0,# Saldos Insolutos
                     'required':False 
                    },
                    {'order':22,
                     'name':'TasaFija',
                     'type':Decimal,
                     'default':0,# Saldos Insolutos
                     'required':True 
                    },
                    {'order':23,
                     'name':'SobreTasa',
                     'type':Decimal,
                     'default':0,# Saldos Insolutos
                     'required':False 
                    },
                    {'order':24,
                     'name':'PisoTasa',
                     'type':Decimal,
                     'default':0,# Saldos Insolutos
                     'required':False 
                    },
                    {'order':25,
                     'name':'TechoTasa',
                     'type':Decimal,
                     'default':0,# Saldos Insolutos
                     'required':True 
                    },
                    {'order':26,
                     'name':'FechaInhabil',
                     'type':str,
                     'default':'S',
                     'required':False 
                    },
                    {'order':27,
                     'name':'AjuFechExiVen',
                     'type':str,
                     'default':'N',
                     'required':False 
                    },
                    {'order':28,
                     'name':'CalIrreg',
                     'type':str,
                     'default':'N', # Calendario Irrgular
                     'required':False 
                    },
                    {'order':29,
                     'name':'AjuFechUltVenAmo',
                     'type':str,
                     'default':'S', 
                     'required':False 
                    },
                    {'order':30,
                     'name':'TipoPagoCap',
                     'type':str,
                     'default':'C', #Crecientes
                     'required':False 
                    },
                    {'order':31,
                     'name':'FrecInteres',
                     'type':str,
                     'default':'M', #Mensual
                     'required':False 
                    },
                    {'order':32,
                     'name':'FrecCapital',
                     'type':str,
                     'default':'M', #Mensual
                     'required':False 
                    },
                    {'order':33,
                     'name':'PeriodInt',
                     'type':int,
                     'default':30, #30 dias
                     'required':False 
                    },
                    {'order':34,
                     'name':'PeriodCap',
                     'type':int,
                     'default':30, #30 dias
                     'required':False 
                    },
                    {'order':35,
                     'name':'DiaPagInt',
                     'type':str,
                     'default':'D', #30 dias
                     'required':False 
                    },
                    {'order':36,
                     'name':'DiaPagCapital',
                     'type':str,
                     'default':'D', #30 dias
                     'required':False 
                    },
                    {'order':37,
                     'name':'DiaMesInt',
                     'type':int,
                     'default':30, #30 dias
                     'required':True
                    },
                    {'order':38,
                     'name':'DiaMesCap',
                     'type':int,
                     'default':30, #30 dias
                     'required':True 
                    },
                    {'order':39,
                     'name':'NumAmorti',
                     'type':int,
                     'default':0, #30 dias
                     'required':True 
                    },
                    {'order':40,
                     'name':'NumTransacSim',
                     'type':int,
                     'default':0, #30 dias
                     'required':False 
                    },
                    {'order':41,
                     'name':'CAT',
                     'type':Decimal,
                     'default':0, #
                     'required':True 
                    },
                    {'order':42,
                     'name':'CuentaCLABE',
                     'type':str,
                     'default':"''", 
                     'required':False 
                    },
                    {'order':43,
                     'name':'TipoCalcInteres',
                     'type':int,
                     'default':1, #Saldos insolutos
                     'required':False
                    },
                    {'order':44,
                     'name':'TipoFondeo',
                     'type':str,
                     'default':'P',#Recursos Propios
                     'required':False 
                    },
                    {'order':45,
                     'name':'InstitFondeoID',
                     'type':int,
                     'default':0, 
                     'required':False 
                    },
                    {'order':46,
                     'name':'LineaFondeo',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':47,
                     'name':'NumAmortInteres',
                     'type':int,
                     'default':0, 
                     'required':True 
                    },
                    {'order':48,
                     'name':'MontoCuota',
                     'type':Decimal,
                     'default':0,
                     'required':True 
                    },
                    {'order':49,
                     'name':'GrupoID',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':50,
                     'name':'TipoIntegr',
                     'type':int,
                     'default':0, 
                     'required':False 
                    },
                    {'order':51,
                     'name':'FechaVencim',
                     'type':date,
                     'default':today.strftime("%M-%d-%y"), 
                     'required':True
                    },
                    {'order':52,
                     'name':'FechaInicio',
                     'type':date,
                     'default':today.strftime("%M-%d-%y"), 
                     'required':True 
                    },
                    {'order':53,
                     'name':'MontoSegVida',
                     'type':Decimal,
                     'default':0, #30 dias
                     'required':False 
                    },
                    {'order':54,
                     'name':'ForCobrSegVida',
                     'type':str,
                     'default':"", 
                     'required':False 
                    },
                    {'order':55,
                     'name':'ClasiDestinCred',
                     'type':str,
                     'default':'O', #'O'=Consumo
                     'required':True 
                    },
                    {'order':56,
                     'name':'InstNominaID',
                     'type':int,
                     'default':0, 
                     'required':False 
                    },
                    {'order':57,
                     'name':'FolioCtrl',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':58,
                     'name':'HorarioVerif',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':59,
                     'name':'PorcGarLiq',
                     'type':Decimal,
                     'default':0, 
                     'required':False 
                    },
                    {'order':60,
                     'name':'FechaInicioAmor',
                     'type':date,
                     'default':today.strftime("%M-%d-%y"),
                     'required':True 
                    },
                    {'order':61,
                     'name':'DescuentoSeg',
                     'type':Decimal,
                     'default':0,
                     'required':False 
                    },
                    {'order':62,
                     'name':'MontoSegOrig',
                     'type':Decimal,
                     'default':0,
                     'required':False 
                    },
                    {'order':63,
                     'name':'TipoLiq',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':64,
                     'name':'CantPagar',
                     'type':Decimal,
                     'default':0,
                     'required':False 
                    },
                    {'order':65,
                     'name':'TipoConsultaSIC',
                     'type':str,
                     'default':'BC',# buro de Credito
                     'required':False 
                    },
                    {'order':66,
                     'name':'FolioConsultaBC',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':67,
                     'name':'FolioConsultaCC',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':68,
                     'name':'FechaCobroCom',
                     'type':date,
                     'default':today ,
                     'required':False 
                    },
                    {'order':69,
                     'name':'InverCredAuto',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':70,
                     'name':'CtaCredAuto',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':71,
                     'name':'Cobertura',
                     'type':Decimal,
                     'default':0,
                     'required':False 
                    },
                    {'order':72,
                     'name':'Prima',
                     'type':Decimal,
                     'default':0,
                     'required':False 
                    },
                    {'order':73,
                     'name':'Vigencia',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':74,
                     'name':'ConvenioNominaID',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':75,
                     'name':'FolioSolici',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':76,
                     'name':'QuinquenioID',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':77,
                     'name':'CLABEDomiciliacion',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':78,
                     'name':'TipoCtaSantander',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':79,
                     'name':'CtaSantander',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':80,
                     'name':'CtaCLABEDisp',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    {'order':81,
                     'name':'DeudorOriginalID',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':82,
                     'name':'LineaCreditoID',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':83,
                     'name':'ManejaComAdmon',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':84,
                     'name':'ComAdmonLinPrevLiq',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':85,
                     'name':'FormPagoComAdmon',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':86,
                     'name':'MontoPagoComAdmon',
                     'type':Decimal,
                     'default':0,
                     'required':False 
                    },
                    {'order':87,
                     'name':'ManejaComGarantia',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':88,
                     'name':'ComGarLinPrevLiq',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':89,
                     'name':'ForPagComGarantia',
                     'type':str,
                     'default':"",
                     'required':False 
                    },
                    {'order':90,
                     'name':'Salida',
                     'type':str,
                     'default':'S',
                     'required':False 
                    },
                    {'order':91,
                     'name':'NumError',
                     'type':int,
                     'default':0,
                     'required':False 
                    },
                    {'order':92,
                     'name':'ErrMen',
                     'type':str,
                     'default':"''",
                     'required':False 
                    },
                    ]
      }
                    

      ]
       
    
    Founds=[]