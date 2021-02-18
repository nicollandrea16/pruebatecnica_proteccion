#Procesador_imagenes
import os
from os.path import isfile, join
import fnmatch
import cv2 as cv
from tkinter import *
from tkinter import filedialog
import sys


def abrirArchivo():
    eleccion= input("Desea seleccionar archivos (s) o trabajar con todas las imágenes de una carpeta (c): ")
    if eleccion=="s":
        img_in= filedialog.askopenfilename(title="Abrir archivos" , filetypes=(("Imagenes jpg", "*.jpg"),("Todos los archivos","*.*")), multiple=True)
    else:
        directory= filedialog.askdirectory(title="Seleccionar carpeta")
        archivos= fnmatch.filter(os.listdir(directory), "*.jpg")
        img_in= []
        for i in archivos: 
            img_in.append(join(directory, i))
    return img_in   


#---Obtener archivo----------------------------------------------------------------------------------------------
path=abrirArchivo()

for i in path :
    img_in = cv.imread(i)

    if img_in is None:
        sys.exit("Could not read the image.")

    #---Mostrar archivo original-------------------------------------------------------------------------------------
    '''cv.imshow("Imagen original", img_in)
    k = cv.waitKey(delay=3000)
    cv.destroyAllWindows()'''

    #---Obtener dimensiones de la imagen-----------------------------------------------------------------------------
    height, width = img_in.shape[:2]

    #---Procesamiento de la imagen-------------------------------------------------------------------------------------------------------------
    if height>width or height==width:
        orientacion = "La imagen es Vertical"
        ratio = width/height
        if int(ratio)==1:
            orientacion = "La imagen es Cuadrada"
        
        if height>1123 or width>796:
            prueba_width=1123*ratio
            prueba_height=796*ratio
            if prueba_width>796:
                new_height=int(round(796/ratio))
                new_width=796
            else:
                new_height=1123
                new_width=int(round(prueba_width))
        else: 
            new_height=height
            new_width=width
    #----------------------------------------------------------------------------------------
    elif height<width:
        ratio = height/width
        orientacion = "La imagen es Horizontal"
        if height>796 or width>1123:
            prueba_width=796*ratio
            prueba_height=1123*ratio
            if prueba_height>796:
                new_height=796
                new_width=int(round(1123/ratio))
            else:
                new_height=int(round(prueba_height))
                new_width=1123
        else: 
            new_height=height
            new_width=width

    #- Impresión de resultados----------------------------------------------------------------------------------------------

    print(orientacion)
    print("- Altura original: ", height, " pixeles")
    print("- Ancho original: ", width, "pixeles")
    print("- Altura modificada: ", new_height, " pixeles")
    print("- Ancho modificado: ", new_width, " pixeles")

    #--Mostrar imagen modificada--------------------------------------------------------------------------------------------
    img_out = cv.resize(img_in,(new_width,new_height))
    '''cv.imshow("Imagen modificada", img_out)
    k = cv.waitKey(delay=4000)
    cv.destroyAllWindows()'''

