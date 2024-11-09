class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.carrito = Carrito()

    def mostrar_inventario(self):
        self.inventario.mostrar_inventario()

    def mostrar_informacion_prenda(self, indice):
        prenda = self.inventario.obtener_prenda(indice)
        if prenda:
            prenda.mostrar_info_completo()
        else:
            print("Prenda no encontrada.")

    def agregar_producto_al_carrito(self, prenda, cantidad=1):
        if prenda.cantidad >= cantidad:
            self.carrito.agregar_producto(prenda, cantidad)
            prenda.cantidad -= cantidad 
        else:
            print(f"No hay suficiente inventario de {prenda.nombre}.")

    def quitar_producto_del_carrito(self, prenda, cantidad=1):
        self.carrito.quitar_producto(prenda, cantidad)
        prenda.cantidad += cantidad 

    def mostrar_carrito(self):
        self.carrito.mostrar_carrito()

    def calcular_total(self):
        return self.carrito.total_carrito()

    def procesar_pago(self):
        total = self.calcular_total()
        total_pagado = 0
        print(f"El total a pagar es: ${total}")

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

        if total_pagado >= total:
            cambio = total_pagado - total
            print("¡Compra exitosa!")
            if cambio > 0:
                print(f"Tu cambio es: ${cambio:.2f}")

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

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, prenda, cantidad=1):
        for item in self.items:
            if item['producto'] == prenda:
                item['cantidad'] += cantidad
                return
        self.items.append({'producto': prenda, 'cantidad': cantidad})

    def quitar_producto(self, prenda, cantidad=1):
        for item in self.items:
            if item['producto'] == prenda:
                item['cantidad'] -= cantidad
                if item['cantidad'] <= 0:
                    self.items.remove(item)
                return
        print(f"El producto {prenda.nombre} no está en el carrito.")

    def mostrar_carrito(self):
        print("\nCarrito de compras:")
        for item in self.items:
            prenda = item['producto']
            print(f"{prenda.nombre} - Cantidad: {item['cantidad']} - Total: ${prenda.precio * item['cantidad']}")

    def total_carrito(self):
        return sum(item['producto'].precio * item['cantidad'] for item in self.items)


def main():
    tienda = Tienda()

    tienda.inventario.agregar_prenda(Camisa("Camisa", 25000, 50, "Mediano", "Blanco"))
    tienda.inventario.agregar_prenda(Falda("Falda", 28000, 15, "Pequeño", "Seda"))
    tienda.inventario.agregar_prenda(Pantalon("Pantalon", 30000, 30, "Mediano", "Jeans"))
    tienda.inventario.agregar_prenda(Chaqueta("Chaqueta", 55000, 20, "Grande", "Cuero"))
    tienda.inventario.agregar_prenda(Zapato_de_Hombre("Zapato de Hombre", 60000, 25, "Mediano", "Mocasin"))
    tienda.inventario.agregar_prenda(Blusa("Blusa", 22000, 40, "Mediano", "100% Algodón"))
    tienda.inventario.agregar_prenda(Vestido("Vestido", 45000, 10, "Mediano", "100% Seda importada"))
    tienda.inventario.agregar_prenda(Zapato_de_Mujer("Zapato de Mujer", 50000, 20, "Pequeño", "Tacon"))

    continuar_comprando = True
    while continuar_comprando:

        tienda.mostrar_inventario()
        print("0. No elegir ninguna prenda")

        try:
            seleccion = int(input("Elige el número de la prenda que quieres agregar al carrito o '0' para no agregar: ")) - 1
            if seleccion == -1:  # Si el usuario elige "0"
                print("No se agregó ninguna prenda al carrito.")
            else:
                # Mostrar información completa de la prenda seleccionada
                tienda.mostrar_informacion_prenda(seleccion)
                prenda_seleccionada = tienda.inventario.obtener_prenda(seleccion)
                if prenda_seleccionada:
                    cantidad = int(input(f"¿Cuántas unidades de {prenda_seleccionada.nombre} deseas agregar? "))
                    tienda.agregar_producto_al_carrito(prenda_seleccionada, cantidad)
                else:
                    print("Selección inválida.")
                    continue

            # Menú de opciones después de agregar o no agregar al carrito
            while True:
                respuesta = input("¿Quieres seguir comprando (s), ver tu carrito (v), quitar un producto (q) o finalizar compra (f)? (s/v/q/f): ").strip().lower()

                if respuesta == 's':
                    break  # Volver a mostrar el inventario
                elif respuesta == 'v':
                    tienda.mostrar_carrito()
                elif respuesta == 'q':
                    tienda.mostrar_carrito()
                    try:
                        prenda_a_quitar = int(input("¿Qué producto deseas eliminar? Elige el número de la prenda: ")) - 1
                        prenda_seleccionada = tienda.inventario.obtener_prenda(prenda_a_quitar)
                        if prenda_seleccionada:
                            cantidad_a_quitar = int(input(f"¿Cuántas unidades de {prenda_seleccionada.nombre} deseas quitar? "))
                            tienda.quitar_producto_del_carrito(prenda_seleccionada, cantidad_a_quitar)
                        else:
                            print("Selección inválida.")
                    except ValueError:
                        print("Entrada inválida.")
                elif respuesta == 'f':
                    continuar_comprando = False
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

        except ValueError:
            print("Entrada inválida.")

    tienda.mostrar_carrito()
    tienda.procesar_pago()

if __name__ == "__main__":
    main()
