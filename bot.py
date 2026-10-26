# Importar las librerías necesarias
import random
import datetime

# --- DATOS ORIGINALES ---

# DATOS USUARIOS
usuarios = [{'Nombre': 'Marcelo', 'Apellido': 'Cortés', 'Dni': 26344067, 'Cuenta': '409662-9', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '25-02-2023', 'Valor': 2747}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '16-02-2023', 'Valor': 2174}], 'Saldo': 3790},
{'Nombre': 'Shelby', 'Apellido': 'Roberts', 'Dni': 38729016, 'Cuenta': '406417-6', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '22-02-2023', 'Valor': 5870}], 'Saldo': 27545},
{'Nombre': 'Rigoberto', 'Apellido': 'Rey', 'Dni': 13656095, 'Cuenta': '402331-3', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '22-02-2023', 'Valor': 4045}, 
{'Servicio': 'Internet', 'Vencimiento': '16-02-2023', 'Valor': 2171}], 'Saldo': 29908},
{'Nombre': 'Luz', 'Apellido': 'Fernández', 'Dni': 32812712, 'Cuenta': '402246-1',
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '23-01-2023', 'Valor': 5271}], 'Saldo': 18348},
{'Nombre': 'Cecilia', 'Apellido': 'Ferrer', 'Dni': 38338334, 'Cuenta': '401243-1', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '01-02-2023', 'Valor': 3597}, 
{'Servicio': 'Internet', 'Vencimiento': '18-02-2023', 'Valor': 1782}], 'Saldo': 17048},
{'Nombre': 'Victorio', 'Apellido': 'Lozano', 'Dni': 25574081, 'Cuenta': '402477-2', 
'FacturasAdeudadas': [{'Servicio': 'Municipal', 'Vencimiento': '19-01-2023', 'Valor': 4341}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '26-02-2023', 'Valor': 5603}, {'Servicio': 'Internet', 'Vencimiento': '27-02-2023', 'Valor': 4117}], 
'Saldo': 24885},
{'Nombre': 'Arturo', 'Apellido': 'Méndez', 'Dni': 27481828, 'Cuenta': '407924-9', 
'FacturasAdeudadas': [{'Servicio': 'Municipal', 'Vencimiento': '07-02-2023', 'Valor': 2592}], 'Saldo': 17249},
{'Nombre': 'Salvio', 'Apellido': 'Carmona', 'Dni': 19585585, 'Cuenta': '406634-1', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '19-02-2023', 'Valor': 4966}, 
{'Servicio': 'Agua', 'Vencimiento': '07-02-2023', 'Valor': 3241}], 'Saldo': 24304},
{'Nombre': 'Lázaro', 'Apellido': 'Durán', 'Dni': 33865607, 'Cuenta': '404204-2', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '15-01-2023', 'Valor': 2870}, 
{'Servicio': 'Agua', 'Vencimiento': '23-02-2023', 'Valor': 3970}, {'Servicio': 'Municipal', 'Vencimiento': '01-02-2023', 'Valor': 3617}, 
{'Servicio': 'Internet', 'Vencimiento': '27-01-2023', 'Valor': 3938}], 'Saldo': 29098},
{'Nombre': 'Nicolás', 'Apellido': 'Caballero', 'Dni': 29808716, 'Cuenta': '406149-8', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '24-01-2023', 'Valor': 3564}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '24-02-2023', 'Valor': 1721}, 
{'Servicio': 'Internet', 'Vencimiento': '04-02-2023', 'Valor': 2202}], 'Saldo': 25611},
{'Nombre': 'José', 'Apellido': 'Gallardo', 'Dni': 22838265, 'Cuenta': '401412-7', 
'FacturasAdeudadas': [{'Servicio': 'Municipal', 'Vencimiento': '06-01-2023', 'Valor': 3516}], 'Saldo': 23070},
{'Nombre': 'Emilio', 'Apellido': 'Pérez', 'Dni': 12183469, 'Cuenta': '405884-4', 
'FacturasAdeudadas': [{'Servicio': 'Telefonía Móvil', 'Vencimiento': '25-02-2023', 'Valor': 5319}, 
{'Servicio': 'Internet', 'Vencimiento': '06-01-2023', 'Valor': 2541}], 'Saldo': 21252},
{'Nombre': 'Otilia', 'Apellido': 'Domínguez', 'Dni': 15317104, 'Cuenta': '404208-8', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '23-02-2023', 'Valor': 1748}], 'Saldo': 29883},
{'Nombre': 'Ezequiel', 'Apellido': 'Soler', 'Dni': 15945952, 'Cuenta': '402077-5', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '03-02-2023', 'Valor': 4200}, 
{'Servicio': 'Municipal', 'Vencimiento': '27-02-2023', 'Valor': 2598}], 'Saldo': 13590},
{'Nombre': 'Cayetano', 'Apellido': 'Ortega', 'Dni': 36963275, 'Cuenta': '409858-5', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '30-01-2023', 'Valor': 3359}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '05-02-2023', 'Valor': 2797}], 'Saldo': 29288},
{'Nombre': 'Juan', 'Apellido': 'Méndez', 'Dni': 40858221, 'Cuenta': '408102-5', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '06-02-2023', 'Valor': 5227}, 
{'Servicio': 'Agua', 'Vencimiento': '25-01-2023', 'Valor': 4237}], 'Saldo': 27800},
{'Nombre': 'Marta', 'Apellido': 'Cambil', 'Dni': 30565127, 'Cuenta': '406371-9', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '06-01-2023', 'Valor': 4052}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '20-02-2023', 'Valor': 2109}], 'Saldo': 27956},
{'Nombre': 'Esiquio', 'Apellido': 'Calvo', 'Dni': 39743640, 'Cuenta': '409666-5', 
'FacturasAdeudadas': [{'Servicio': 'Municipal', 'Vencimiento': '20-02-2023', 'Valor': 1775}], 'Saldo': 19572},
{'Nombre': 'Iván', 'Apellido': 'Ruiz', 'Dni': 14327165, 'Cuenta': '401212-4', 
'FacturasAdeudadas': [{'Servicio': 'Telefonía Móvil', 'Vencimiento': '13-02-2023', 'Valor': 1816}], 'Saldo': 29991},
{'Nombre': 'Noel', 'Apellido': 'Montgomery', 'Dni': 15365358, 'Cuenta': '402530-9', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '18-02-2023', 'Valor': 2954}], 'Saldo': 13270},
{'Nombre': 'Noel', 'Apellido': 'Travis', 'Dni': 32695653, 'Cuenta': '401987-9', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '29-01-2023', 'Valor': 4377}, 
{'Servicio': 'Electricidad', 'Vencimiento': '20-01-2023', 'Valor': 4013}], 'Saldo': 26625},
{'Nombre': 'Josefa', 'Apellido': 'Castillo', 'Dni': 37865298, 'Cuenta': '406467-1', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '15-01-2023', 'Valor': 2794}, 
{'Servicio': 'Electricidad', 'Vencimiento': '03-01-2023', 'Valor': 2566}], 'Saldo': 23888},
{'Nombre': 'Edgar', 'Apellido': 'Pascual', 'Dni': 17615561, 'Cuenta': '408807-2', 
'FacturasAdeudadas': [{'Servicio': 'Telefonía Móvil', 'Vencimiento': '15-02-2023', 'Valor': 5500}, 
{'Servicio': 'Electricidad', 'Vencimiento': '11-02-2023', 'Valor': 3590}, 
{'Servicio': 'Agua', 'Vencimiento': '21-01-2023', 'Valor': 4682}, 
{'Servicio': 'Municipal', 'Vencimiento': '09-02-2023', 'Valor': 2565}], 'Saldo': 25349},
{'Nombre': 'Ramiro', 'Apellido': 'Ramírez', 'Dni': 16656444, 'Cuenta': '409585-3', 
'FacturasAdeudadas': [{'Servicio': 'Telefonía Móvil', 'Vencimiento': '21-02-2023', 'Valor': 4744}, 
{'Servicio': 'Electricidad', 'Vencimiento': '07-01-2023', 'Valor': 3570}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '14-02-2023', 'Valor': 2996}], 'Saldo': 25678},
{'Nombre': 'Ali', 'Apellido': 'Short', 'Dni': 14003158, 'Cuenta': '405315-6', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '27-01-2023', 'Valor': 4053}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '13-01-2023', 'Valor': 5106}], 'Saldo': 22572},
{'Nombre': 'Lázaro', 'Apellido': 'Parra', 'Dni': 11401498, 'Cuenta': '404112-1', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '14-02-2023', 'Valor': 5218}, 
{'Servicio': 'Electricidad', 'Vencimiento': '30-01-2023', 'Valor': 4763}], 'Saldo': 12478},
{'Nombre': 'Eliseo', 'Apellido': 'Castro', 'Dni': 14014305, 'Cuenta': '409976-5', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '04-02-2023', 'Valor': 4019}, 
{'Servicio': 'Electricidad', 'Vencimiento': '19-01-2023', 'Valor': 5809}], 'Saldo': 25535},
{'Nombre': 'Julio', 'Apellido': 'Soler', 'Dni': 20444786, 'Cuenta': '402929-2', 
'FacturasAdeudadas': [{'Servicio': 'Telefonía Móvil', 'Vencimiento': '09-01-2023', 'Valor': 4800}, 
{'Servicio': 'Internet', 'Vencimiento': '27-01-2023', 'Valor': 3773}, 
{'Servicio': 'Electricidad', 'Vencimiento': '16-01-2023', 'Valor': 3924}], 'Saldo': 23853},
{'Nombre': 'Federico', 'Apellido': 'Santiago', 'Dni': 29405122, 'Cuenta': '409493-2', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '27-02-2023', 'Valor': 4617}], 'Saldo': 28539},
{'Nombre': 'Bernardo', 'Apellido': 'Rey', 'Dni': 12829857, 'Cuenta': '401534-5', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '22-01-2023', 'Valor': 2408}, 
{'Servicio': 'Agua', 'Vencimiento': '11-01-2023', 'Valor': 3137}], 'Saldo': 22234},
{'Nombre': 'Matías', 'Apellido': 'Hidalgo', 'Dni': 35418172, 'Cuenta': '409668-2', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '16-01-2023', 'Valor': 2187}], 'Saldo': 28294},
{'Nombre': 'Abdón', 'Apellido': 'Navarro', 'Dni': 35729884, 'Cuenta': '409079-8', 
'FacturasAdeudadas': [{'Servicio': 'Telefonía Móvil', 'Vencimiento': '19-01-2023', 'Valor': 2942}, 
{'Servicio': 'Internet', 'Vencimiento': '09-01-2023', 'Valor': 2563}], 'Saldo': 16126},
{'Nombre': 'Samuel', 'Apellido': 'Márquez', 'Dni': 35917042, 'Cuenta': '407283-5', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '21-02-2023', 'Valor': 3358}, 
{'Servicio': 'Electricidad', 'Vencimiento': '03-01-2023', 'Valor': 2566}], 'Saldo': 16327},
{'Nombre': 'Teresa', 'Apellido': 'Carrasco', 'Dni': 13248587, 'Cuenta': '402721-4', 
'FacturasAdeudadas': [{'Servicio': 'Agua', 'Vencimiento': '04-02-2023', 'Valor': 4019}, 
{'Servicio': 'Electricidad', 'Vencimiento': '19-01-2023', 'Valor': 5809}], 'Saldo': 24629},
{'Nombre': 'Isabel', 'Apellido': 'Cabrera', 'Dni': 40652949, 'Cuenta': '404022-4', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '01-02-2023', 'Valor': 3597}, 
{'Servicio': 'Municipal', 'Vencimiento': '19-01-2023', 'Valor': 4341}], 'Saldo': 18218},
{'Nombre': 'Cayetano', 'Apellido': 'Lorenzo', 'Dni': 18982267, 'Cuenta': '405395-8', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '16-01-2023', 'Valor': 2187}], 'Saldo': 22028},
{'Nombre': 'Aurelia', 'Apellido': 'Aguilar', 'Dni': 12030952, 'Cuenta': '408498-5', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '14-02-2023', 'Valor': 2944}, 
{'Servicio': 'Internet', 'Vencimiento': '27-02-2023', 'Valor': 4617}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '19-01-2023', 'Valor': 2942}], 'Saldo': 21495},
{'Nombre': 'Ramiro', 'Apellido': 'López', 'Dni': 38444115, 'Cuenta': '408707-2', 
'FacturasAdeudadas': [{'Servicio': 'Municipal', 'Vencimiento': '06-01-2023', 'Valor': 3516}, 
{'Servicio': 'Agua', 'Vencimiento': '15-01-2023', 'Valor': 2794}], 'Saldo': 27258},
{'Nombre': 'Urbano', 'Apellido': 'Moya', 'Dni': 27487008, 'Cuenta': '409994-4', 
'FacturasAdeudadas': [{'Servicio': 'Electricidad', 'Vencimiento': '03-01-2023', 'Valor': 5292}], 'Saldo': 20076},
{'Nombre': 'Brenden', 'Apellido': 'Martin', 'Dni': 31275281, 'Cuenta': '402400-8', 
'FacturasAdeudadas': [{'Servicio': 'Internet', 'Vencimiento': '23-02-2023', 'Valor': 1748}, 
{'Servicio': 'Telefonía Móvil', 'Vencimiento': '15-02-2023', 'Valor': 5500}], 'Saldo': 16374}]

