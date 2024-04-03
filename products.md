# Funcionalidades del Programa de Compras Online

## 1. Mostrar Categorías
    - Se muestran todas las categorías disponibles.
    - Opciones:
        1. Acceder a una categoría específica
            - Se muestran todos los productos de la categoría seleccionada.
            - Opciones:
                1. Agregar producto al carrito
                    - Se solicita la cantidad del producto a agregar.
                2. Retroceder al menú anterior
        2. Retroceder al menú principal

## 2. Menú Carrito
    - Opciones:
        1. Ver todo el carrito
            - Se muestra cada producto con su cantidad, precio unitario y precio total.
        2. Eliminar artículo
            - Se muestra cada producto con su cantidad.
            - Se elige el producto a eliminar y la cantidad a eliminar.
        3. Eliminar todo
            - Elimina todos los productos del carrito.
        4. Retroceder al menú principal

## 3. Pagar Compra
    - Opciones de pago:
        1. Pagar en efectivo
        2. Pagar con tarjeta
        3. Pagar con QR


# Clase PaymentMethod

La clase `PaymentMethod` es una clase base abstracta para los métodos de pago. Define la estructura que todas las clases de métodos de pago deben implementar.

## Métodos

1. `process_payment(monto)`: 
    - Procesa el pago según el monto dado.
    - Parámetros: 
        - `monto` (float): El monto total a pagar.
    - Retorna: 
        - float: El costo de los productos después de aplicar el método de pago.

# Clase CashPayment

La clase `CashPayment` representa un método de pago utilizando efectivo.

## Métodos

1. `process_payment(monto)`: 
    - Procesa el pago utilizando efectivo.
    - Parámetros: 
        - `monto` (float): El monto total a pagar.
    - Retorna: 
        - float: El costo de los productos sin ningún descuento.

# Clase CardPayment

La clase `CardPayment` representa un método de pago utilizando una tarjeta.

## Métodos

1. `process_payment(monto)`: 
    - Procesa el pago utilizando una tarjeta con un descuento del 30%.
    - Parámetros: 
        - `monto` (float): El monto total a pagar.
    - Retorna: 
        - float: El costo de los productos después de aplicar el descuento del 30%.

# Clase QRPayment

La clase `QRPayment` representa un método de pago utilizando un código QR.

## Métodos

1. `process_payment(monto)`: 
    - Procesa el pago utilizando un código QR con un descuento del 10%.
    - Parámetros: 
        - `monto` (float): El monto total a pagar.
    - Retorna: 
        - float: El costo de los productos después de aplicar el descuento del 10%.

# Función process_payment

La función `process_payment` procesa el pago utilizando el método de pago especificado.

## Parámetros

- `payment_method` (PaymentMethod): El objeto del método de pago.
- `total_amount` (float): El monto total a pagar.

## Retorna

- float: El costo de los productos después de aplicar el método de pago.

# Clase ShippingMethod

La clase `ShippingMethod` es una clase base abstracta para los métodos de envío. Define la estructura que todas las clases de métodos de envío deben implementar.

## Métodos

1. `calculate_shipping_cost(peso, distancia_desde_tienda)`: 
    - Calcula el costo de envío basado en el peso de los productos y la distancia desde la tienda.
    - Parámetros: 
        - `peso` (float): El peso de los productos a enviar.
        - `distancia_desde_tienda` (float): La distancia del destino desde la tienda.
    - Retorna: 
        - float: El costo de envío.

# Clase StandardShipping

La clase `StandardShipping` representa un método de envío estándar.

## Métodos

1. `calculate_shipping_cost(peso, distancia_desde_tienda)`: 
    - Calcula el costo de envío para el envío estándar.
    - Parámetros: 
        - `peso` (float): El peso de los productos a enviar.
        - `distancia_desde_tienda` (float): La distancia del destino desde la tienda.
    - Retorna: 
        - float: El costo de envío para el envío estándar.

# Clase ExpressShipping

La clase `ExpressShipping` representa un método de envío exprés.

## Métodos

1. `calculate_shipping_cost(peso, distancia_desde_tienda)`: 
    - Calcula el costo de envío para el envío exprés.
    - Parámetros: 
        - `peso` (float): El peso de los productos a enviar.
        - `distancia_desde_tienda` (float): La distancia del destino desde la tienda.
    - Retorna: 
        - float: El costo de envío para el envío exprés.

