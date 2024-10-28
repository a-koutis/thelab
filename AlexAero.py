#%%
import requests 
from typing import List
class Aero() :
    baseurl='https://aeroapi.flightaware.com/aeroapi'
    token='PgtpRAzyCMCFviNHWYNxw8GPmgKhnye2'
    airports_data:List=[]
    airports_cursor:str=None
    def __init__(self) :
        ...
    def get_airports_page(self, cursor:str=None) :
        if cursor == None :
            url = f'{self.baseurl}/airports'
        else :
            url = f'{self.baseurl}{cursor}'
        response = requests.get(
            url,
            headers={'x-apikey':self.token}
            )
        self.airports_data.append(response.json()['airports'])
        self.airports_cursor = response.json()['links']['next']
    
    def get_airports(self, pages:int=1) :
        for i in range(pages) :
            print(i, len(self.airports_data))
            if self.airports_cursor == None :
                self.get_airports_page()
            else :
                self.get_airports_page(cursor=self.airports_cursor)


myaero = Aero()
myaero.get_airports(3)
        

#%%
# Na stamataei otan ferei ola taeirports

# Questions: how do we view the last page of the json file?

import requests 
from typing import List
class Aero() :
    baseurl='https://aeroapi.flightaware.com/aeroapi'
    token='PgtpRAzyCMCFviNHWYNxw8GPmgKhnye2'
    airports_data:List=[]
    airports_cursor:str=None
    which_page:int=None
    def __init__(self) :
        ...
    def get_airports_page(self, cursor:str=None) :
        if cursor == None :
            url = f'{self.baseurl}/airports'
        else :
            url = f'{self.baseurl}{cursor}'
        response = requests.get(
            url,
            headers={'x-apikey':self.token}
            )
        self.airports_data.append(response.json()['airports'])
        self.airports_cursor = response.json()['links']['next']
        self.which_page = response.json()['num_pages']['next']
    
    def get_airports(self) :
        while self.airports_cursor !=None  :
            print(len(self.airports_data))
            if self.airports_cursor == None :
                self.get_airports_page()
            else :
                self.get_airports_page(cursor=self.airports_cursor)


myaero = Aero()
myaero.get_airports()

#%%
# Get Data into a DF

# Giati den kanei print to df?

import requests 
import pandas as pd
from typing import List
class Aero() :
    baseurl='https://aeroapi.flightaware.com/aeroapi'
    token='PgtpRAzyCMCFviNHWYNxw8GPmgKhnye2'
    airports_data:List=[]
    airports_cursor:str=None
    airports_data_in_df:pd.DataFrame
    def __init__(self) :
        ...
    def get_airports_page(self, cursor:str=None) :
        if cursor == None :
            url = f'{self.baseurl}/airports'
        else :
            url = f'{self.baseurl}{cursor}'
        response = requests.get(
            url,
            headers={'x-apikey':self.token}
            )
        self.airports_cursor = response.json()['links']['next']
        return response.json()['airports']
        

        
    
    def get_airports(self, pages:int=1) :
        for i in range(pages) :
            print(i, len(self.airports_data))
            if self.airports_cursor == None :
                data = self.get_airports_page()
                data_df = pd.DataFrame.from_records(data)
                self.airports_data.append(data_df)
            else :
                data = self.get_airports_page(cursor=self.airports_cursor)
                data_df = pd.DataFrame.from_records(data)
                self.airports_data.append(data_df)
        self.airports_data_in_df = pd.concat(self.airports_data)

        print(self.airports_data_in_df)
        
myaero = Aero()
myaero.get_airports(3)

# %%



#%%
# Get Data into a DF


import requests 
import pandas as pd
from typing import List
from dotenv import load_dotenv
import os
load_dotenv()

class Aero() :
    baseurl='https://aeroapi.flightaware.com/aeroapi'
    token=os.environ['token']
    airports_data:List=[]
    airports_cursor:str=None
    airports_data_in_df:pd.DataFrame
    list_to_return:list=[]
    cont:bool = True
    def __init__(self) :
        ...
    def get_flights_from_airport(self, airport_code:str, cursor:str=None) :
        """ """
        if cursor == None :
            url = f'{self.baseurl}/airports/{airport_code}/flights'
        else :
            url = f'{self.baseurl}{cursor}'
        response = requests.get(
            url,
            headers={'x-apikey':self.token}
            )
        print(response.text)
        if response.json()['links'] != None:
            print('My comment is :')
            print(response.json()['links'])
            self.airports_cursor = response.json()['links']['next']
        else :
            self.cont=False
        return response.json()
        
      
    
    def get_flights(self, airport_code:str, pages:int=1) :
        while self.cont :
            for type_of_flight in ('arrivals', 'departures', 'scheduled_arrivals', 'scheduled_departures'):
                if self.airports_cursor == None :
                    data = self.get_flights_from_airport(airport_code)
                    MyList = [
                        {
                            'flight_id' : row['fa_flight_id'],
                            'aircraft_type' : row['aircraft_type'],
                            'destination_city' : row['destination']['city'],
                            'origin_city' : row['origin']['city'],
                            'type_of_flight' : type_of_flight
                        } for row in data[type_of_flight]]
                    data_df = pd.DataFrame.from_records(MyList)
                    self.airports_data.append(data_df)
                else :
                    data = self.get_flights_from_airport(airport_code, cursor=self.airports_cursor)
                    MyList = [
                        {
                            'flight_id' : row['fa_flight_id'],
                            'aircraft_type' : row['aircraft_type'],
                            'destination_city' : row['destination']['city'],
                            'origin_city' : row['origin']['city'], 
                            'type_of_flight' : type_of_flight
                        } for row in data[type_of_flight]]
                    data_df = pd.DataFrame.from_records(MyList)
                    self.airports_data.append(data_df)
        self.airports_data_in_df = pd.concat(self.airports_data)

        # print(self.airports_data_in_df)
        return self.airports_data_in_df
        
myaero = Aero()
x = myaero.get_flights('LGSR', 10)

# %%
# fa_flight_id, aircraft_type, origin_name, destination_name