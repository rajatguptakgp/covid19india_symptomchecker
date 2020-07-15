import os
import json
import pandas as pd
import device_tracker
from tqdm import tqdm
import googletrans
from googletrans import Translator
from IPython.display import display
translator = Translator()

os.mkdir('testing_sites')
df=pd.read_csv('data/ICMRTestingLabs.csv')
States=df['State'].values

def testing_sites_translator(df,df_lang,lang_id):
    df_lang=df.copy()
    
    for label in tqdm(df.columns):
        for i in tqdm(range(len(df))):
            try:
                df_lang.loc[i,label]=translator.translate(df[label][i],dest=lang_id).text
            except Exception as e:
                pass

    columns_lang=[]
    for label in df.columns:
        try:
            columns_lang.append(translator.translate(label,dest=lang_id).text)
        except Exception as e:
            pass
    
    df_lang=pd.DataFrame(df_lang.values,columns=columns_lang)
    return df_lang

def translate_data(lang):
    df=pd.read_csv('data/ICMRTestingLabs.csv')
    df=df[:25]
    lang_id=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]
    vars()[f'data_{lang}']=pd.DataFrame()
    vars()[f'data_{lang}']=testing_sites_translator(df,vars()[f'data_{lang}'],lang_id)

    vars()[f'data_{lang}'].to_csv(f'testing_sites/testing_sites_{lang}.csv',index=False)
    return 

class Screen:      
    def __init__(self,lang):        
        self.age = ''
        self.covid_contact = False
        self.covid_exposure = False
        self.new_cough = False
        self.fever = False
        self.shortness_breath = False
        self.sore_throat = False
        self.muscle_ache = False
        self.nurse_facility = False
        self.heart_conditions = False
        self.immunocompromised = False    

def load_dialog_data(lang):
    with open(f'lang_data/dialog_{lang}.json') as json_file: 
        data = json.load(json_file)
    return data 

def load_testing_facilities_data(person_state,lang):
   
    df=pd.read_csv(f'testing_sites/testing_sites_{lang}.csv')
    
    lang_id=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]
    person_state=translator.translate(person_state,dest=lang_id).text
    df_state=df[df[df.columns[4]].values==person_state]
    df_state.reset_index(drop=True,inplace=True)
    return df_state,df
   
def start_diagnoser():    
    question_1()

def get_valid_input(lang):
    choice_text="1-Yes  2-No  3-Not sure   >> "
    lang_id=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]
    result=translator.translate(choice_text,dest=lang_id)
    choice_text=result.text
    option = int(input(choice_text))
    # need to validate the input here
    return option

def ask_user_to_do_covid_test(lang):
    print("\n" + data["7"]['dialog']) 
    
    lang_id=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]
    print()
    print('*'*60)
    print()
    
    print(translator.translate('COVID-19 Testing Site nearest to you',dest=lang_id).text)
    print()
    display(df_state_facilities.loc[:,['lab','pincode','city','state','type']])
    print()
    print('*'*60)
    print()
    
    #print('\nCOVID-19 Testing Sites in India')
    print(translator.translate('\nCOVID-19 Testing Sites in India',dest=lang_id).text)
    display(df_mass_test_facilities.loc[:,['lab','pincode','city','state','type']])
    print()
    print('*'*60)
    print()
    
def ask_user_to_confinue_monitor(lang):
    print("\n" + data["15"]['dialog'])
    
    lang_id=list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(lang)]
    print()
    print('*'*60)
    print()
    
    print(translator.translate('COVID-19 Testing Site nearest to you',dest=lang_id).text)
    print()
    display(df_state_facilities.loc[:,['lab','pincode','city','state','type']])
    print()
    print('*'*60)
    print()
    
    #print('\nCOVID-19 Testing Sites in India')
    print(translator.translate('\nCOVID-19 Testing Sites in India',dest=lang_id).text)
    print()
    display(df_mass_test_facilities.loc[:,['lab','pincode','city','state','type']])
    print('*'*50)
    print()
    