# Clase InStorePickup

La clase `InStorePickup` representa un método de envío de recogida en la tienda.

## Métodos

1. `calculate_shipping_cost(peso, distancia_desde_tienda)`: 
    - Calcula el costo de envío para la recogida en la tienda (siempre es 0).
    - Parámetros: 
        - `peso` (float): El peso de los productos a enviar.
        - `distancia_desde_tienda` (float): La distancia del destino desde la tienda.
    - Retorna: 
        - float: El costo de envío para la recogida en la tienda (siempre es 0).

# Función calculate_shipping

La función `calculate_shipping` calcula el costo de envío utilizando el método de envío especificado.

## Parámetros

- `shipping_method` (ShippingMethod): El objeto del método de envío.
- `weight` (float): El peso de los productos a enviar.
- `distance_from_store` (float): La distancia del destino desde la tienda.

## Retorna

- float: El costo de envío calculado.

# Clase Node

La clase `Node` representa un nodo en una lista enlazada. Contiene un dato y una referencia al siguiente nodo en la lista.

## Atributos

- `data` (any): Los datos almacenados en el nodo.
- `next_node` (Node): La referencia al siguiente nodo en la lista.

## Métodos

No hay métodos adicionales.

# Clase LinkedList

La clase `LinkedList` representa una lista enlazada. Contiene una secuencia de nodos que están conectados entre sí.

## Atributos

- `head` (Node): El primer nodo de la lista.
- `size` (int): El tamaño actual de la lista.

## Métodos

1. `is_empty()`:
    - Verifica si la lista está vacía.
    - Retorna: True si la lista está vacía, False de lo contrario.

2. `add_to_end(data)`:
    - Agrega un nuevo nodo al final de la lista con el dato proporcionado.
    - Parámetros:
        - `data` (any): Los datos a almacenar en el nuevo nodo.
    - Retorna: None.

3. `remove(data)`:
    - Elimina el primer nodo que contiene el dato especificado de la lista.
    - Parámetros:
        - `data` (any): Los datos del nodo a eliminar.
    - Retorna: None.

4. `print_list()`:
    - Imprime los datos de todos los nodos en la lista.
    - Retorna: None.

# Clase Category

La clase `Category` representa una categoría de productos en un inventario. Contiene un identificador de categoría, un nombre de categoría y una lista enlazada de productos.

## Atributos

- `category_id` (int): El identificador de la categoría.
- `category_name` (str): El nombre de la categoría.
- `products` (LinkedList): La lista enlazada de productos en esta categoría.

## Métodos

1. `modify_product_quantity(product_name, quantity)`:
    - Modifica la cantidad de un producto en la categoría.
    - Parámetros:
        - `product_name` (str): El nombre del producto cuya cantidad se modificará.
        - `quantity` (int): La cantidad a restar del producto existente.
    - Retorna: None.

# Clase Product

La clase `Product` representa un producto en un inventario. Contiene un identificador de producto, un nombre de producto, un precio de producto, una cantidad de producto y un peso de producto.

## Atributos

- `product_id` (int): El identificador del producto.
- `product_name` (str): El nombre del producto.
- `product_price` (float): El precio del producto.
- `product_quantity` (int): La cantidad de producto disponible.
- `product_weight` (float): El peso del producto.

## Métodos

No hay métodos adicionales.

# Clase Client

La clase `Client` representa un cliente en el sistema. Contiene información básica sobre el cliente, como su identificación, nombre, correo electrónico, contraseña, dirección y distancia desde la tienda.

## Atributos

- `client_id` (str): La identificación única del cliente.
- `client_name` (str): El nombre del cliente.
- `client_email` (str): El correo electrónico del cliente.
- `client_password` (str): La contraseña del cliente.
- `client_address` (str): La dirección del cliente.
- `client_distance_from_store` (float): La distancia del cliente desde la tienda.

## Métodos

No hay métodos adicionales.

# Clase Cart

La clase `Cart` representa el carrito de compras de un cliente. Contiene una lista enlazada de productos que el cliente ha agregado al carrito.

## Atributos

- `head` (Node): El primer nodo en la lista enlazada que representa el carrito.
  
