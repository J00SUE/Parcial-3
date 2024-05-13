import numpy as np 
import pydicom
import matplotlib.pyplot as plt
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

    
D = Dicom()
ruta = r"C:\Users\dario\Parcial-3\Sarcoma\img1"
A = D.Imagen(ruta)
N = D.Nombre(0)
print('Nombre: {}' .format(N))
E = D.Age(0)
print('Edad: {}' .format(E))
p = D.Estudio(0)
print('Estudio: {}' .format(p))
k = D.Sex(0)
print('Genero: {}' .format(k))
for i in range (len(A)):
    img=D.retornar_imagen(i)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


