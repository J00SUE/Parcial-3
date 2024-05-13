import numpy as np 
import pydicom
import matplotlib.pyplot as plt
import os
import dicom2nifti
import nilearn
from nilearn import plotting
     
class Dicom():
    def Imagen(self, path):
        Imagen_list = []
        for archivo in os.listdir(path):
            if archivo.endswith('.dcm'):
                Imagen_list.append(pydicom.dcmread(os.path.join(path, archivo)))
        Imagen_list.sort(key = lambda x: int(x.ImagePositionPatient[2]))
        return Imagen_list

    def Nombre(self, Lista,i):
        Nombre = Lista[i].PatientName
        return Nombre

    def Age(self, Lista,i):
        Edad = Lista[i].PatientAge
        return Edad

    def Id(self, Lista,i):
        Id = Lista[i].PatientID
        return Id
    
    def Sex(self, Lista,i):
        Sex = Lista[i].PatientSex
        return Sex

    def Estudio(self, Lista,i):
        Estudio = Lista[i].StudyDescription
        return Estudio
    
    def Im(self, Lista,i):
        Im = Lista[i]
        return Im
    
    def Nifti(self, ruta, rutan):
        dicom2nifti.convert_directory(ruta,rutan)
        img1 = nilearn.image.load_img(rutan)
        plotting.plot_anat(img1[0])
    
D = Dicom()
ruta = r"C:\Users\Chimuelo\OneDrive\Escritorio\Parcial 3\Sarcoma\img1"
A = D.Imagen(ruta)
N = D.Nombre(A,0)
print('Nombre: {}' .format(N))
I = D.Id(A,0)
print('Id: {}' .format(I))
E = D.Age(A,0)
print('Edad: {}' .format(E))
p = D.Estudio(A,0)
print('Estudio: {}' .format(p))
k = D.Sex(A,0)
print('Genero: {}' .format(k))
z = D.Im(A,0)
rutan = r"C:\Users\Chimuelo\OneDrive\Escritorio\Parcial 3\nifti"
s = D.Nifti(ruta,rutan)





