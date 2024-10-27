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
    
    def get_airports(self) :
        for i in range(5) :
            print(i, len(self.airports_data))
            if self.airports_cursor == None :
                self.get_airports_page()
            else :
                self.get_airports_page(cursor=self.airports_cursor)


myaero = Aero()
myaero.get_airports()
        