# DATOS SUCURSALES
sucursales = {"Oeste": ["Merlo", "Castelar", "Ramos Mejía"],
"Norte": ["Martínez", "San Isidro", "Vicente López"],
"Sur": ["Quilmes", "Lanús", "Avellaneda"],
"Caba": ["Belgrano", "Palermo", "Recoleta"],
}


# --- FUNCIONES DEL CHATBOT ---

# FUNCIÓN PARA BUSCAR USUARIO POR DNI
def buscarUsuarioPorDni(nroBuscado):
  print("\nBuscando usuario...")
  for usuario in usuarios:
    if usuario["Dni"] == nroBuscado:
      return usuario
  return None

# FUNCIÓN PARA CONSULTAR EL SALDO
def consultarSaldo(usuario):
  print("\nConsultando Saldo...")
  print(f"Titular: {usuario['Nombre']} {usuario['Apellido']}")
  print(f"Cuenta N°: {usuario['Cuenta']}")
  print(f"Saldo disponible: ${usuario['Saldo']}")

# FUNCIÓN PARA CONSULTAR FACTURAS
def consultarFacturas(usuario):
  print("\nConsultando Facturas...")
  facturas = usuario["FacturasAdeudadas"]
  if not facturas:
    print("No posee facturas adeudadas.")
  else:
    print(f"Facturas adeudadas ({len(facturas)}):")
    total = 0
    for i, factura in enumerate(facturas, start=1):
      print(f"  {i}. {factura['Servicio']} | Vencimiento: {factura['Vencimiento']} | Importe: ${factura['Valor']}")
      total += factura["Valor"]
    print(f"Total adeudado: ${total}")

