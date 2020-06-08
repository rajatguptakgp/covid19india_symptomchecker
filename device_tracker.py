import requests
from geopy.geocoders import Nominatim

import pandas as pd

import googletrans
from googletrans import Translator

def display_ip():
    """  Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' + my_ip + '.json')
    geo_data = geo_request.json()
    return {'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']}
    
def find_location(loc_corr,States):
    geolocator = Nominatim(user_agent='python3')
    location = geolocator.reverse(loc_corr['latitude'] + ',' + loc_corr['longitude'])
    
    person_state='Delhi'
    for state in States:
        if state in location[0]:
            person_state=state
            
    return person_state,location[0] 
    
def find_lang_id(loc_text):
    df=pd.read_csv('language_data.csv')

    lang_map=pd.DataFrame()
    lang_map['regions']=df['state'].values
    lang_map['language']=df['language'].values

    lang='english'
    lang_id='en'
  
    for region in lang_map['regions'].values:
        if region in loc_text:
            try:
                lang=((lang_map[lang_map['regions']==region]['language']).values)[0]
                lang_id=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]
            except Exception as e:
                pass

    #print('\nLanguage: ', lang)
    return lang,lang_id
