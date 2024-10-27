
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
        self.list_to_return = [row for row in response.json()['airports'] if row['code'] == 'JTR']
        return self.list_to_return
        

        
    
    def get_airports(self, pages:int=10) :
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
