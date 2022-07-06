from datetime import date
from django.db import connections
from  .repository import Base
'''Engine set an handle the database configuration'''   
class Session():
    
    def get(self,request):
        params=request.parameters
        audit=[ 1, 1, date.today(), '127.0.0.1', 'api.rest', 1, 1]
        params.extend(audit)
        print (request.routine)
        print (params)

        with connections['core'].cursor() as cursor:       
            cursor.callproc(request.routine,params)
            raw_data = self.fetch_raw(cursor) 
            

        return raw_data

        
    def fetch_raw(self, cursor):
        columns = [col[0] for col in cursor.description]
        print (cursor.rowcount)
        if cursor.rowcount>1:
            results=[]
        else:
            results={}
        #results = []
        for row in cursor.fetchall():
            #print (row)
            if cursor.rowcount>1:
                results.append(dict(zip(columns, row))) # for list
            else:


                results=dict(zip(columns, row))
        return results
    
    
    class Connection():
        @property
        def string_connection(self):
            return self._string_connection
        
        @string_connection.setter
        def string_connection(self,value):
            self._string_connection = value
        pass
    class License():
                
        @property
        def licence_key(self):
            return self._licence_key
        
        @licence_key.setter
        def licence_key(self,value):
            self._licence_key = value
        pass
    pass

## Session (Request(Session)) Class manage the prepare and  run request
class Request():
    def __init__(self,user,Engine):
        #repo=Repository()
        print(type(self))
        self._audit=[ 1, 1, date.today(), '127.0.0.1', 'api.rest', 1, 1]
        pass
     
      
    class GenericRequest():
        def __init__(self,request):
            #print(repo)
            self._properties=''
            self._parameters=[]
            self._routine=''
            
        def run(self):
            return {'output':'json'}
            pass

        
        def get_props(self,request, repository):
            return [element for element in repository if element['request'] == request]
        
        def add(self,**kwargs):
            raw_parameters=[]
            unpack=self.properties[0]
            self._routine=unpack['routine']
            parameter_properties=unpack['parameters']
            for par in parameter_properties:
                #print(par['name'])
                value= kwargs.get(par['name'],par['default'])
                raw_parameters.append(value)
            self._parameters= raw_parameters
            
            return self
  
        
        @property
        def properties(self):
            return self._properties
        
        @properties.setter
        def properties(self,value):
            self._properties = value
        
        @property
        def parameters(self):
            return self._parameters
        
        @parameters.setter
        def parameters(self,value):
            self._parameters = value
            
        @property
        def routine(self):
            return self._routine
        
        @routine.setter
        def routine(self,value):
            self._routine = value           
            
            
            
            
    class Account(GenericRequest):
        def __init__(self,request):
            super().__init__(request)
            repository=Base.Account
            self.properties=self.get_props(request,repository)
            

    class Client(GenericRequest):
        def __init__(self,request):
            super().__init__(request)
            repository=Base.Client
            self.properties=self.get_props(request,repository)

    class Loan(GenericRequest):
            def __init__(self,request):
                super().__init__(request)
                repository=Base.Loan
                self.properties=self.get_props(request,repository)
