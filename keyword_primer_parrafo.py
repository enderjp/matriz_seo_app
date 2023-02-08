# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:41:08 2022

@author: darwi
"""
import streamlit as st
from quitar_acentos import quitar_acentos
import dateutil.parser as dparser
import unicodedata
import re 
from keyword_resaltada import texto_no_resaltado
# funcion para quitar acentos de una frase/párrafo

# def quitar_acentos(string):
    

#     trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
#     resultado = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', string).translate(trans_tab))

#     return resultado

def keyword_primer_parrafo(soup,keyword):
    """
    ""
    
    Determina si el keyword aparece en el primer párrafo
    
    Nota: Cuidado con las páginas que usan la etiqueta "p" para 
    texto que no es párrafo. Para esto se toman en cuenta textos que no sean
    excesivamente cortos
    
    return (el keyword está subrayado en el 1er párrafo?) , (el keyword aparece en el 1er párrafo),
             (Se da el caso especial donde hay más texto subrayado junto al kw?)

    """
    
    try:
         
    
        if  soup.body.h1.find_all_next("p", limit=4):  # Se extraen los 2 primeros párrafos luego de tag h1
            parrafos = soup.body.h1.find_all_next("p", limit=15)
        
            keyword_sin_acentos = quitar_acentos(keyword)
            #segundo_parrafo = soup.find("p").get_text().lower()
            
            # se recorren los parrafos  en búsqueda de aquellos demasiado cortos
            # que probablemente no tengan contenido como tal
            cont=0 # con esta variable establecemos dónde considerar el primer párrafo válido
            
           # parrafo_sin_acentos = []
            # for parrafo in parrafos:
            #     x = parrafo.get_text().lower()
            #     x = quitar_acentos(x)
            #     parrafo_sin_acentos.append(x)
            
            for  parrafo in parrafos:
               string = " ".join(parrafo.get_text().split() ) #quitamos espacios adicionales
               if len(string) < 60:
                   cont+=1
                   print(parrafo.get_text(), " ", len(parrafo.get_text()))
               else:
                   break
            

            parrafo_sin_acentos = parrafos[cont].get_text().lower() 
            parrafo_sin_acentos = quitar_acentos(parrafo_sin_acentos)
            
           # eliminar espacios adicionales entre las palabras
            parrafo_sin_acentos = " ".join( parrafo_sin_acentos.split() ) 
           
           # hacer lo mismo a la string con codigo html para hacer operaciones
            primer_parrafo = " ".join( quitar_acentos(str(parrafos[cont])).lower().split() )
            
                           
            try:         # # Si hay una fecha y el parrafo es muy corto, revisa si está 
                    if  dparser.parse(parrafo_sin_acentos, fuzzy=True) and len(parrafo_sin_acentos < 60): # si hay una fecha
                        if (keyword_sin_acentos in parrafo_sin_acentos ): 
                              
                          # expresión regular para determinar si en el primer párrafo está la keyword subrayada
                          # se  consideran las etiquetas strong, b, span, u, i, y em-strong
                            match = re.search(r"(<(strong|b|span|em|u|i|a).*>.?" + keyword_sin_acentos + "[.,]?.?</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + keyword_sin_acentos + "[.,]?.*?</strong>.*?</em>)",primer_parrafo)

                            if (match):
                              return "SI", "SI", False
                          
                            elif (not match):
                               
                                # RE ahora considerando texto adicional junto a la kw
                                match2 = re.search(r"(<(strong|b|span|em|u|i|a).*>.*" + keyword_sin_acentos + "[.,]?.*</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + keyword_sin_acentos + "[.,]?.*?</strong>.*?</em>)",primer_parrafo)
                                
                                if (match2):
                                       # si hay mas 1 hijo  en la etiqueta p
                                       keyword_resaltada = texto_no_resaltado(parrafos[cont].contents)
                                       if keyword_resaltada:
                                           
                                           return "SI", "SI", True
                                       else:
                                           return "NO", "SI", False
                                    
                                elif (not match2):
                                    
                                      # si la kw tiene mas de 1 palabra
                                      if (len(keyword_sin_acentos.split()) > 1):
                                          contador_keyword = 0
                                          palabras_keyword = keyword_sin_acentos.split()
                                         
                                          for palabra in palabras_keyword:
                                              match = re.search(r"(<(strong|b|span|em|u|i|a).*>.*" + palabra + "[.,]?.*</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + palabra + "[.,]?.*?</strong>.*?</em>)",primer_parrafo)
                                              if (match):
                                                  contador_keyword+=1
                                                

                                          if (contador_keyword == len(palabras_keyword)):
                                              return "SI", "SI", False
                                          
                                          else:
                                              return "NO", "SI", False
                                    
                                          
                                      else:
                                         return "NO", "SI", False
                                
                          
                            else:
                               
                               return "NO", "SI" , False
                    
                        else: 
                                return "NO", "NO", False
                    
            # de no ser así y arroja error al verificar fecha, analizar igual si la keyword está alli
            except:
                       
                        if ( keyword_sin_acentos in parrafo_sin_acentos ): 
                             match = re.search(r"(<(strong|b|span|em|u|i).*>.?" + keyword_sin_acentos + "[.,]?.?</(strong|b|span|em|u|i)>)|(<em>.*?<strong>.*?" + keyword_sin_acentos + "[.,]?.*?</strong>.*?</em>)",primer_parrafo)
                             
                             if (match):
                                  return "SI", "SI", False
                              
                             elif (not match):
                                    
                                match2 = re.search(r"(<(strong|b|span|em|u|i|a).*>.*" + keyword_sin_acentos + "[.,]?.*</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + keyword_sin_acentos + "[.,]?.*?</strong>.*?</em>)",primer_parrafo)
                                
                                if (match2):
                                          # si hay mas 1 hijo  en la etiqueta p
                                            keyword_resaltada = texto_no_resaltado(parrafos[cont].contents)
                                            if keyword_resaltada:
                                                
                                                return "SI", "SI", True
                                            else:
                                                return "NO", "SI", False
                                       
                                elif (not match2):
                                    # si la kw tiene mas de 1 palabra
                                      if (len(keyword_sin_acentos.split()) > 1):
                                          contador_keyword = 0
                                          palabras_keyword = keyword_sin_acentos.split()
                                         
                                          for palabra in palabras_keyword:
                                              match = re.search(r"(<(strong|b|span|em|u|i|a).*>.*" + palabra + "[.,]?.*</(strong|b|span|em|u|i|a)>)|(<em>.*?<strong>.*?" + palabra + "[.,]?.*?</strong>.*?</em>)",primer_parrafo)
                                              if (match):
                                                  contador_keyword+=1
                                               

                                          if (contador_keyword == len(palabras_keyword)):
                                              return "SI", "SI", False
                                          
                                          else:
                                              return "NO", "SI", False
                                    
                                    
                                      else:
                                         return "NO", "SI", False   
                                     
                                    
                             else:
                               
                               return "NO", "SI" , False
                        
                    
                        else: 
                            return "NO", "NO", False
                            
                        
                  
       
        else:
            return " ", " ", False
    

    #añadir validación para el caso particular de que no haya tag h1
    except:
        return  "NULL","ERROR ", False
        

