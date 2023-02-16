# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:10:31 2023

@author: darwi
"""

from bs4 import BeautifulSoup, NavigableString, Tag

def palabra_no_resaltada(parrafo,keyword):
    """
    

    Parameters
    ----------
    parrafo : TYPE
    Funcion para determinar si una keyword esta resaltada en el parrafo,
    si se diferencia visualmente del resto del texto

    Returns
    -------
    bool
        DESCRIPTION.

    """

    
    kw_inside_tags = False
    
    for child in parrafo:
        
            if  keyword in str(child) and child.name in ['b', 'span', 'i', 'em', 'strong', 'u', 'a']:

                kw_inside_tags = True
                
              # return True
                print("Entro una palabra de toda la kw resaltada")
        
    if kw_inside_tags == False:
              return False
          
    else:
        return True
            
        
   

            
        
        