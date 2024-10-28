
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
            print(response.json()['links'])
            self.airports_cursor = response.json()['links']['next']
        else :
            self.cont=False
        return response.json()
        
      
    
    def get_flights(self, airport_code:str, pages:int=1) :
        while self.cont :
            if self.airports_cursor == None :
                data = self.get_flights_from_airport(airport_code)
                MyList = [
                    {
                        'flight_id' : row['fa_flight_id'],
                        'aircraft_type' : row['aircraft_type'],
                        'destination_city' : row['destination']['city'],
                        'origin_city' : row['origin']['city']
                    } for row in data['arrivals']]
                data_df = pd.DataFrame.from_records(MyList)
                self.airports_data.append(data_df)
            else :
                data = self.get_flights_from_airport(airport_code, cursor=self.airports_cursor)
                MyList = [
                    {
                        'flight_id' : row['fa_flight_id'],
                        'aircraft_type' : row['aircraft_type'],
                        'destination_city' : row['destination']['city'],
                        'origin_city' : row['origin']['city']
                    } for row in data['arrivals']]
                data_df = pd.DataFrame.from_records(MyList)
                self.airports_data.append(data_df)
        self.airports_data_in_df = pd.concat(self.airports_data)

        # print(self.airports_data_in_df)
        return self.airports_data_in_df
        
myaero = Aero()
x = myaero.get_flights('LGSR', 10)


#%%
# Get data for Arrivals / Departures / Scheduled Arrivals / Scheduled Departures


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
