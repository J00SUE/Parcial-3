from Parcial 3 import Paciente
from Parcial 3 import Imagenes
D = Paciente()
P = 0

while True:
    paciente = {}
    rutan = r"C:\Users\Chimuelo\OneDrive\Escritorio\Parcial 3\nifti"
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

        paciente[I] = {
            'Nombre': N,
            'Edad': E,
            'Estudio': p,
            'Genero': k,
            'Imagen' : z,
            'Nifti' : s
        }

    elif Menu == "b":
        pass
    elif Menu == "c":
        pass
    elif Menu == "d":
        pass
    elif Menu == "e":
        break