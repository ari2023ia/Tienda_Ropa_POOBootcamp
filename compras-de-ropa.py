class Producto:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_info(self):
        print(f"{self.nombre}")    

class Prenda(Producto):

    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre)
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        super().mostrar_info()
            
    def mostrar_info_completo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Talla: {self.precio}")
        print(f"Color: {self.cantidad}")
        

class Camisa(Prenda):
    
    def __init__(self, nombre, precio, cantidad, talla, color):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.color = color
    
    def mostrar_info(self):
        super().mostrar_info()
    
    def mostrar_info_completo(self):
        super().mostrar_info_completo()    
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.color}")


class Falda(Prenda):

    def __init__(self, nombre, precio, cantidad, talla, tipo_de_tela):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.tipo_de_tela = tipo_de_tela
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.tipo_de_tela}")
        

class Pantalon(Prenda):

    def __init__(self, nombre, precio, cantidad, talla, tipo):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.tipo = tipo
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.tipo}")        


class Zapato_de_Hombre(Prenda):

    def __init__(self, nombre, precio, cantidad, talla, tipo):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.tipo = tipo
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.tipo}")


class Chaqueta(Prenda):

    def __init__(self, nombre, precio, cantidad, talla, tipo_de_tela):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.tipo_de_tela = tipo_de_tela
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.tipo_de_tela}")
        

class Blusa(Prenda):

    def __init__(self, nombre, precio, cantidad, talla, tipo_de_tela):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.tipo_de_tela = tipo_de_tela
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.tipo_de_tela}")
          
                  
class Vestido(Prenda):

    def __init__(self, nombre, precio, cantidad, talla, tipo):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.tipo = tipo
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.tipo}")
        
        
class Zapato_de_Mujer(Prenda):

    def __init__(self, nombre, precio, cantidad, talla, tipo):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.tipo = tipo
    
    def mostrar_info(self):
        super().mostrar_info()
  
    def mostrar_info_completo(self):
        super().mostrar_info_completo()
        print(f"Talla: {self.talla}")
        print(f"Talla: {self.tipo}")        
        
        
class Inventario:
    
    def __init__(self):
        self.__prendas = []

    def agregar_prenda(self, prenda):
        self.__prendas.append(prenda)
        
    def mostrar_inventario(self):
        print("Prendas Disponibles:")
        for index, prenda in enumerate(self.__prendas):
            print(f"{index + 1}.")
            prenda.mostrar_info()
    
    def obtener_prenda(self, indice):
        if 0 <= indice < len(self.__prendas):
            return self.__prendas[indice]
        else:
            return None

def main():
    inventario = Inventario()
    inventario.agregar_prenda(Camisa("Camisa", 25000, 50, "Mediano", "Blanco"))
    inventario.agregar_prenda(Falda("Falda", 28000, 15, "Pequeño", "Seda"))
    inventario.agregar_prenda(Pantalon("Pantalon", 30000, 30, "Mediano", "Jeans"))
    inventario.agregar_prenda(Chaqueta("Chaqueta", 55000, 20, "Grande", "Cuero"))
    inventario.agregar_prenda(Zapato_de_Hombre("Zapato de Hombre", 60000, 25, "Mediano", "Mocasin"))
    inventario.agregar_prenda(Blusa("Blusa", 22000, 40, "Mediano", "100% Algodón"))
    inventario.agregar_prenda(Vestido("Vestido", 45000, 10, "Mediano", "100% Seda importada"))
    inventario.agregar_prenda(Zapato_de_Mujer("Zapato de Mujer", 50000, 20, "Pequeño", "Tacon"))

        # Carrito de compras
    carrito = []
    continuar_comprando = True

    while continuar_comprando:
        # Mostrar inventario al usuario
        inventario.mostrar_inventario()

        # Selección de prenda
        try:
            seleccion = int(input("Elige el número de la prenda que quieres agregar al carrito: ")) - 1
            prenda_seleccionada = inventario.obtener_prenda(seleccion)
            if prenda_seleccionada:
                carrito.append(prenda_seleccionada)
                print(f"Has agregado {prenda_seleccionada.nombre} al carrito.")
            else:
                print("Selección inválida. Inténtalo de nuevo.")
                continue
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")
            continue

        # Preguntar si el usuario desea seguir comprando o pagar
        respuesta = input("¿Quieres seguir comprando? (s/n): ").strip().lower()
        if respuesta == 'n':
            continuar_comprando = False

    # Calcular total y proceder al pago
    total = sum(prenda.precio for prenda in carrito)
    print("\nCarrito de compras:")
    for prenda in carrito:
        prenda.mostrar_info()

    print(f"Total a pagar: ${total}")

    # Proceso de pago
    total_pagado = 0
    while total_pagado < total:
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
    if total_pagado >= total:
        cambio = total_pagado - total
        print("¡Compra exitosa!")
        if cambio > 0:
            print(f"Tu cambio es: ${cambio:.2f}")
            
            
if __name__ == "__main__":
    main()  