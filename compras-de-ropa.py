class Prenda:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        print(f"{self.nombre}")
            
    def mostrar_info_completo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Talla: {self.precio}")
        print(f"Color: {self.cantidad}")
        

class RopaHombre(Prenda):
    
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    
    def mostrar_info(self):
        super().mostrar_info()
    
    def mostrar_info_completo(self):
        super().mostrar_info_completo()    
        print(f"Talla: {self.talla}")


class RopaMujer(Prenda):

    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")


class Inventario:
    
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
        
    def mostrar_inventario(self):
        print("Prendas Disponibles:")
        for index, prenda in enumerate(self.prendas):
            print(f"{index + 1}.")
            prenda.mostrar_info()
    
    def obtener_prenda(self, indice):
        if 0 <= indice < len(self.prendas):
            return self.prendas[indice]
        else:
            return None

def main():
    inventario = Inventario()
    inventario.agregar_prenda(RopaHombre("Camisa", 25000, 50, "Mediano"))
    inventario.agregar_prenda(RopaMujer("Falda", 28000, 15, "Pequeño"))
    inventario.agregar_prenda(Prenda("Pantalon", 30000, 30))
    inventario.agregar_prenda(RopaHombre("Chaqueta", 55000, 20, "Grande"))
    inventario.agregar_prenda(RopaHombre("Zapato", 60000, 25, "Mediano"))
    inventario.agregar_prenda(RopaMujer("Blusa", 22000, 40, "Mediano"))
    inventario.agregar_prenda(RopaMujer("Vestido", 45000, 10, "Mediano"))
    inventario.agregar_prenda(RopaMujer("Zapato", 50000, 20, "Pequeño"))

    inventario.mostrar_inventario()


    try:
        seleccion = int(input("Elige el número de la prenda que quieres comprar: ")) - 1
    except ValueError:
        print("Entrada inválida.")
        return  
    


    prenda_seleccionada = inventario.obtener_prenda(seleccion)
    if prenda_seleccionada is None:
        print("Selección inválida. Inténtalo de nuevo.")
        return

    print("Has elegido:")
    prenda_seleccionada.mostrar_info()
    
    
    print(f"El precio de esta prenda es: ${prenda_seleccionada.precio}")
    total_pagado = 0
    while total_pagado < prenda_seleccionada.precio:
        try:
            pago = float(input("Ingresa el monto a pagar: $"))
            if pago <= 0:
                print("Ingresa una cantidad positiva.")
                continue
            total_pagado += pago
            print(f"Total pagado: ${total_pagado}")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Confirmación de compra
    if total_pagado >= prenda_seleccionada.precio:
        cambio = total_pagado - prenda_seleccionada.precio
        print("¡Compra exitosa!")
        if cambio > 0:
            print(f"Tu cambio es: ${cambio:.2f}")
            
            
if __name__ == "__main__":
    main()  