## Métodos

1. `add_product(product, quantity)`:
    - Agrega un producto al carrito de compras.
    - Parámetros:
        - `product` (Product): El producto a agregar al carrito.
        - `quantity` (int): La cantidad del producto a agregar.
    - Retorna: None.

2. `calculate_totals()`:
    - Calcula el precio total y el peso total de todos los productos en el carrito.
    - Retorna: Una tupla con el precio total (float) y el peso total (float) de los productos en el carrito.

3. `view_cart()`:
    - Muestra los detalles del carrito de compras, incluidos los nombres de los productos, las cantidades, los precios individuales y el precio total.
    - Retorna: None.

4. `clear_cart()`:
    - Elimina todos los productos del carrito de compras.
    - Retorna: None.

5. `remove_product()`:
    - Permite al cliente eliminar productos específicos del carrito de compras o reducir la cantidad de productos.
    - Retorna: None.

6. `remove_entire_product(product)`:
    - Elimina completamente un producto específico del carrito de compras.
    - Parámetros:
        - `product` (Product): El producto a eliminar completamente del carrito.
    - Retorna: None.

# Clase Order

La clase `Order` representa una orden de compra realizada por un cliente. Contiene información sobre el cliente que realiza la orden, el carrito de compras asociado a la orden y detalles adicionales de la orden.

Esta clase será implementada en la próxima versión para el modo empleado, donde se podrán ver los pedidos de todos los clientes.

## Atributos

- `client` (Client): El cliente que realiza la orden.
- `cart` (Cart): El carrito de compras asociado a la orden.
- `order_id` (str): El identificador único de la orden.
- `order_status` (str): El estado actual de la orden.
- `order_details` (str): Detalles adicionales sobre la orden.

## Métodos

1. `place_order()`:
    - Coloca la orden de compra en el sistema.
    - Retorna: None.

2. `cancel_order()`:
    - Cancela la orden de compra.
    - Retorna: None.

# Clase Empleado

La clase `Empleado` representa a un empleado de la tienda.

## Atributos

- `employee_id` (int): El identificador único del empleado.
- `employee_name` (str): El nombre del empleado.
- `employee_role` (str): El rol o puesto del empleado.
- `categories` (LinkedList): Una lista enlazada que contiene las categorías administradas por el empleado.

## Métodos

1. `add_category(category)`: 
    - Agrega una categoría a la lista de categorías administradas por el empleado.
    - Parámetros:
        - `category` (Category): El objeto de categoría que se agregará.

2. `add_product_to_category(category_name, product)`: 
    - Agrega un producto a una categoría específica administrada por el empleado.
    - Parámetros:
        - `category_name` (str): El nombre de la categoría a la que pertenece el producto.
        - `product` (Product): El objeto de producto que se agregará a la categoría.

3. `find_category(category_id)`: 
    - Encuentra y devuelve un objeto de categoría basado en su ID.
    - Parámetros:
        - `category_id` (int): El ID de la categoría a encontrar.
    - Retorna:
        - `Category or None`: El objeto de categoría encontrado o None si no se encuentra.

# Función read_inventory

La función `read_inventory` lee los datos del inventario desde un archivo y crea objetos de categoría y producto correspondientes.

## Parámetros

- `file_path` (str): La ruta al archivo que contiene los datos del inventario.

## Retorna

- `LinkedList`: Una lista enlazada que contiene las categorías creadas a partir de los datos del inventario.

## Proceso

1. Se inicializa un objeto `Employee`.
2. Se abre el archivo especificado por `file_path` en modo lectura.
3. Por cada línea en el archivo:
    - Se eliminan los espacios en blanco al inicio y al final de la línea, y se divide en una lista de datos.
    - Se extraen los valores de ID de categoría, nombre de categoría, ID de producto, nombre de producto, precio, cantidad y peso del producto.
    - Se busca la categoría actual utilizando el ID de categoría.
    - Si la categoría no existe, se crea una nueva instancia de `Category` y se agrega al empleado.
    - Se crea un nuevo producto utilizando los datos extraídos y se agrega a la categoría actual.
4. Se retorna la lista enlazada que contiene las categorías.

# Función print_inventory