# FUNCIÓN PARA PAGAR FACTURAS
def pagarFacturas(usuario):
  print("\nPagando Facturas...")
  # LAS FACTURAS SOLO SE PAGAN SI TIENES SALDO SUFICIENTE
  # SI LAS FACTURAS SE PAGAN, SE BORRAN DEL DICCIONARIO
  facturas = usuario["FacturasAdeudadas"]
  if not facturas:
    print("No posee facturas adeudadas para pagar.")
    return

  print(f"Saldo disponible: ${usuario['Saldo']}")
  print("Facturas pendientes:")
  total = 0
  for i, factura in enumerate(facturas, start=1):
    print(f"  {i}. {factura['Servicio']} | Vencimiento: {factura['Vencimiento']} | Importe: ${factura['Valor']}")
    total += factura["Valor"]
  print(f"Total a pagar: ${total}")

  print("\n¿Qué desea hacer?")
  print("  1. Pagar una factura individual")
  print("  2. Pagar todas las facturas")
  print("  3. Cancelar")
  opcion_pago = input("Seleccione una opción: ").strip()

  if opcion_pago == "1":
    num = input(f"Ingrese el número de la factura a pagar (1-{len(facturas)}): ").strip()
    if num.isdigit() and 1 <= int(num) <= len(facturas):
      idx = int(num) - 1
      factura_seleccionada = facturas[idx]
      importe = factura_seleccionada["Valor"]
      if usuario["Saldo"] >= importe:
        usuario["Saldo"] -= importe
        facturas.pop(idx)
        print(f"\n¡Pago exitoso! Se abonó la factura de {factura_seleccionada['Servicio']} por ${importe}.")
        print(f"Su nuevo saldo es: ${usuario['Saldo']}")
      else:
        print(f"\nSaldo insuficiente. Saldo actual: ${usuario['Saldo']} | Importe necesario: ${importe}")
    else:
      print("Opción inválida.")
  elif opcion_pago == "2":
    if usuario["Saldo"] >= total:
      usuario["Saldo"] -= total
      facturas.clear()
      print(f"\n¡Pago exitoso! Se abonaron todas las facturas por un total de ${total}.")
      print(f"Su nuevo saldo es: ${usuario['Saldo']}")
    else:
      print(f"\nSaldo insuficiente. Saldo actual: ${usuario['Saldo']} | Total necesario: ${total}")
  elif opcion_pago == "3":
    print("Operación cancelada.")
  else:
    print("Opción inválida.")

