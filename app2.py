import requests
import json

URL = "http://127.0.0.1:5000/estudiantes"

def mostrar_menu():
    print("Menú CRUD")
    print("1. Ver todos los estudiantes (GET)")
    print("2. Agregar nuevo estudiante (POST)")
    print("3. Actualizar estudiante (PUT)")
    print("4. Eliminar estudiante (DELETE)")
    print("5. Salir")
    
def obtener_estudiantes():
    respuesta = requests.get(URL)
    if respuesta.status_code == 200:
        estudiantes = respuesta.json()
        for estudiante in estudiantes:
            print(estudiante)
    else:
        print("Error al obtener estudiantes")

def agregar_estudiante():
    no_control = input("Número de control: ")
    nombre = input("Nombre: ")
    ap_paterno = input("Apellido Paterno: ")
    ap_materno = input("Apellido Materno: ")
    semestre = int(input("Semestre: "))
    
    data = {
        'no_control': no_control,
        'nombre': nombre,
        'ap_paterno': ap_paterno,
        'ap_materno': ap_materno,
        'semestre': semestre
    }
    
    respuesta = requests.post(URL, json=data)
    print(respuesta.json())

def actualizar_estudiante():
    no_control = input("Número de control del estudiante a actualizar: ")
    nombre = input("Nuevo nombre: ")
    ap_paterno = input("Nuevo Apellido Paterno: ")
    ap_materno = input("Nuevo Apellido Materno: ")
    semestre = int(input("Nuevo semestre: "))
    
    data = {
        'nombre': nombre,
        'ap_paterno': ap_paterno,
        'ap_materno': ap_materno,
        'semestre': semestre
    }
    
    respuesta = requests.put(f"{URL}/{no_control}", json=data)
    print(respuesta.json())

def eliminar_estudiante():
    no_control = input("Número de control del estudiante a eliminar: ")
    respuesta = requests.delete(f"{URL}/{no_control}")
    print(respuesta.json())

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        obtener_estudiantes()
    elif opcion == '2':
        agregar_estudiante()
    elif opcion == '3':
        actualizar_estudiante()
    elif opcion == '4':
        eliminar_estudiante()
    elif opcion == '5':
        break
    else:
        print("Opción no válida, intenta de nuevo.")