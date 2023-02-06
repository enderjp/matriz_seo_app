# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:40:35 2023

@author: darwi
"""
from bs4 import BeautifulSoup

def texto_no_resaltado(parrafo):
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

    
    all_children_highlighted = True
    all_children_have_same_tag = True
    tag = None
    attrs = None
    for child in parrafo:
        if child.name not in ['b', 'span', 'i', 'em', 'strong']:
            all_children_highlighted = False
            return True
        
        if tag is None:
            tag = child.name
            attrs = child.attrs
        else:
            if child.name != tag and child.attrs != attrs:
                all_children_have_same_tag = False
                return True
    print("Entro a keyword resaltada")
    return False
    
            
        
        
        
        
        
        