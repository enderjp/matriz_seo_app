# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:35:32 2022

@author: ender

Extraer títulos y metadescripción
"""

# import requests
# import pandas as pd
# import urllib.request
# from urllib.parse import urlparse
# from bs4 import BeautifulSoup
from quitar_tildes import quitar_tildes

def title_seo_h1_diferentes(soup):
    
    if  soup.find("title") and  soup.find("h1") :
     
         title_seo  = soup.find("title").get_text().strip().lower()
         title_seo = quitar_tildes(title_seo)
         
         title_h1 = soup.find("h1").get_text().strip().lower()
         title_h1 = quitar_tildes(title_h1)
         
         if title_seo.startswith(title_h1):
             return "NO"
         else:
             return "SI"
    
    else:
        return "NULL"

def get_title_seo(soup,keyword):
    """Return the page title

    Args:
        soup: HTML code from Beautiful Soup
        
    Returns: 
        value (string): Parsed value
    """

    if soup.findAll("title"):
        title_seo = soup.find("title").get_text().strip()
        # Chequear longitud
        if len(title_seo) > 70:
            len_title_seo = "No"
        else:
            len_title_seo = "SI"
            
        # Chequear si contiene el keyword
        if keyword.lower() in title_seo.lower():
            have_kw =  "SI"
        else:
            have_kw =  "NO"
            
        return len_title_seo, have_kw
        
    else:
        return "Titulo SEO no encontrado", "Nulo"

    
def get_title_h1(soup,keyword):
    """Return the page title

    Args:
        soup: HTML code from Beautiful Soup
        
    Returns: 
        value (string): Parsed value
    """

    if soup.findAll("h1"):
        title_h1 = soup.find("h1").get_text().strip()
        
        # chequear si contiene el keyword al inicio
        if title_h1.lower().startswith(keyword.lower()):
            starts_with_kw = "SI"
            
       
        elif  keyword.lower() in title_h1.lower() :  
            
                    # indice del comienzo de la keyword
                 if len(title_h1.lower()[0:title_h1.lower().index(keyword.lower())]) <= 14:
                    starts_with_kw = "SI"
                 else:
                     starts_with_kw = "NO"
           
        else:
            starts_with_kw = "NO"
        
        if len(title_h1) <= 70:
            len_title_seo = "SI"
        else:
            len_title_seo = "NO"
        return title_h1, len_title_seo, starts_with_kw
    else:
        return "NOT FOUND","Nulo", "Nulo"
   
    
def get_description(soup, keyword):
    
    """
    Función para obtener la meta descripción de la url
    
    también determina si en dicha descripción aparece el keyword
    
    """
    if soup.findAll("meta", attrs={"name": "description"}):
        description = soup.find("meta", attrs={"name": "description"}).get("content")
        
        if len(description) >= 156:
            len_description= "NO"
        else:
            len_description = "SI"
       
        if keyword.lower() in description.lower():
            have_kw =  "SI"
        else:
            have_kw =  "NO"
        return len_description, have_kw
    
    else:
        return "NOT FOUND", "NULO"

    