La función `print_inventory` imprime los detalles del inventario, incluyendo los nombres de las categorías, productos, precios y cantidades.

## Parámetros

- `categories` (LinkedList): Una lista enlazada que contiene las categorías a imprimir.

## Proceso

1. Se obtiene el nodo de la cabeza de la lista `categories`.
2. Mientras haya un nodo actual:
    - Se obtiene la categoría actual.
    - Se imprime el nombre de la categoría.
    - Se obtiene el nodo de la cabeza de la lista de productos de la categoría.
    - Mientras haya un nodo de producto actual:
        - Se obtiene el producto actual.
        - Se imprime el nombre del producto, el precio y la cantidad en stock.
        - Se avanza al siguiente nodo de producto.
    - Se avanza al siguiente nodo de categoría.

# Función employee_main

La función `employee_main` representa la función principal para el modo empleado.

## Retorna

- `LinkedList`: Una lista enlazada que contiene las categorías leídas desde el archivo de inventario.

## Proceso

1. Se inicializa un objeto `Employee`.
2. Se establecen los atributos `employee_id`, `employee_name` y `employee_role`.
3. Se lee el inventario del archivo "inventory.txt" utilizando la función `read_inventory`, y se almacenan las categorías en `categories`.
4. Se retorna la lista enlazada de categorías.

# Función client_main

La función `client_main` representa la función principal para el cliente. Permite al cliente navegar por las categorías de productos, administrar el carrito de compras, realizar el proceso de pago y salir de la tienda sin comprar.

## Proceso

1. Se limpia la pantalla.
2. Se crea un cliente y un carrito para el cliente.
3. Se establecen los atributos del cliente.
4. Se exporta el inventario utilizando la función `employee_main`.
5. Se muestra el menú principal y se espera la elección del cliente.
6. Dependiendo de la elección del cliente:
    - Se muestran las categorías disponibles.
    - Se accede a una categoría específica para mostrar los productos disponibles.
    - Se accede al menú del carrito para gestionar los productos en el carrito.
    - Se procede con el proceso de pago y salida de la tienda.
    
# Función show_main_menu

La función `show_main_menu` muestra el menú principal de la tienda.

## Proceso

1. Imprime un mensaje de bienvenida en mayúsculas.
2. Muestra las opciones disponibles en el menú principal.

# Función show_categories

La función `show_categories` muestra las categorías disponibles.

## Parámetros

- `categories` (LinkedList): Una lista enlazada que contiene las categorías a mostrar.

## Proceso

1. Se crea un conjunto `printed_categories` para evitar imprimir categorías duplicadas.
2. Por cada categoría en la lista de categorías:
    - Si la categoría no ha sido impresa previamente:
        - Imprime el ID y nombre de la categoría.

# Función access_category

La función `access_category` permite al usuario acceder a una categoría específica.

## Parámetros

- `categories` (LinkedList): Una lista enlazada que contiene todas las categorías disponibles.
- `client_cart`: Representa el carrito de compras del cliente.

## Proceso

1. Se solicita al usuario que ingrese el número de la categoría a la que desea acceder, o 0 para volver al menú principal.
2. Si se ingresa "0", la función retorna.
3. Si se ingresa un número válido:
    - Se busca la categoría correspondiente.
    - Si se encuentra la categoría, se muestra el listado de productos en esa categoría.
    - Si no se encuentra la categoría, se imprime un mensaje indicando que no se encontró la categoría.

# Función find_category_by_id

La función `find_category_by_id` busca una categoría por su ID en la lista de categorías.

## Parámetros

- `categories` (LinkedList): Una lista enlazada que contiene todas las categorías disponibles.
- `category_id` (int): El ID de la categoría a buscar.

## Retorna

- `Category` or `None`: Devuelve el objeto de categoría si se encuentra, de lo contrario, devuelve `None`.

# Función show_products_in_category

La función `show_products_in_category` muestra los productos en una categoría específica.

- `category` (Category): La categoría de la cual se mostrarán los productos.
- `client_cart`: Representa el carrito de compras del cliente.

## Proceso

1. Limpia la pantalla.
2. Imprime el encabezado de la categoría.
3. Por cada producto en la lista de productos de la categoría:
    - Imprime los detalles del producto, incluyendo ID, nombre, cantidad en stock y precio.
