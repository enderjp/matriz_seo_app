# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:05:50 2022

@author: darwi
"""

# Funcion para quitar tildes de las vocales
def quitar_tildes(keyword):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        keyword = keyword.replace(a, b).replace(a.upper(), b.upper())
    return keyword