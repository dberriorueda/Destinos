class Cotizacion:
    def __init__(self, destino, precio_adulto, precio_nino):
        self.destino = destino
        self.precio_adulto = precio_adulto
        self.precio_nino = precio_nino
    
    def calcular_total(self, adultos, ninos):
        total = (self.precio_adulto * adultos) + (self.precio_nino * ninos)
        return total
    
def obtenerCotizacion(destinos, opcion):
    return destinos.get(opcion)  

def main():
    destinos = {
        1: Cotizacion("guajira", 1450000, 870000),
        2: Cotizacion("Cañon de Chicamocha", 1600000, 960000),
        3: Cotizacion("Llanos orientales",1200000,720000)
    }

    nombre_cliente = input("Ingrese el nombre del cliente: ")

    print("Destinos disponibles:")
    for opcion, cotizacion in destinos.items():
        print(f"{opcion}. {cotizacion.destino}:")
    opcion= int(input("Ingrese el destino: "))
    adultos = int(input("Ingrese el número de personas adultas: "))
    ninos = int(input("Ingrese el número de niños: "))

    cotizacion = obtenerCotizacion(destinos, opcion)
    if cotizacion:
        total_destino = cotizacion.calcular_total(adultos,ninos)
        print("\nResumen de la cotización:")
        print("Nombre del cliente:", nombre_cliente)
        print("Destino:", cotizacion.destino)
        print("Número de personas adultas:", adultos)
        print("Número de niños:", ninos)
        print(f"Total a pagar por el destino:",total_destino)
    else:
        print("Destino no válido.")

if __name__ == "__main__":
    main()
