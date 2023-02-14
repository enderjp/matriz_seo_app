# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:50:41 2022

@author: darwi
"""
#from dateutil.parser import parse
import re
from quitar_acentos import quitar_acentos

def longitud(url):
    
    if len(url) < 100:
        url_tam = "SI"
    else:
        url_tam = "NO"
        
    return url_tam



    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    
def contiene_fecha(url):
    # Expresiones regulares para fechas en los formatos YYYY, YYYY/MM y YYYY/MM/DD
    date_regex1 = r"\b\d{4}\b"
    date_regex2 = r"\b\d{4}[/-]\d{2}\b"
    date_regex3 = r"\b\d{4}[/-]\d{2}[/-]\d{2}\b"

    # Combinar las expresiones regulares en una sola
    date_regex = f"({date_regex1}|{date_regex2}|{date_regex3})"
    # Buscar fechas en la URL
    match = re.search(date_regex, url)
    if match:
        return "SI"
    return "NO"
        
   
    
def tiene_kw(url,keyword):
      
    keyword = keyword.replace(" ", "-") # Si tiene más de una palabra, llevamos el 
                                        # keyword al formato que tiene en las urls
    keyword = keyword.replace("ñ", "n")  
    keyword = keyword.replace(".", "")
    keyword = quitar_acentos(keyword) 
    
    if keyword.lower() in url.lower():
        return "SI"
    else: 
        return "NO"
    
