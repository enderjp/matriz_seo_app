# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:49:45 2022

@author:  Ender

Detectar si el keyword está en negrita

"""

import re 
from quitar_tildes import quitar_tildes
import unicodedata

def quitar_acentos(string):
    

    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    resultado = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', string).translate(trans_tab))

    return resultado

def keyword_sub(soup,keyword):
    """
    ""

    Cuenta el número de veces que aparece el keyword en los párrafos de la página,
    y el número de veces que aparece junto con la etiqueta "strong",
    luego compara si ambos números son iguales para determinar 
    que no hay ninguna sin resaltar en negrita.
    
    Se asume que si no están todos en negrita, la respuesta es NO

    """
    # if soup.find_all(string=[keyword,keyword.lower(),
    #                          keyword.capitalize(),
    #                          keyword + " ", 
    #                          " " + keyword]) or soup.find_all(["p","span"],string=re.compile('.*{0}.*'.format(keyword.lower())), recursive=True):# sí consigue el kw
        
    
    
    # se considera la kw dentro de etiquetas p, strong y b
    if soup.find_all(["p","strong","b","span"],string=re.compile('^{0}$'.format(keyword),flags=re.IGNORECASE), recursive=True):
   
        
        
    
   
        # Todas las keyword dentro de una etiqueta 
        
        num_kw =  soup.find_all(["p","strong","b"],string=re.compile('^{0}$'.format(keyword),flags=re.IGNORECASE), recursive=True)
        
        
        # todas las keyword en general (solo la keyword)
        # num_kw = soup.find_all(string=[keyword,keyword.lower(),
        #                                keyword.capitalize(),
        #                                keyword + " ",
        #                                " " + keyword])
        
        kw_strong = soup.find_all(["strong"],string=re.compile('^{0}$'.format(keyword),flags=re.IGNORECASE), recursive=True)

        
        
        # kw_bold = soup.find_all("span",attrs={"style": "display: initial; font-weight: bold;"},
        #                 string=[keyword,keyword.lower(),
        #                         keyword.capitalize(),
        #                         keyword + " ", " " + keyword])
        
        kw_bold = soup.find_all(["span"],string=re.compile('^{0}$'.format(keyword),flags=re.IGNORECASE), recursive=True)

    
        
        kw_b = soup.find_all(["b"],string=re.compile('^{0}$'.format(keyword),flags=re.IGNORECASE), recursive=True)

        # no considerar acentos en los artículos
        
        



        #print(num_kw,"  ", kw_strong)
        if    len(num_kw) - len(kw_strong) <= 1 or len(num_kw) - len(kw_bold) <= 1  or len(num_kw) - len(kw_b) <= 1:
            return "SI"
        else:
            return "NO"
        
       
        
    else:
        return " "
    

# keyword = "casa"
# c = soup.find_all(text= keyword)
# u = soup.find_all(string=keyword)
# t = soup.find_all(["strong"],string=keyword)


# # # keyword = "impacto visual"
# num_kw = soup.find_all(string=[keyword,keyword.lower(),keyword.capitalize()])
# kw_strong = soup.find_all("strong", string=[keyword,keyword.lower(),keyword.capitalize()])

# soup.find_all("p",string=re.compile('.*{0}.*'.format(keyword)), recursive=True)


# keyword = "comunicación visual"

# soup.find_all(string=[keyword,keyword.lower(),
#                                keyword.capitalize(),
#                                keyword + " ",
#                                " " + keyword])



