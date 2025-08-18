#  Sistema de Gestión de Inventarios de Productos de una Tienda.

# La Clase Producto representa un artículo en el inventario.
class Producto:
    def __init__(self, nombre, precio, cantidad):# crear un constructor con los tres atributos.
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

# Crear  una clase que gestiona el inventario de productos.
class Inventario:
    def __init__(self): # Crear constructor que inicializa la lista de productos.
        self.productos = []  # Usar productos.

# Agregar productos al inventario.
    def agregar_producto(self, producto): # Recibe un objeto de la clase producto y lo añade a la lista productos.
        self.productos.append(producto)

# crear el metodo para mostrar todos los productos en el inventario.
    def mostrar_productos(self): # Recorre la lista de productos y muestra en la consola los detalles de cada uno.
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")

# Crear instancias de productos
producto1 = Producto("Avena Tradicional", 2.50, 10)
producto2 = Producto("Avena Quinua", 3.00, 5)
producto3 = Producto("Arros cevada", 1.00, 10)
producto4 = Producto("Aceite Vegetal",3.50, 10)
producto5 = Producto("Sardina Real", 1.80, 25)
producto6 = Producto("Sal", 1.00, 100)
producto7 = Producto("Azucar Morena", 2.00, 150)
producto8 = Producto("Atún", 2.00, 90)

# Crear una instancia de inventario.
mi_inventario = Inventario()

# Agregar productos al inventario
mi_inventario.agregar_producto(producto1)
mi_inventario.agregar_producto(producto2)
mi_inventario.agregar_producto(producto3)
mi_inventario.agregar_producto(producto4)
mi_inventario.agregar_producto(producto5)
mi_inventario.agregar_producto(producto6)
mi_inventario.agregar_producto(producto7)
mi_inventario.agregar_producto(producto8)

# Mostrar los productos en el inventario.
mi_inventario.mostrar_productos()

# Crear una lista de productos.
lista_producto = ["Avena Tradicional","Avena Quinua","Arroz Cevada","Aceite Vegetal","Sardina Real","Sal","Azúcar Morena","Atún"]

#Obtener productos de la (lista_producto) y imprimir.
print(lista_producto[0])
print(lista_producto[2])
print(lista_producto[3])
print(lista_producto[4])
print(lista_producto[5])
print(lista_producto[6])
print(lista_producto[7])

# Borrar mediante su indice , Avena Tradicional,Aceite Vegetal, sal, Atún.
lista_producta = ["Avena Tradicional","Avena Quinua","Arroz Cevada","Aceite Vegetal","Sardina Real","Sal","Azucar Morena","Atún"]
del lista_producto[0]
del lista_producto[2]
del lista_producto[3]
del lista_producto[4]

# Imprimir los productos de la lista existente.
for producto in lista_producto:
    print(f"producto:{producto}")







































