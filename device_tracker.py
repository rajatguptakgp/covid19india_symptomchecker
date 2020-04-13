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
    lang_map=pd.DataFrame()
    lang_map['regions']=['West Bengal','Gujarat','Karnataka','Kerala','Maharashtra','Punjab','Tamil Nadu','Telangana','Andhra Pradesh']
    lang_map['language']=['bengali','gujarati','kannada','malayalam','marathi','punjabi','tamil','telugu','telugu']

    lang='hindi'
    lang_id='hi'
  
    for region in lang_map['regions'].values:
        if region in loc_text:
            lang=((lang_map[lang_map['regions']==region]['language']).values)[0]
            lang_id=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]

    #print('\nLanguage: ', lang)
    return lang,lang_id