# FUNCIÓN PARA CONSULTAR SUCURSALES
def consultarSucursales():
  print("\nAccediendo a datos de sucursales...")
  print("Sucursales disponibles por zona:")
  for zona, lista in sucursales.items():
    print(f"  • Zona {zona}: {', '.join(lista)}")

# FUNCIÓN PARA SACAR TURNO
def sacarTurno():
  print("\nObteniendo horarios disponibles...")
  # Seleccionar zona
  zonas = list(sucursales.keys())
  print("\nZonas disponibles:")
  for i, zona in enumerate(zonas, start=1):
    print(f"  {i}. {zona}")
  opc_zona = input("Seleccione una zona (número): ").strip()
  if not (opc_zona.isdigit() and 1 <= int(opc_zona) <= len(zonas)):
    print("Opción no válida. Cancelando solicitud de turno.")
    return
  zona_elegida = zonas[int(opc_zona) - 1]

  # Seleccionar sucursal
  sucursales_zona = sucursales[zona_elegida]
  print(f"\nSucursales en zona {zona_elegida}:")
  for i, suc in enumerate(sucursales_zona, start=1):
    print(f"  {i}. {suc}")
  opc_suc = input("Seleccione una sucursal (número): ").strip()
  if not (opc_suc.isdigit() and 1 <= int(opc_suc) <= len(sucursales_zona)):
    print("Opción no válida. Cancelando solicitud de turno.")
    return
  sucursal_elegida = sucursales_zona[int(opc_suc) - 1]

  # Fechas disponibles a partir de mañana usando datetime
  hoy = datetime.date.today()
  fechas = [hoy + datetime.timedelta(days=i) for i in range(1, 4)]
  print("\nFechas disponibles:")
  for i, f in enumerate(fechas, start=1):
    print(f"  {i}. {f.strftime('%d/%m/%Y')}")
  opc_fecha = input("Seleccione una fecha (1-3): ").strip()
  if not (opc_fecha.isdigit() and 1 <= int(opc_fecha) <= len(fechas)):
    print("Opción no válida. Cancelando solicitud de turno.")
    return
  fecha_elegida = fechas[int(opc_fecha) - 1]

  # Horarios disponibles usando random
  horarios_base = ["09:00", "10:30", "11:45", "14:00", "15:15", "16:30"]
  horarios_disponibles = sorted(random.sample(horarios_base, 3))
  print("\nHorarios disponibles:")
  for i, h in enumerate(horarios_disponibles, start=1):
    print(f"  {i}. {h} hs")
  opc_hora = input("Seleccione un horario (1-3): ").strip()
  if not (opc_hora.isdigit() and 1 <= int(opc_hora) <= len(horarios_disponibles)):
    print("Opción no válida. Cancelando solicitud de turno.")
    return
  hora_elegida = horarios_disponibles[int(opc_hora) - 1]

  nro_turno = random.randint(1000, 9999)
  print("\n" + "=" * 45)
  print("           ¡TURNO REGISTRADO!         ")
  print("=" * 45)
  print(f"Número de Turno: #{nro_turno}")
  print(f"Sucursal:        {sucursal_elegida} ({zona_elegida})")
  print(f"Fecha:           {fecha_elegida.strftime('%d/%m/%Y')}")
  print(f"Horario:         {hora_elegida} hs")
  print("=" * 45)



