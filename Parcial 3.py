import numpy as np 
import pydicom
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import dicom2nifti
#import nilearn
#from nilearn import plotting
     
class Dicom():
    def __init__(self) -> None:
        self.dicomlist=[]
    def Imagen(self, path):

        for archivo in os.listdir(path):
            if archivo.endswith('.dcm'):
                self.dicomlist.append(pydicom.dcmread(os.path.join(path, archivo)))
                self.dicomlist.sort(key = lambda x: int(x.ImagePositionPatient[2]))
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
        z= self.dicomlist[i]
        img=z.pixel_array
        return img
class Imagenes:
    def __init__(self):
        self.imagenesorg = {}
        self.imagenesrto = {}
        self.imagenesbin = {}
        self.umbral = 128  
        self.tamano_kernel = 3

    def leer_imagen(self, key, iman):
        imn=[]
        for i in range (len(iman)):
            imagen = iman[i].pixel_array
            img = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
            imn.append(img)
        if imn is not None:
            self.imagenesorg[key] = img
            print("Imagen leída correctamente.")
        else:
            print("No se pudo leer la imagen desde la ruta especificada.")
    def obtener_imagen(self, key,i):
        if key in self.imagenesorg:
            return self.imagenesorg[key][i]
        else:
            print("No se encontró la imagen especificada en el diccionario.")
            return None

    def rotar_imagen(self, key, angulo,i):
        if key in self.imagenes:
            if angulo == 1:
                imagen_rotada = cv2.rotate(self.imagenesorc[key][i], cv2.ROTATE_90_CLOCKWISE)
            elif angulo == 2:
                imagen_rotada = cv2.rotate(self.imagenesorc[key][i], cv2.ROTATE_180)
            elif angulo == 3:
                imagen_rotada = cv2.rotate(self.imagenesorc[key][i], cv2.ROTATE_90_COUNTERCLOCKWISE)
            else:
                print("El ángulo especificado no es válido.")
                return None
                
            self.imagenesrto[key] = imagen_rotada
            print("Imagen rotada correctamente.")
            return imagen_rotada
        else:
            print("No se encontró la imagen especificada en el diccionario.")
            return None

    def binarizar_imagen(self, key,i, umbral=None ,  tamano_kernel=None):
        if tamano_kernel is not None:
            self.tamano_kernel = tamano_kernel
        if umbral is not None:
            self.umbral = umbral

        if key in self.imagenes:
            imagen_gris = cv2.cvtColor(self.imagenesorc[key][i], cv2.COLOR_BGR2GRAY)
            _, imagen_binarizada = cv2.threshold(imagen_gris, self.umbral, 255, cv2.THRESH_BINARY)
            kernel = np.ones((self.tamano_kernel, self.tamano_kernel), np.uint8)
            imagen_morfologica = cv2.morphologyEx(imagen_binarizada, cv2.MORPH_OPEN, kernel)
            info = f"Imagen binarizada (Umbral: {self.umbral},  kernel: {self.tamano_kernel})"
            cv2.putText(imagen_morfologica, info, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            self.imagenesbin[key] = imagen_morfologica
            print("Imagen binarizada y transformación morfológica aplicadas correctamente.")
            return imagen_morfologica
            
        else:
            print("No se encontró la imagen especificada en el diccionario.")

    
D = Dicom()
imagenes_obj = Imagenes()
key="123"

ruta = r"C:\Users\dario\Parcial-3\Sarcoma\img1"
A = D.Imagen(ruta)
img=A[0].pixel_array
print(img)
imagenes_obj.leer_imagen(key, A)
img=imagenes_obj.obtener_imagen(key)
N = D.Nombre(0)
print('Nombre: {}' .format(N))
E = D.Age(0)
print('Edad: {}' .format(E))
p = D.Estudio(0)
print('Estudio: {}' .format(p))
k = D.Sex(0)
print('Genero: {}' .format(k))
for i in range (len(A)):
    img=imagenes_obj.obtener_imagen(key,i)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
#for i in range (len(A)):
    #img=D.retornar_imagen(i)
    #plt.imshow(img)
    #plt.axis('off')
    #plt.show()