def question_1():
    print("\n" + data["1"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        print(data["1"]['yes_injection'])
        question_3()
        
    elif (option == 2):
        print(data["1"]['no_injection'])
        print("\n" + data["2"]['dialog'])
    
    else:
        print(data["1"]['not_sure_injection'])
        question_3()

def question_3():
    print("\n" + data["3"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.age = "60+"
        print(data["3"]['yes_injection'])               
    
    elif (option == 2):
        screen.age = "18-60"
        print(data["3"]['no_injection'])        
    
    else:
        screen.age = "60+"
        print(data["3"]['not_sure_injection'])            
        
    question_4()

def question_4():
    print("\n" +data["4"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.covid_contact = True
        print(data["4"]['yes_injection'])
                    
    
    elif (option == 2):
        screen.covid_contact = False
        print(data["4"]['no_injection'])    
        
    else:
        screen.covid_contact = True
        print(data["4"]['not_sure_injection'])        
    
    question_5()

def question_5():
    print("\n" +data["5"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.covid_exposure = True        
        if (screen.age == "60+" and screen.covid_exposure == True):
            ask_user_to_do_covid_test(lang)
            
        else:
            print(data["5"]['yes_injection'])
            question_6()                  
    
    elif (option == 2):
        screen.covid_exposure = False        
        print(data["5"]['no_injection'])  
        question_6() 
        
    else:
        screen.covid_exposure = True         
        if (screen.age == "60+" and screen.covid_exposure == True):
            ask_user_to_do_covid_test(lang)
            
        else:
            print(data["5"]['not_sure_injection'])
            question_6() 

def question_6():
    print("\n" +data["6"]["dialog"])
    option = get_valid_input(lang)    
    if (option == 1):
        screen.new_cough = True
        ask_user_to_do_covid_test(lang)
        
    elif (option == 2):
        screen.new_cough = False
        question_8()
        
    else:
        screen.new_cough = True
        ask_user_to_do_covid_test(lang)

def question_8():
    print("\n" +data["8"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.fever = True
        if (screen.new_cough == True and screen.fever == True):
            ask_user_to_do_covid_test(lang)
            
        else:
            question_9()        
        
    elif (option == 2):
        screen.fever = False
        question_9()
        
    else:
        screen.fever = True
        if (screen.new_cough == True and screen.fever == True):
            ask_user_to_do_covid_test(lang)

def question_9():
    print("\n" +data["9"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.shortness_breath = True
        if ((screen.shortness_breath == True and screen.fever == True) or 
            (screen.shortness_breath == True and screen.age == "60+")):
                ask_user_to_do_covid_test(lang)
        else:
            question_10()
    
    elif (option == 2):
        screen.shortness_breath = False
        question_10()
        
    else:
        screen.shortness_breath = True
        if ((screen.shortness_breath == True and screen.fever == True) or 
            (screen.shortness_breath == True and screen.age == "60+")):
                ask_user_to_do_covid_test(lang)
                
        else:
            question_10()

def question_10():
    print("\n" +data["10"]["dialog"])
    option = get_valid_input(lang)   
    if (option == 1):
        screen.sore_throat = True
        if (screen.sore_throat == True and screen.fever == True):
            ask_user_to_do_covid_test(lang)
        
        else:
            print(data["10"]['yes_injection'])
            question_11()
    
    elif (option == 2):
        screen.sore_throat = False
        print(data["10"]['no_injection'])
        question_11()
    
    else:
        screen.sore_throat = True
        if (screen.sore_throat == True and screen.fever == True):
            ask_user_to_do_covid_test(lang)
        
        else:
            print(data["10"]['not_sure_injection'])
            question_11()

def question_11():
    print("\n" +data["11"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.muscle_ache = True
        if (screen.muscle_ache == True and screen.fever == True):
            ask_user_to_do_covid_test(lang)
        
        else:            
            question_12()
    
    elif (option == 2):
        screen.muscle_ache = False        
        question_12()
    
    else:
        screen.muscle_ache = True
        if (screen.muscle_ache == True and screen.fever == True):
            ask_user_to_do_covid_test(lang)
        
        else:            
            question_12()    

def question_12():
    print("\n" +data["12"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.nurse_facility = True
        if (screen.nurse_facility == True and (screen.new_cough == True or
            screen.fever == True or screen.shortness_breath == True or
            screen.sore_throat == True or screen.muscle_ache == True)):
            ask_user_to_do_covid_test(lang)
        
        else:         
            print(data["12"]['yes_injection'])
            question_13()
    
    elif (option == 2):
        screen.nurse_facility = False        
        print(data["12"]['no_injection'])
        question_13()
    
    else:
        screen.muscle_ache = True
        if (screen.nurse_facility == True and (screen.new_cough == True or
            screen.fever == True or screen.shortness_breath == True or
            screen.sore_throat == True or screen.muscle_ache == True)):
            ask_user_to_do_covid_test(lang)
        
        else:         
            print(data["12"]['not_sure_injection'])
            question_13()   

def question_13():
    print("\n" +data["13"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.heart_conditions = True
        if (screen.heart_conditions == True and (screen.new_cough == True or
            screen.fever == True or screen.shortness_breath == True or
            screen.sore_throat == True or screen.muscle_ache == True)):
            ask_user_to_do_covid_test(lang)
        
        else:            
            question_14()
    
    elif (option == 2):
        screen.heart_conditions = False  
        print(data["13"]['no_injection'])
        question_14()
    
    else:
        screen.heart_conditions = True
        if (screen.heart_conditions == True and (screen.new_cough == True or
            screen.fever == True or screen.shortness_breath == True or
            screen.sore_throat == True or screen.muscle_ache == True)):
            ask_user_to_do_covid_test(lang)
        
        else:            
            question_14()  

def question_14():
    print("\n" +data["14"]["dialog"])
    option = get_valid_input(lang)
    if (option == 1):
        screen.immunocompromised = True
        if (screen.immunocompromised == True and (screen.new_cough == True or
            screen.fever == True or screen.shortness_breath == True or
            screen.sore_throat == True or screen.muscle_ache == True)):
            ask_user_to_do_covid_test(lang)
        
        else:            
            ask_user_to_confinue_monitor(lang)
    
    elif (option == 2):
        screen.immunocompromised = False        
        ask_user_to_confinue_monitor(lang)

    else:
        screen.immunocompromised = True
        if (screen.immunocompromised == True and (screen.new_cough == True or
            screen.fever == True or screen.shortness_breath == True or
            screen.sore_throat == True or screen.muscle_ache == True)):
            ask_user_to_do_covid_test(lang)
        
        else:            
            ask_user_to_confinue_monitor(lang)


if __name__ == '__main__':
    
    loc_corr = device_tracker.display_ip()
    #print(loc_corr)

    person_state, loc_text = device_tracker.find_location(loc_corr,States)
    #print('\nLocation: ')
    #print(loc_text)
    
    #print('\nState: ')
    #print(person_state)
    
    lang, lang_id = device_tracker.find_lang_id(loc_text)

    translate_data(lang)
    data = load_dialog_data(lang)
    df_state_facilities, df_mass_test_facilities = load_testing_facilities_data(person_state,lang)
    screen = Screen(lang)
    start_diagnoser()
    
