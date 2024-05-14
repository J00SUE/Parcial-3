from clases import Paciente
from clases import Imagenes
import matplotlib.pyplot as plt
import cv2

D = Paciente()
P = 0
img=Imagenes()
D = Paciente()
P = 0
img=Imagenes()
while True:
    paciente = {}
    dicom = {}
    PNG = {}
    
    rutan = r"C:\Users\dario\Desktop\p3\Parcial-3\Sarcoma\img2"
    Menu = input("""
            a. Ingresar paciente
            b. Ingreso imagenes
            c. Rotacion
            d. Manipulacion imagen
            e. Salir
                 """)
    
    if Menu == "a":
        ruta = input("Ruta de Dicom: ")
        A = D.Imagen(ruta)
        N = D.Nombre(P)
        I = D.Id(P)
        E = D.Age(P)
        p = D.Estudio(P)
        k = D.Sex(P)
        z = D.retornar_imagen(P)
        s = D.Nifti(ruta,rutan)

        paciente[I] = {'Nombre': N,'Edad': E,'Estudio': p,'Genero': k,'Imagen' : z,'Nifti' : s}

    elif Menu == "b":
        key = input("Ingresa key: ")
        Im = input("Ruta de imagen: ")
        A = img.leer_imagen(key,Im)
        PNG[key] = {'Imagen': A}
        
    elif Menu == "c":
        key=input("ingrese la clave del paciente")
        angulo=input("""ingrese el angulo al que quiere rotar
                     1. 90 grados
                     2. 180 grados
                     3. 270 grados
                     """)
        infopac=D.Imagen(ruta)
        print(f"su paciente tiene {len()} cortes")
        corte=int(input("ingrese el corte que quiere rotar"))
        rotada=Imagenes.rotar_imagen(key,angulo,corte)
        orginal=infopac[corte].pixelarray
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].imshow(orginal, cmap="bone")
        axs[0].set_title('Imagen Original')
        axs[0].axis('off')
        axs[1].imshow(rotada, cmap='bone')
        axs[1].set_title('Imagen Rotada')
        axs[1].axis('off')
        plt.tight_layout()
        plt.show()

    elif Menu == "d":
        key = input("Ingresa key: ")
        Im = input("Ruta de imagen: ")
        Umbral = input("Umbral: ")
        Kernel = input("Kernel a usar: ")
        A = img.leer_imagen(key,Im)
        B = img.binarizar_imagen(key,A,Umbral,Kernel)
        
    elif Menu == "e":
        break