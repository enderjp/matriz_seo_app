# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:50:41 2022

@author: darwi
"""
#from dateutil.parser import parse
import dateutil.parser as dparser
import re
from quitar_acentos import quitar_acentos

def longitud(url, keyword):
    
    if len(url) < 100:
        url_tam = "SI"
    else:
        url_tam = "NO"
        
    return url_tam


def contiene_fecha(url):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    cont = 0 # contador para verificar si hay fechas en la URL
    
   # url_split = url.split("/") # separamos la URL por cada "/"
    
    #for i in range(len(url_split)):
        
       # if  url_split[i].isalnum(): # ignorar las cadenas tipo 0406, XXXXXX, etc
            
    try: 
        
        dparser.parse(url, fuzzy=True)
        # si el número de numeros es menor a 4, no lo toma como una fecha
        countNumbers = lambda x: len(re.findall("[0-9]", str(url)));
       
        if countNumbers > 3: 
            
                #return True
                cont+=1
        else:
            pass
       # print(cont)
    except:  #(ValueError, OverflowError):
          pass
        
        
        
    if cont != 0: 
        return "SI"
    else:
        return "NO" # no se consiguieron números que puedan ser interpretados como una fecha
    
def tiene_kw(url,keyword):
      
    keyword = keyword.replace(" ", "-") # Si tiene más de una palabra, llevamos el 
                                        # keyword al formato que tiene en las urls
    keyword = keyword.replace("ñ", "n")  
    keyword = quitar_acentos(keyword) 
    
    if keyword.lower() in url.lower():
        return "SI"
    else: 
        return "NO"
    
