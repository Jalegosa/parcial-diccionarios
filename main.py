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
input("\n CONTROL DE EMPLEADOS:")
codigo = input("Ingrese el código del Empleado: ")
nombre = input("Ingrese el nombre completo: ")
departamento = input("Ingrese el departamento en el que trabaja: ")



print(f"El empleado {nombre} con codigo {codigo} trabaja en {departamento}")