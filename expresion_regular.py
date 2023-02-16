# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:40:01 2023

@author: darwi
"""
import re

def match_keyword(keyword,parrafo):
    
    match = re.search(r"(<(strong|b|span|em|u|i|a).*>.?" + keyword + "[.,]?.?</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + keyword + "[.,]?.*?</strong>.*?</em>)",parrafo)

    if match:
       return True
    else:
       return False