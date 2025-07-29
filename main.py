class EvaluacionDesempeno:
    def __init__(self, puntualidad, equipo, productividad):
        self.puntualidad = puntualidad
        self.equipo = equipo
        self.productividad = productividad
        self.promedio = self.calcular_promedio()
        self.estado = self.obtener_estado()

    def calcular_promedio(self):
        return round((self.puntualidad + self.equipo + self.productividad) / 3, 2)

    def obtener_estado(self):
        if self.promedio >= 7:
            return "Satisfactorio"
        else:
            return "Mejorar"

empleados = {}

print("CONTROL DE EMPLEADOS:")

codigo = input("Ingrese el código del Empleado: ")
nombre = input("Ingrese el nombre completo: ")
departamento = input("Ingrese el departamento en el que trabaja: ")
antiguedad = input("Ingrese la antigüedad del empleado: ")

print(f"\nPara conocer el desempeño del empleado {nombre}, por favor responda:")

puntualidad = int(input("Puntualidad (0-10): "))
equipo = int(input("Trabajo en equipo (0-10): "))
productividad = int(input("Nivel de productividad (0-10): "))
observaciones = input("Agregue sus observaciones: ")

evaluacion = EvaluacionDesempeno(puntualidad, equipo, productividad)

print(f"\nEl desempeño del empleado es: {evaluacion.estado} (Promedio: {evaluacion.promedio})")

print(f"\nPor favor, ingrese la información de contacto de {nombre}:")
telefono = input("Número telefónico: ")
correo = input("Correo electrónico: ")

empleados[codigo] = {
    "nombre": nombre,
    "departamento": departamento,
    "antiguedad": antiguedad,
    "evaluacion": {
        "puntualidad": puntualidad,
        "equipo": equipo,
        "productividad": productividad,
        "observaciones": observaciones,
        "promedio": evaluacion.promedio,
        "estado": evaluacion.estado,
    },
    "contacto": {
        "telefono": telefono,
        "correo": correo
    }
}

print("\nBÚSQUEDA DE EMPLEADOS")
empleado_buscado = input("Ingrese el código del empleado que desea buscar: ")

if empleado_buscado in empleados:
    empleado = empleados[empleado_buscado]
    print("\nEmpleado encontrado:")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Departamento: {empleado['departamento']}")
    print(f"Antigüedad: {empleado['antiguedad']}")
    print(f"Puntualidad: {empleado['evaluacion']['puntualidad']}")
    print(f"Trabajo en equipo: {empleado['evaluacion']['equipo']}")
    print(f"Productividad: {empleado['evaluacion']['productividad']}")
    print(f"Promedio: {empleado['evaluacion']['promedio']}")
    print(f"Estado: {empleado['evaluacion']['estado']}")
    print(f"Observaciones: {empleado['evaluacion']['observaciones']}")
    print(f"Correo: {empleado['contacto']['correo']}")
    print(f"Teléfono: {empleado['contacto']['telefono']}")
else:
    print("Empleado no encontrado.")


#op = input("¿Desea ver la información completa del empleado? (si/no) ").upper()
#if op == "si":
#     mostrar.empleado()
#else:
#    exit()





