# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import titulos_metadescripcion as inf_seo
import keyword_neg 
import keyword_primer_parrafo as kw_primer_p
import url_tam_fecha as url
import obtener_fecha_publicacion as fecha_public
from titulos_metadescripcion import title_seo_h1_diferentes
#from titulos_metadescripcion import *


# Leer archivo excel con URLs y keywords
file = pd.read_excel('urls_movistar.xlsx')  


matriz_seo = pd.DataFrame( columns=['Titulo',
                                    'Categoría',
                                    'Mes producido',
                                         '¿Ya esta publicado?',
                                         'Fecha de publicacion',
                                         'Keyword',
                                         'URL',
                                         '¿El titulo SEO es de máximo 70 caracteres?',
                                         'El titulo SEO tiene el keyword',
                                         '¿La metadescripción es inferior a 156 caracteres?',
                                         '¿Aparece el keyword en la metadescripción?',
                                         '¿Aparece el keyword al inicio en el título H1?',
                                         '¿Titulo H1 inferior a 70 caracteres?',
                                         'El 25% de las oraciones sobrepasan las 20 palabras',
                                         'Está subrayado el keyword',
                                         'El keyword está en el primer párrafo',
                                         'Densidad del keyword cercana al 2%',
                                         'Contiene algún link interno',
                                         'Contiene links externos',
                                         '¿Cuándo se da clic envía a otra ventana?',
                                         '¿La URL es inferior a 100 caracteres?',
                                         'La URL no tiene fecha de publicación',
                                         'Tiene el keyword en la URL'
                                         #'¿Título SEO y H1 diferentes?' # añadido
                                         ])

 

print("Obteniendo datos de las URLs...")
print("\n")


# lista para llevar un control de los comentarios de titulo H1 y SEO iguales
titles_h1_seo_same =[]
   

for i in range(len(file)):
    
    # Se obtiene parte del contenido de la URL
    
    # usar un try y except para manejar el error de SSL certificate
    page = requests.get(file.loc[i][0],headers= {'User-Agent': 'Mozilla/5.0'},verify=False)
    

    soup = BeautifulSoup(page.content, 'html.parser')
    keyword = file.loc[i][1].strip()
    len_title_seo, have_kw_title_seo = inf_seo.get_title_seo(soup, keyword)
    len_description, have_kw_meta = inf_seo.get_description(soup, keyword)
    title_h1,len_title_h1, starts_with_kw= inf_seo.get_title_h1(soup, keyword)
    
    #se añade a la lista un SI o NO, dependiendo si el titulo H1 Y seo son iguales
    titles_h1_seo_same.append(title_seo_h1_diferentes(soup))
   
    
    matriz_seo.loc[i] = [title_h1 ,  
                         ' ',
                        ' ',
                        'SI',
                        fecha_public.get_date(file.loc[i][0], soup),
                        keyword,
                        file.loc[i][0],
                        len_title_seo,
                        have_kw_title_seo,
                        len_description,
                        have_kw_meta,
                        starts_with_kw,
                        len_title_h1,
                        'SI',
                        keyword_neg.keyword_sub(soup, keyword),
                        kw_primer_p.kw_prim_p(soup, keyword),
                        'SI',
                        ' ',
                        ' ',
                        ' ',
                        url.url_tam(file.loc[i][0], keyword),
                        url.contiene_fecha(file.loc[i][0]),
                        url.tiene_kw(file.loc[i][0], keyword)
                     ]
                        
 
    
    print("URLS PROCESADAS: ",i+1)
    print("keyword :", keyword)
     
#matriz_seo.to_excel("output.xlsx")  


#writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("MATRIZ SEO.xlsx", engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
matriz_seo.to_excel(writer, sheet_name='MATRIZ DE SEO', index=False)

# Write data to an excel

# Get workbook
workbook = writer.book

# Get Sheet1
worksheet = writer.sheets['MATRIZ DE SEO']

cell_format = workbook.add_format()
cell_format.set_font_name('Century Gothic')
cell_format.set_font_size(11)
cell_format.set_border()
worksheet.set_column('A:Z', None, cell_format)

for i in range(len(file)):
    if titles_h1_seo_same[i] == 'NO':
      #  worksheet.write('A1', 'Hello')
        worksheet.write_comment('M%s'%(i+2), 'Título H1 duplicado')

    
    
   

writer.close()
    
