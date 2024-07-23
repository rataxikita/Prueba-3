import time, os, random
patentes = []
from datetime import datetime
def app():
    while True:
        try:
            print("=== Bienvenido a Auto Seguro ===")
            menu_opcion = int(input("\n 1. Registrar vehiculo \n 2. Buscar vehiculo \n 3. Imprimir certificado \n 4. Salir\n"))
            limpiar_pantalla()
            if menu_opcion == 1:
                print("===Registrar Vehiculo===")
                registro_vehiculo()
            if menu_opcion ==2:
                print("===Buscar Vehiculo===")
                buscar_vehiculo()
            if menu_opcion ==3:
                print("===Imprimir certificado===")
                imprimir_certificados()
            if menu_opcion ==4:
                salida_menu()
                break
        except ValueError:
            print("Ingresa una opcion valida!!!")
            
def obtencion_marca():
    while True:
        marca = input("Ingresa la marca del vehiculo: ")
        if len(marca) >2 and len(marca) <12:
            return marca
        else:
            print("Ingresa marca con mas de 2 caracteres y menos de 12 caracteres")
            
def obtencion_modelo():
    while True:
        modelo = input("Ingresa modelo de vehiculo: ")
        if len(modelo) >0:
            return modelo
        else:
            print("El campo no puede venir vacio. Ingresa modelo del vehiculo")
            
            
def obtencion_tipo():
    while True:
        tipo = input("Ingrese tipo el vehiculo: ").strip()
        if tipo != "" :
            return tipo
        else:
            print("Debes ingresar el tipo del vehiculo")
        
def obtencion_multa():
    while True:
            fecha = input ("Ingresa fecha formato dd-mm-aaaa")
            monto =int(input("Ingresa monto de multa"))
            return fecha,monto
            
        
def obtencion_precio():
    while True:
        try:
            precio = int(input("Ingresa precio del vehiculo: "))
            if precio <= 5000000:
                return precio
            else:
                print("El precio del vehiculo debe ser mayor a $5000000")
        except:
            print("Ingresa valores numericos!!!")
            
def salida_menu():
    os.system("cls")
    
    print("Saliendo del menu.")
    time.sleep(1)
    os.system("cls")
    print("Saliendo del menu..")
    time.sleep(1)
    os.system("cls")
    print("Saliendo del menu...")
    time.sleep(1)
    print("Programa hecho por Catalina Rosales, version 1.0")
    
def obtencion_patente():
    while True:
        patente = input ("Ingrese la patente(2 letras seguidas de 4 numeros)")
        if len(patente) == 6 and patente[:2]. isalpha() and patente[2:].isdigit():
            return patente 
        else: 
            print("Formato incorrecto, la patente debe contener dos letras seguidas de 4 numeros")
        

def obtencion_propietario():
    while True:
        propietario = input("Ingrese nombre completo del propietario del vehiculo: ").strip()
        if propietario != "" :
            return propietario
        else:
            print("Debes ingresar el nombre del propietario")
            
def obtencion_fecha():
    fecha_actual = datetime.now()
    return fecha_actual

def registro_vehiculo():
    while True:
        patente = obtencion_patente()
        tipo = obtencion_tipo()
        marca = obtencion_marca()
        modelo = obtencion_modelo()
        precio = obtencion_precio()
        propietario = obtencion_propietario()
        multa = obtencion_multa()
        fecha_actual= obtencion_fecha()
        vehiculo = {
            "Patente": patente,
            "Marca": marca,
            "Modelo": modelo,
            "Tipo": tipo,
            "Precio": precio,
            "Propietario": propietario,
            "Fecha" : fecha_actual,
            "Multa": multa,
            
            }
        patentes.append(vehiculo)
        print(patentes)
        time.sleep(5)
        print("Vehiculo registrado existosamente")
        continuar = input("Deseas registrar otro vehiculo? 1.Si 2.No \n")
        if continuar != '1':
            break
        limpiar_pantalla()
    

def limpiar_pantalla():
    os.system("cls")
    
def buscar_vehiculo():
    while True:
        print("Patentes registradas")
        for vehiculo in patentes:
            print(vehiculo['Patente'])
        patente_buscar = input("Ingresa patente a buscar: ")
        limpiar_pantalla()
        encontrado = False
        for vehiculo in patentes:
            if vehiculo["Patente"] == patente_buscar:
                encontrado = True
                print(f"=== Información del vehiculo con patente {patente_buscar} ===")
                print(f"Patente: {vehiculo['Patente']}")
                print(f"Marca: {vehiculo['Marca']}")
                print(f"Tipo: {vehiculo['Tipo']}")
                print(f"Modelo: {vehiculo['Modelo']}")
                print(f"Propietario: {vehiculo['Propietario']}")
                print(f"Multa: {vehiculo['Multa']}")
        if encontrado:
            break
        else:
            print(f"No se encontro ningun vehiculo con patente {patente_buscar}.")
            retry = input("Deseas intentar de nuevo? 1. Si 2. No\n")
            if retry != '1':
                break
def anotaciones_vigentes():
    return int(random.uniform(1500, 3000))
def generar_emision_gases():
    estados_posibles = ["Alto", "Medio", "Bajo"]
    return random.choice(estados_posibles)
def imprimir_certificados():
    if not patentes:
        print("No hay vehiculos registrados para generar certificados.")
        return
    patente_buscar = input("Ingresa la patente del vehiculo par imprimir certificados: ")
    encontrado = False
    
    for vehiculo in patentes:
        if vehiculo["Patente"] == patente_buscar:
            encontrado = True
            print(f"=== Certificados del vehiculo con patente {patente_buscar}===")
            print(f"Nombre: Certificado de Propiedad")
            print(f"Patente: {vehiculo['Patente']}")
            print(f"Marca: {vehiculo['Marca']}")
            print(f"Propietario: {vehiculo['Propietario']}")
            print("===Certificado de Emision de contaminantes===")
            emision_gases = generar_emision_gases()
            print(f"Nombre: Certificado de Emisión de contaminantes")
            print(f"Patente: {vehiculo['Patente']}")
            print(f"Marca: {vehiculo['Marca']}")
            print(f"Tipo: {vehiculo['Tipo']}")
            print(f"Propietario: {vehiculo['Propietario']}")
            print(f"Emision de contaminantes: {emision_gases}")
            print("===Certificado de anotaciones vigentes y multas ===")
            anotaciones = anotaciones_vigentes()
            print(f"Nombre: anotaciones vigentes y multas")
            print(f"Patente: {vehiculo['Patente']}")
            print(f"Marca: {vehiculo['Marca']}")
            print(f"Tipo: {vehiculo['Tipo']}")
            print(f"Propietario: {vehiculo['Propietario']}")
            print(f"Anotaciones vigentes: {anotaciones}")
            print(f"Multas: {vehiculo['Multa']}")
            
            