# --- INTERACCIONES DEL CHATBOT ---

# MENSAJE INICIAL
print("\n**¡Hola! Soy Telmo, tu asistente virtual**")

# SOLICITAR DNI CON input() Y ALMACENARLO EN UNA VARIABLE
# BUSCAR USUARIO SEGÚN SU DNI Y ALMACENARLO EN UNA VARIABLE LLAMADA "usuarioActual"
usuarioActual = None
while usuarioActual is None:
  entradaDni = input("\nIngrese su número de DNI (sin puntos): ").strip()
  if entradaDni.isdigit():
    numeroDni = int(entradaDni)
    usuarioActual = buscarUsuarioPorDni(numeroDni)
    if usuarioActual is None:
      print("No se encontró ningún usuario con ese DNI. Intente nuevamente.")
  else:
    print("Por favor, ingrese un número de DNI válido (solo números).")

# SALUDAR AL "usuarioActual" SEGÚN SU NOMBRE
print("\nHola", usuarioActual["Nombre"], "¡Bienvenido a nuestro sistema!")


# BUCLE DEL CHATBOT - PERMITIR ELEGIR OPCIONES HASTA QUE DESEE TERMINAR

continuar = "SI"
while continuar == "SI":
  opcion = input("""
  Ingrese el número de opción que desea:
  
  1. Consultar saldo
  2. Consultar facturas de servicios vencidas
  3. Pagar facturas
  4. Consultar sucursales
  5. Solicitar un turno
  >>>>>>>>>>>>: """).strip()

  # VERIFICAR QUE LA OPCIÓN INGRESADA SEA CORRECTA
  # USAR UN CONDICIONAL PARA EJECUTAR LA FUNCIÓN QUE CORRESPONDA SEGÚN LA ELECCIÓN
  if opcion == "1":
    consultarSaldo(usuarioActual)
  elif opcion == "2":
    consultarFacturas(usuarioActual)
  elif opcion == "3":
    pagarFacturas(usuarioActual)
  elif opcion == "4":
    consultarSucursales()
  elif opcion == "5":
    sacarTurno()
  else:
    print("\nOpción no válida. Por favor ingrese un número del 1 al 5.")

  # PREGUNTAR SI DESEA CONTINUAR
  respuesta = input("\n¿Desea continuar operando? (SI/NO): ").strip().upper()
  if respuesta == "SI" or respuesta == "S":
    continuar = "SI"
  else:
    continuar = "NO"


# CUANDO TERMINA EL BUCLE, SE MUESTRA UN MENSAJE DE DESPEDIDA
print("\n**¡Gracias por utilizar el servicio de autogestión!**")
