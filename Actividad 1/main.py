carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]

estudiantes = []

for _ in range(5):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    carrera = int(input("Ingrese la carrera (0, 1 o 2): "))

    persona = (nombre, apellido, edad, carrera)
    personas.append(persona)

    print("")

for persona in personas:
    nombre = persona[0]
    apellido = persona[1]
    edad = persona[2]
    indice_carrera = persona[3]

    nombre_carrera = carreras[indice_carrera]

    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": nombre_carrera
    }

    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(
        estudiante["nombre"],
        estudiante["apellido"],
        "tiene",
        estudiante["edad"],
        "años y estudia",
        estudiante["carrera"]
    )
