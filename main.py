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
          "promedio" : "promedio"
      },
        "contacto":{
            "telefono" : "telefono",
            "correo" : "correo"
        }
    }

    }

def resultado_promedio(calificacion)


print(" CONTROL DE EMPLEADOS:")
codigo = input("Ingrese el código del Empleado: ")
nombre = input("Ingrese el nombre completo: ")
departamento = input("Ingrese el departamento en el que trabaja: ")
#print(f"El empleado {nombre} con codigo {codigo} trabaja en {departamento}")

print(f"\n Para conocer el desempeño del empleado {nombre} por favor, responda:")
puntualidad = input("\nPuntualidad (0-10):  ")
equipo = input("\nTrabajo en Equio (0-10): ")
productividad = input("\nNivel de Productividad (0-10): ")
observaciones = input("Agregue sus observaciones :")






