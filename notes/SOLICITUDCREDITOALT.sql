 call SOLICITUDCREDITOALT(
1 -- prospecto *
0 -- cliente * 
9001 -- producto *
'2022-06-23' -- fecha Reg (now)
1 -- promotor *

'N' -- Tipo Creduti (nuevo)
1 -- Num Creditos(calculado) *
0 -- Relacionado (renovacion)
0.0 -- Aporte
1 -- MonedaID (Fijo) pesos

20003 -- Destino Credito (fijo)
'COMPRA ' -- Proyecto (fijo)
1 -- SucursaLID (de la sesion)
3000.0 -- Monto Solicitado (se consulta por WS)*
'31' Plazo ID

2.0 -- Factor Mora
0.0 -- Com apertura
0.0 -- IVA Com Apertura  
'E' -- tipo Dispersion (efectivo)
1 -- Calculo interes (Saldos Insolutos)

0.0 -- tasa base
30.0 -- Tasa Fija *
0.0 -- Sobre Tasa
0.0 -- Piso Tasa
0.0 -- Techo Tasa

'S' -- En Fecha inha = Siguiente
'S' -- Ajust Fecha Ex-Ven
'N' -- Cal irregular
'N' --  Ajust Fecha Ult venc.
'C' --- Tipo Pago Cap (Crecientes)

'M' -- Frec Int Mensual
'M' -- Frec Cap Mensual
30 -- Periodo Int (dias)
30 --  Periodo Cap (dias)
'D' --  dias Pag cap. (dia)

'D' -- dias pag cap (dia mes)
23 -- dia Mes int
23 -- dia mes Cap
6 -- Numn amorti *
484 -- Simulador trans *

35.4 -- CAT *
'' --  Cuenta Clabe
1 --  TipoCalInteres (1) Insolutos
'P' -- Tipo Fonde (Propios)
0 -- Institucion Fondeo

0 -- Linea Fonde
6 -- NumAmort Interes
553.0 -- Monto Cuota *
0.0 -- GrupoID
0.0 -- Tipo Integrante

'2022-12-23' --FechaVencim
'2022-06-23' --FechaInicio
0.0 -- Monto Seg Vida
'' --  Forma Cob SgVida
'O' -- ClasFestCred= O=Consumo

0 -- InstitNominaID
'' -- Folio Ctrl
'' -- Horario Verif
0.0 -- Porc Gar Liqi
'2022-06-23' -- FechaIniAmor

0.0 -- desc seg
0.0 -- Monto seg orig
null -- TipoLiq
0.0 -- CantPagar
'BC' -- Tipo ConsultaSIC

'' -- Folio BC
'' -- Folio CC
'2022-07-25' -- FechaCobro Coimision
0 -- Inversion credAuto
0 -- Cta Cred Auto

'0' -- Cobertura
'0' -- prima
0 -- vigencia
0 -- Convenio NominaID
'' -- Folio Solicitud

0 -- Quinquenio ID
'' -- CLABE domi
'' -- Tipo CtaSantander
'' -- CtaSantander
'' -- CtaCLABE disp

0 -- deudor orig
0 -- Linea CreditoID
null -- Maneja Com Admon
null -- ComAdminLinPreviaLiq
null -- FormPagoComAdmon

0.0 -- Monto Pago ComAdmon
null -- Manje ComGArantia
null -- ComGarLinPrevLiq
null -- formPagoComGarantia
'S' -- Salida

** NOT SPECIFIED ** -- NumError
** NOT SPECIFIED ** -- ErrMen
1
2
'2022-06-23'

		'172.17.0.1'
'CreditosDAO'
1
487);
