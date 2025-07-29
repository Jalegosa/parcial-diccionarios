empleados = {
    "codigo": {
    "nombre": "nombre",
     "departamento" : "departamento",
     "antiguedad": "antiguedad",
      "evaluacion": {
          "puntualidad": "puntualidad",
          "equipo": "equipo",
          "productividad": "productividad",
          "observaciones": "observaciones",
          "promedio" : "promedio",
          "estado": "estado",
      },
        "contacto":{
            "telefono" : "telefono",
            "correo" : "correo"
        }
    }

    }

#def resultado_promedio(calificacion):
#    calificacion = puntualidad + equipo + productividad
# return 0



print(" CONTROL DE EMPLEADOS:")
codigo = input("Ingrese el código del Empleado: ")
nombre = input("Ingrese el nombre completo: ")
departamento = input("Ingrese el departamento en el que trabaja: ")
antiguedad = input("Ingrese la antiguedad del empleado: ")

#print(f"El empleado {nombre} con codigo {codigo} trabaja en {departamento}")

print(f"\n Para conocer el desempeño del empleado {nombre} por favor, responda:")
puntualidad = int (input("Puntualidad (0-10):  "))
equipo = input("Trabajo en Equipo (0-10): ")
productividad = input("Nivel de Productividad (0-10): ")
observaciones = input("Agregue sus observaciones : ")

print(f"\n Por favor ingrese la información de contacto de {nombre}:")
telefono= input("\nNúmero telefónico: ")
correo = input("Correo electrónico :")

#op = input("¿Desea ver la información completa del empleado? (si/no) ").upper()
#if op == "si":
#     mostrar.empleado()
#else:
#    exit()


print("\nBúsqueda de empleados")
empleado_buscado = input("Ingrese el codigo de empleado que desea buscar: ")

if empleado_buscado in empleados:
    empleado = empleados[empleado_buscado]
    print("\nEmpleado encontrado:")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Departamento: {empleado['departamento']}")
    print(f"Antiguedad: {empleado['antiguedad']}")
    print(f"Evaluacion: {empleado['evaluacion']['estado']}")
    print(f"Correo: {empleado['contacto']['correo']}")
    print(f"Teléfono: {empleado['contacto']['telefono']}")
else:
    print("Empleado no encontrado.")





