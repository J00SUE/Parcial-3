from clases import Paciente
from clases import Imagenes
import matplotlib.pyplot as plt
import cv2

D = Paciente()
P = 0
img=Imagenes()
paciente = {}
dicom = {}
PNG = {}
while True:
    
    
    rutan = r"C:\Users\dario\Desktop\p3\Parcial-3\Sarcoma\img2"
    Menu = input("""
            a. Ingresar paciente
            b. Ingreso imagenes
            c. Rotacion
            d. binarizacion
            e. Salir
                 """)
    
    if Menu == "a":
        #ruta = input("Ruta de Dicom: ")
        ruta=r"C:\Users\dario\Parcial-3-4\Sarcoma\img1"
        key="1456"
        A = D.Imagen(ruta,key)
        N = D.Nombre(key)
        I = D.Id(key)
        E = D.Age(key)
        p = D.Estudio(key)
        k = D.Sex(key)
        z = D.retornar_imagen(key)
        #s = D.Nifti(ruta,rutan)
        #'Nifti' : s
        paciente[I] = {'Nombre': N,'Edad': E,'Estudio': p,'Genero': k,'Imagen' : z}
        plt.imshow(z)
        plt.axis('off')
        plt.show()
        dicom[key]=A
        PNG[key]=z

    elif Menu == "b":
        ruta=r"C:\Users\dario\Parcial-3-4\celula.jpg"
        key="987"
        #key = input("Ingresa key: ")
        #ruta = input("Ruta de imagen: ")
        A = img.leer_imagen(key,ruta)
        PNG[key] = {'Imagen': A}
        
    elif Menu == "c":
        #ruta=input("ingrese la ruta de la imagen")
        #key=input("ingrese la clave del paciente")
        ruta=r"C:\Users\dario\Parcial-3-4\celula.jpg"
        
        key="123"
        angulo=input("""ingrese el angulo al que quiere rotar
                     1. 90 grados
                     2. 180 grados
                     3. 270 grados
                     """)
        img.leer_imagen(key,ruta)
        rotada=img.rotar_imagen(key,angulo)
        orginal=img.obtener_imagen(key)
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].imshow(orginal, cmap="bone")
        axs[0].set_title('Imagen Original')
        axs[0].axis('off')
        axs[1].imshow(rotada, cmap='bone')
        axs[1].set_title('Imagen Rotada')
        axs[1].axis('off')
        plt.tight_layout()
        plt.show()
        PNG[key]= rotada

    elif Menu == "d":
        ruta=r"C:\Users\dario\Parcial-3-4\Imagen celula.jpg"
        key = input("Ingresa key: ")
        Umbral = int(input("Umbral: "))
        Kernel = int(input("Kernel a usar: "))
        A = img.leer_imagen(key,ruta)
        B = img.binarizar_imagen(key,Umbral,Kernel)
        plt.imshow(B)
        plt.axis('off')
        plt.show()
        PNG[key]=B
            
    elif Menu == "e":
        break