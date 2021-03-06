import literals as msg
import csv
from datetime import datetime

#Amb aquesta funció(que va compartir en Nil) puc validar tots els rangs de valors.
def validate(msg, ini, fin):
   if fin is None:
       num = int(input(msg))
       while num < ini:
           num = int(input(msg))
   elif ini is None:
       num = int(input(msg))
       while num > fin:
           num = int(input(msg))
   elif ini is not None and fin is not None:
       num = int(input(msg))
       while num < ini or num > fin:
           num = int(input(msg))
   else:
       num = int(input(msg))
   return num

#Amb la següent funció s'omple el diccionari.
def dictionary():
   sentinella = dict()
   sentinella['Curs'] = input(msg.MSG1)
   sentinella['Aula'] = input(msg.MSG2)
   sentinella['Nºalumnes'] = validate(msg.MSG3, 0, None)
   sentinella['Nºprofessors/es'] = validate(msg.MSG4, 0, None)
   any = validate(msg.MSG5, 2020, None)
   mes = validate(msg.MSG6, 1, 12)
   if mes == 2:
       dia = validate(msg.MSG7, 1, 28)
   elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
       dia = validate(msg.MSG7, 0 , 31)
   else:
       dia = validate(msg.MSG7, 1, 30)
   sentinella['Data'] = str(dia) + '-' + str(mes) + '-' + str(any)
   hora =  datetime.now().time()
   sentinella['Hora'] = hora
   sentinella['CO2'] = validate(msg.MSG8, 0, None)
   sentinella['Temperatura'] = validate(msg.MSG9, -15, 50)
   sentinella['Humitat'] = validate(msg.MSG10, 0, 100)
   sentinella['Professor'] = input(msg.MSG11)
   sentinella['Assignatura'] = input(msg.MSG12)
   portasecun = validate(msg.MSG13, 1, 2)
   finestresext = validate(msg.MSG14, 1, 2)
   finestresint = validate(msg.MSG15, 1, 2)
   sentinella['Minuts porta principal oberta'] = validate(msg.MSG16, 0, 60)
   sentinella['Minuts porta principal tancada'] = 60 - sentinella['Minuts porta principal oberta']
   if portasecun == 1:
       sentinella['Minuts porta secundària oberta'] = validate(msg.MSG17, 0, 60)
       sentinella['Minuts porta secundària tancada'] = 60 - sentinella['Minuts porta secundària oberta']
   else:
       sentinella['Minuts porta secundària oberta'] = 0
       sentinella['Minuts porta secundària tancada'] = 0
   if finestresext == 1:
       sentinella['Minuts finestra externa oberta'] = validate(msg.MSG18, 0, 60)
       sentinella['Minuts finestra externa tancada'] = 60 - sentinella['Minuts finestra externa oberta']
   else:
       sentinella['Minuts finestra externa oberta'] = 0
       sentinella['Minuts finestra externa tancada'] = 0
   if finestresint == 1:
       sentinella['Minuts finestra interna oberta'] = validate(msg.MSG19, 0, 60)
       sentinella['Minuts finestra interna tancada'] = 60 - sentinella['Minuts finestra interna oberta']
   else:
       sentinella['Minuts finestra interna oberta'] = 0
       sentinella['Minuts finestra interna tancada'] = 0
   ventcreu = validate(msg.MSG20, 1, 2)
   if ventcreu == 1:
       sentinella['Ventilació creuada'] = 'Sí.'
   else:
       sentinella['Ventilació creuada'] = 'No.'
   return sentinella

#Aquesta funció serveix per veure si el fitxer existeix o no.
def fitxer_existent(file):
   try:
       with open(file, 'r'):
           return 1
   except FileNotFoundError:
       return 0

#Aquesta funció serveix per a que el fitxer tingui l'extensió desitjada.
def nomfitxer():
   f = input(msg.MSGNAME)
   if f[-4:] == '.csv':
       f = 'files/' + f
   else:
       f = 'files/' + f + '.csv'
   return f

#Amb aquesta funció s'introdueixen els registres al fitxer.
def introregistres(f_name, method, header):
   registres = 1
   try:
       with open(f_name, method, encoding='utf-8', newline='\n') as csvfile:
           fieldnames = ['Curs', 'Aula', 'Nºalumnes', 'Nºprofessors/es', 'Data', 'Hora', 'CO2', 'Temperatura', 'Humitat', 'Professor',
                         'Assignatura', 'Minuts porta principal oberta', 'Minuts porta principal tancada', 'Minuts porta secundària oberta',
                         'Minuts porta secundària tancada', 'Minuts finestra externa oberta', 'Minuts finestra externa tancada',
                         'Minuts finestra interna oberta', 'Minuts finestra interna tancada', 'Ventilació creuada']
           writecsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
           if header == 0 or method == 'w':
               writecsv.writeheader()
           while registres == 1:
               sentinella = dictionary()
               writecsv.writerow(sentinella)
               registres = validate(msg.MSG21, 1, 2)
   except:
       print(msg.MSG22)
   else:
       print(msg.MSG23)


