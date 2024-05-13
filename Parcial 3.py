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
        rut = input("Ruta archivo nifti: ")
        a = input("Tiempo de espera") 
        img = nilearn.image.load_img(rut)
        plotting.plot_anat(img)
        plt.show()
    
D = Dicom()
ruta = input("Ruta de Dicom: ")
A = D.Imagen(ruta)
P = int(input("Paciente: "))
N = D.Nombre(A,P)
print('Nombre: {}' .format(N))
I = D.Id(A,P)
print('Id: {}' .format(I))
E = D.Age(A,P)
print('Edad: {}' .format(E))
p = D.Estudio(A,P)
print('Estudio: {}' .format(p))
k = D.Sex(A,P)
print('Genero: {}' .format(k))
z = D.Im(A,P)
rutan = r"C:\Users\Chimuelo\OneDrive\Escritorio\Parcial 3\nifti"
s = D.Nifti(ruta,rutan)

paciente = {}
paciente[I] = {
    'Nombre': N,
    'Edad': E,
    'Estudio': p,
    'Genero': k,
    'Imagen' : z,
    'Nifti' : s
}