4. Maneja la selección de productos mediante la función `handle_product_selection`.

# Función handle_product_selection

La función `handle_product_selection` maneja la selección de productos por parte del usuario.

- `category` (Category): La categoría de la cual se seleccionarán los productos.
- `client_cart`: Representa el carrito de compras del cliente.

## Proceso

1. Mientras no se haya seleccionado una opción válida:
    - Solicita al usuario que ingrese el número del producto que desea agregar al carrito, o 0 para volver.
    - Si se ingresa "0", la función retorna.
    - Si se ingresa un número válido:
        - Se agrega el producto al carrito utilizando la función `add_product_to_cart`.

# Función print_product

La función `print_product` imprime los detalles de un producto.

- `product` (Product): El producto del cual se imprimirán los detalles.

## Proceso

1. Imprime el ID, nombre, precio y cantidad en stock del producto.

# Función add_product_to_cart

La función `add_product_to_cart` agrega un producto al carrito de compras del cliente.

- `category` (Category): La categoría a la cual pertenece el producto a agregar.
- `product_number` (int): El número de producto que se desea agregar al carrito.
- `client_cart`: Representa el carrito de compras del cliente.

## Proceso

1. Busca el producto seleccionado en la categoría.
2. Si se encuentra el producto:
    - Solicita al usuario que ingrese la cantidad que desea agregar al carrito.
    - Si la cantidad ingresada es válida y hay suficiente stock:
        - Agrega el producto al carrito del cliente.
        - Modifica la cantidad de stock en la categoría.

# Función show_cart_menu

La función `show_cart_menu` muestra el menú del carrito.

## Proceso

1. Imprime el encabezado del menú del carrito.
2. Muestra las opciones disponibles en el menú del carrito.

# Función exit_without_buying

La función `exit_without_buying` imprime un mensaje de despedida cuando el usuario elige salir sin comprar nada.

## Proceso

1. Imprime un mensaje de despedida y finaliza el programa.

# Función cart_menu

La función `cart_menu` representa el menú del carrito, donde el usuario puede ver, eliminar o limpiar el carrito.

## Parámetros

- `client_cart`: Representa el carrito de compras del cliente.

## Proceso

1. Mientras el usuario no seleccione la opción de volver al menú principal:
    - Limpia la pantalla.
    - Muestra el menú del carrito.
    - Solicita al usuario que ingrese su elección.
    - Según la elección del usuario:
        - Si selecciona '1', muestra el carrito.
        - Si selecciona '2', elimina un producto del carrito.
        - Si selecciona '3', limpia el carrito.
        - Si selecciona '0', sale del menú del carrito.

# Función print_category

La función `print_category` imprime los detalles de una categoría y sus productos.

## Parámetros

- `category` (Category): La categoría cuyos detalles se imprimirán.

## Proceso

1. Imprime el nombre de la categoría y una tabla de productos que incluye ID, nombre, cantidad en stock y precio de cada producto.

# Función checkout_menu

La función `checkout_menu` representa el menú de pago y envío para finalizar la compra.

## Parámetros

- `client`: El cliente que realiza la compra.
- `client_cart`: Representa el carrito de compras del cliente.

## Proceso

1. Calcula el monto total y el peso total de los productos en el carrito.
2. Muestra el contenido del carrito.
3. Mientras el usuario no seleccione la opción de volver al menú principal:
    - Muestra el menú de pago.
    - Solicita al usuario que seleccione un método de pago.
    - Procesa el pago y calcula el total con descuento.
    - Muestra el menú de envío.
    - Solicita al usuario que seleccione un método de envío.
    - Calcula el costo de envío.
    - Calcula el total con descuento y costo de envío.
4. Muestra un mensaje de despedida y finaliza el programa.

# Función clear_screen

La función `clear_screen` limpia la pantalla del terminal.

## Proceso

1. Limpia la pantalla según el sistema operativo utilizado.

# Función wait_for_key

La función `wait_for_key` espera a que el usuario presione la tecla Enter para continuar.

## Proceso

1. Solicita al usuario que presione Enter para continuar.

# Función farewell_message

La función `farewell_message` muestra un mensaje de despedida al usuario.

## Proceso

1. Imprime un mensaje de agradecimiento y finaliza el programa.
