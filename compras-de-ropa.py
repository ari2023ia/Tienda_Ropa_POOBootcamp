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
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_inventario(self):
        print("Inventario de productos:")
        for index, producto in enumerate(self.__productos):
            print(f"{index + 1}. ", end="")
            producto.mostrar_info()

    def obtener_producto(self, indice):
        if 0 <= indice < len(self.__productos):
            return self.__productos[indice]
        else:
            return None


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto.nombre} ha sido agregado al carrito.")

    def mostrar_carrito(self):
        print("Productos en el carrito:")
        for producto in self.productos:
            producto.mostrar_info()

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)


class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.carrito = Carrito()

    def agregar_producto_inventario(self, producto):
        self.inventario.agregar_producto(producto)

    def mostrar_inventario(self):
        self.inventario.mostrar_inventario()

    def agregar_al_carrito(self, indice_producto):
        producto = self.inventario.obtener_producto(indice_producto)
        if producto:
            self.carrito.agregar_producto(producto)
        else:
            print("Producto no encontrado en el inventario.")

    def mostrar_carrito(self):
        self.carrito.mostrar_carrito()

    def procesar_pago(self):
        total = self.carrito.calcular_total()
        print(f"Total a pagar: ${total}")
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


def main():

    inventario = Inventario()
    inventario.agregar_producto(Camisa("Camisa", 25000, 50, "Mediano", "Blanco"))
    inventario.agregar_producto(Falda("Falda", 28000, 15, "Pequeño", "Seda"))
    inventario.agregar_producto(Pantalon("Pantalon", 30000, 30, "Mediano", "Jeans"))
    inventario.agregar_producto(Chaqueta("Chaqueta", 55000, 20, "Grande", "Cuero"))
    inventario.agregar_producto(Zapato_de_Hombre("Zapato de Hombre", 60000, 25, "Mediano", "Mocasin"))
    inventario.agregar_producto(Blusa("Blusa", 22000, 40, "Mediano", "100% Algodón"))
    inventario.agregar_producto(Vestido("Vestido", 45000, 10, "Mediano", "100% Seda importada"))
    inventario.agregar_producto(Zapato_de_Mujer("Zapato de Mujer", 50000, 20, "Pequeño", "Tacon"))
    tienda = Tienda()
    
 # Proceso de compra
    continuar_comprando = True
    while continuar_comprando:
        tienda.mostrar_inventario()
        try:
            seleccion = int(input("Elige el número del producto que quieres agregar al carrito: ")) - 1
            tienda.agregar_al_carrito(seleccion)
        except ValueError:
            print("Entrada inválida.")
            continue

        respuesta = input("¿Quieres seguir comprando? (s/n): ").strip().lower()
        if respuesta == 'n':
            continuar_comprando = False

    # Mostrar el carrito y proceder al pago
    tienda.mostrar_carrito()
    tienda.procesar_pago()


# Ejecutar el programa principal
if __name__ == "__main__":
    main()