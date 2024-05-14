import numpy as np 
import pydicom
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import dicom2nifti
import nilearn
from nilearn import plotting
     
class Paciente():
    def __init__(self):
        self.dicomlist= {}

    def Imagen(self, path, key):
        for archivo in os.listdir(path):
            if archivo.endswith('.dcm'):
                j=pydicom.dcmread(os.path.join(path, archivo))
                self.dicomlist[key]=j
        return self.dicomlist

    def Nombre(self,i):
        Nombre = self.dicomlist[i].PatientName
        return Nombre

    def Age(self,i):
        Edad = self.dicomlist[i].PatientAge
        return Edad

    def Id(self,i):
        Id = self.dicomlist[i].PatientID
        return Id
    
    def Sex(self,i):
        Sex = self.dicomlist[i].PatientSex
        return Sex

    def Estudio(self,i):
        Estudio = self.dicomlist[i].StudyDescription
        return Estudio
    
    def retornar_imagen(self,i):
        z = self.dicomlist[i]
        img = z.pixel_array
        return img
    
    def Nifti(self, ruta, rutan):
        dicom2nifti.convert_directory(ruta,rutan)
        rut = input("Ruta archivo nifti: ")
        a = input("Tiempo de espera") 
        img = nilearn.image.load_img(rut)
        plotting.plot_anat(img)
        plt.show()
        return img
    
class Imagenes:
    def __init__(self):
        self.imagenesorg = {}
        self.imagenesrto = {}
        self.imagenesbin = {}
        self.umbral = 128  
        self.tamano_kernel = 3

    def leer_imagen(self, key, ruta):
        imn=[]

        imagen = cv2.imread(ruta)
        img = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        imn.append(img)
        if imn is not None:
            self.imagenesorg[key] = imn
            print("Imagen leída correctamente.")
        else:
            print("No se pudo leer la imagen desde la ruta especificada.")
    def obtener_imagen(self, key):
        if key in self.imagenesorg:
            return self.imagenesorg[key][0]
        else:
            print("No se encontró la imagen especificada en el diccionario.")
            return None

    def rotar_imagen(self, key=None, angulo="1"):
        if key in self.imagenesorg:
            imn=self.imagenesorg[key][0]
            if angulo == "1":
                imagen_rotada = cv2.rotate(imn, cv2.ROTATE_90_CLOCKWISE)
            elif angulo == "2":
                imagen_rotada = cv2.rotate(imn, cv2.ROTATE_180)
            elif angulo == "3":
                imagen_rotada = cv2.rotate(imn, cv2.ROTATE_90_COUNTERCLOCKWISE)
            else:
                print("El ángulo especificado no es válido.")
                return None
                
            self.imagenesrto[key] = imagen_rotada
            print("Imagen rotada correctamente.")
            return imagen_rotada
        else:
            print("No se encontró la imagen especificada en el diccionario.")
            return None

    def binarizar_imagen(self, key, umbral=None ,  tamano_kernel=None):
        if tamano_kernel is not None:
            self.tamano_kernel = int(tamano_kernel)
        if umbral is not None:
            self.umbral = umbral

        if key in self.imagenesorg:
            imn=self.imagenesorg[key][0]
            imagen_gris = cv2.cvtColor(imn, cv2.COLOR_BGR2GRAY)
            imagen_binarizada = cv2.threshold(imagen_gris, self.umbral, 255, cv2.THRESH_BINARY)
            kernel = np.ones((self.tamano_kernel, self.tamano_kernel), np.uint8)

            imagen_morfologica = cv2.morphologyEx(imagen_binarizada[1], cv2.MORPH_OPEN, kernel)
            info = f"Imagen binarizada (Umbral: {self.umbral},  kernel: {self.tamano_kernel})"
            cv2.putText(imagen_morfologica, info, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            self.imagenesbin[key] = imagen_morfologica
            print("Imagen binarizada y transformación morfológica aplicadas correctamente.")
            return imagen_morfologica
            
        else:
            print("No se encontró la imagen especificada en el diccionario.")
    


