# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:41:08 2022

@author: darwi
"""
from quitar_tildes import quitar_tildes
import dateutil.parser as dparser
import unicodedata
import re 
# funcion para quitar acentos de una frase/párrafo
def quitar_acentos(string):
    

    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    resultado = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', string).translate(trans_tab))

    return resultado

def kw_prim_p(soup,keyword):
    """
    ""
    
    Determina si el keyword aparece en el primer párrafo
    
    Nota: Cuidado con las páginas que usan la etiqueta "p" para 
    texto que no es párrafo. Para esto se toman en cuenta textos que no sean
    excesivamente cortos
    
    return (el keyword está subrayado en el 1er párrafo?) , (el keyword aparece en el 1er párrafo)

    """
    
    try:
         #prueba
    
        if  soup.body.h1.find_all_next("p", limit=4):  # Se extraen los 2 primeros párrafos luego de tag h1
            parrafos = soup.body.h1.find_all_next("p", limit=4)
            
            # en caso que no esté con acentos en el párrafo
            keyword_2 = quitar_tildes(keyword)
            #segundo_parrafo = soup.find("p").get_text().lower()
            
            
            # se recorren los parrafos  en búsqueda de aquellos demasiado cortos
            # que probablemente no tengan contenido como tal
            cont=0 # con esta vaariable establecemos dónde considerar el primer párrafo válido
            
            parrafo_sin_acentos = []
            for parrafo in parrafos:
                x = parrafo.get_text()
                x = quitar_acentos(x)
                parrafo_sin_acentos.append(x)
            
            
            for  parrafo in parrafos:
                 
               if len(parrafo.get_text()) < 40:
                   cont+=1
               else:
                   break
              
                
            # # Si hay una fecha y el parrafo es muy corto, revisa si está 
            # try:
            #         if  dparser.parse(parrafos[cont].get_text(), fuzzy=True) and len(parrafos[cont].get_text() < 50): # si hay una fecha
                       
            #             if ( keyword.lower() in parrafos[cont].get_text().lower()) or (keyword_2.lower() in parrafos[cont].get_text().lower() ): 
            #                      return "SI" 
                    
            #             else: 
            #                     return "NO"
                    
            # # de no ser así y arroja error al verificar fecha, analizar igual si la keyword está alli
            # except:
            #             if ( keyword.lower() in parrafos[cont].get_text().lower()) or (keyword_2.lower() in parrafos[cont].get_text().lower() ): 
            #                 return "SI"
                        
            #           #  elif ( keyword.lower() in parrafos[1].get_text().lower()) or (keyword_2.lower() in parrafos[1].get_text().lower() ): 
            #              #       return "SI"
                            
            #             else: 
            #                 return "NO"
            try:
                    if  dparser.parse(parrafo_sin_acentos[cont], fuzzy=True) and len(parrafo_sin_acentos[cont] < 50): # si hay una fecha
                       
                        if ( keyword.lower() in parrafo_sin_acentos[cont].lower()) or (keyword_2.lower() in parrafo_sin_acentos[cont].lower() ): 
                               
                           if (  soup.body.h1.find_all_next(["strong","b","span"],string=re.compile('^{0}$'.format(quitar_acentos(keyword)),flags=re.IGNORECASE), recursive=True) or soup.body.h1.find_all_next(["strong","b","span"],string=re.compile('^{0}$'.format(keyword),flags=re.IGNORECASE), recursive=True) ):      
                                          return "SI", "SI"
                           return "NO", "SI" 
                    
                        else: 
                                return "NO", "NO"
                    
            # de no ser así y arroja error al verificar fecha, analizar igual si la keyword está alli
            except:
                        if ( keyword.lower() in parrafo_sin_acentos[cont].lower()) or (keyword_2.lower() in parrafo_sin_acentos[cont].lower() ): 
                             if (  soup.body.h1.find_all_next(["strong","b","span"],string=re.compile('^{0}$'.format(quitar_acentos(keyword)),flags=re.IGNORECASE), recursive=True) or soup.body.h1.find_all_next(["strong","b","span"],string=re.compile('^{0}$'.format(keyword),flags=re.IGNORECASE), recursive=True) ):      
                                            return "SI", "SI"
                            
                             return "NO","SI"
                        
                      #  elif ( keyword.lower() in parrafos[1].get_text().lower()) or (keyword_2.lower() in parrafos[1].get_text().lower() ): 
                         #       return "SI"
                            
                        else: 
                            return "NO", "NO"
                            
                        
                        
                            
            
                            
           # elif soup.find("h2"): # modificado el if por elif
          #      parrafos = soup.find("h2")
              
                #segundo_parrafo = soup.find("p").get_text().lower()
             #   if keyword.lower() in parrafos.get_text().lower():
             #       return "SI"
             #   else:
             #       return "NO"
        
       
        else:
            return " ", " "
    

   #añadir validación para el caso particular de que no haya tag h1
    except:
        return  "NULL","H1 TAG NOT FOUND"
        

