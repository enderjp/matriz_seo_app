0# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:50:41 2022

@author: darwi
"""
#from dateutil.parser import parse
import dateutil.parser as dparser
import unicodedata
#from quitar_tildes import quitar_tildes


def url_tam(url, keyword):
    
    # Chequeamos si la url tiene menos de 100 caracteres
    if len(url) < 100:
        url_tam = "SI"
    else:
        url_tam = "NO"
        
    return url_tam



# funcion para quitar acentos de una frase/párrafo
def quitar_acentos(string):
    

    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    resultado = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', string).translate(trans_tab))

    return resultado


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
       
                #return True
        cont+=1
       # print(cont)
    except:  #(ValueError, OverflowError):
          pass
        
        
        
    if cont != 0: 
        return "SI"
    else:
        return "NO" # no se consiguieron números que puedan ser interpretados como una fecha
    

#x = contiene_fecha(a)

def tiene_kw(url,keyword):
    
    
    keyword = keyword.replace(" ", "-") # Si tiene más de una palabra, llevamos el 
                                        # keyword al formato que tiene en las urls
    keyword = keyword.replace("ñ", "n")  
    keyword = quitar_acentos(keyword) # Quitar acentos
    
    if keyword.lower() in url.lower():
        return "SI"
    else: 
        return "NO"
    
