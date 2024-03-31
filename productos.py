class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  # Añadir un atributo para registrar el tamaño de la lista

    def is_empty(self):
        return self.head is None

    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1  # Incrementar el tamaño de la lista

    def add_to_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1  # Incrementar el tamaño de la lista

    def remove(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
            self.size -= 1  # Decrementar el tamaño de la lista

    def print_list(self):
        current = self.head
        if not current:
            print("The cart is empty")
        else:
            print("Cart content:")
            counter = 1
            while current:
                print(f"{counter}. {current.data}")
                current = current.next
                counter += 1


class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
        self.category_description = None
        self.products = LinkedList()

class Product(Category):
    def __init__(self):
        super().__init__()
        self.product_id = None
        self.product_name = None
        self.product_price = None
        self.product_stock = None
        self.product_rating = None
        self.product_comment = None

class Client:
    def __init__(self):
        self.client_id = None
        self.client_name = None
        self.client_ruc = None
        self.client_email = None
        self.client_password = None
        self.client_address = None

    def login(self):
        pass

    def pay(self):
        pass

class Cart(LinkedList):
    def __init__(self):
        super().__init__()

    def add_to_cart(self, data):
        self.add_to_end(data)

    def remove_from_cart(self, data):
        self.remove(data)

    def view_cart(self):
        self.print_list()

class Order(Client):
    def __init__(self):
        super().__init__()
        self.order_id = None
        self.order_status = None
        self.order_details = None

    def place_order(self):
        pass

    def cancel_order(self):
        pass

class Employee:
    def __init__(self):
        self.employee_id = None
        self.employee_name = None
        self.employee_role = None
        self.categories = LinkedList()

    def add_category(self, category):
        self.categories.add_to_end(category)

    def add_product_to_category(self, category_name, product):
        current_category = self.find_category(category_name)
        if current_category:
            current_category.products.add_to_end(product)

    def find_category(self, index):
        current_index = 0
        current = self.categories.head
        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1
        return None

if __name__ == "__main__":
    # Crear un empleado
    employee = Employee()
    employee.employee_id = 1
    employee.employee_name = "John Doe"
    employee.employee_role = "Clerk"

    # Leer el archivo de inventario
    with open("inventory.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            category_id = int(data[0])
            category_name = data[1]
            product_name = data[2]
            product_description = " ".join(data[3:-1])
            product_price = float(data[-1])
            
            current_category = employee.find_category(category_name)
            if not current_category:
                current_category = Category(category_id, category_name)
                employee.add_category(current_category)
            
            product_info = f"{product_name}: {product_description}, ${product_price:.2f}"  # Concatenar nombre, descripción y precio
            current_category.products.add_to_end(product_info)

    # Crear un cliente
    client = Client()
    client.client_id = 1
    client.client_name = "Alice"
    client.client_email = "alice@example.com"
    client.client_password = "password123"

# Función para mostrar el menú principal
def show_main_menu():
    print("\n╔════════════════════════════════════╗")
    print("║        Welcome to the store!       ║")
    print("║                                    ║")
    print("║            Main Menu:              ║")
    print("║   1. Show categories               ║")
    print("║   2. Cart menu                     ║")
    print("║   3. Checkout                      ║")
    print("║   4. Exit without buying           ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")


# Función para mostrar las categorías disponibles
# falta arreglar porque milena no hizo nada, solo puso el texto aesthetic
def show_categories():
    print("\n╔══════════════════════════════════════════════════╗")
    print("║             Available Categories                 ║")
    print("╠══════════════════════════════════════════════════╣")
    current_category = employee.categories.head
    while current_category:
        print(f"║ {current_category.data.category_id}. {current_category.data.category_name.ljust(40)}      ║")
        current_category = current_category.next
    print("╚══════════════════════════════════════════════════╝")

# Función para seleccionar una categoría y ver sus productos
def select_category():
    selected_category_id = int(input("Select a category: "))
    selected_category = employee.find_category(selected_category_id)
    if selected_category:
        print(f"\nProducts in {selected_category.category_name}:")
        selected_category.products.print_list()
        return selected_category
    else:
        print("Invalid category selected.")
        return None

# Función para el menú del carrito
def show_cart_menu():
    print("\n╔════════════════════════════════════════╗")
    print("║               Cart Menu                 ║")
    print("╠════════════════════════════════════════╣")
    print("║   1. View Cart                          ║")
    print("║   2. Remove Item                        ║")
    print("║   3. Clear Cart                         ║")
    print("║   4. Back                               ║")
    print("╚════════════════════════════════════════╝")


# Función para mostrar el carrito
def view_cart(cart):
    print("\nCart contents:")
    cart.view_cart()

# Función para eliminar un artículo del carrito
def remove_item_from_cart(cart):
    item_to_remove = input("Enter the product to remove: ")
    cart.remove_from_cart(item_to_remove)

# Función para limpiar el carrito
def clear_cart(cart):
    cart.clear()

# Función para realizar el pago
def checkout():
    print("\nCheckout options:")
    # Opciones de pago aquí

# Función principal del cliente
def client_main():
    client_cart = Cart()  # Instanciar un carrito para el cliente

    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            show_categories()
            selected_category = select_category()
            if selected_category:
                # Aquí iría la lógica para agregar productos al carrito
                pass

        elif choice == "2":
            show_cart_menu()
            cart_choice = input("Enter your choice: ")
            if cart_choice == "a":
                view_cart(client_cart)
            elif cart_choice == "b":
                remove_item_from_cart(client_cart)
            elif cart_choice == "c":
                clear_cart(client_cart)

        elif choice == "3":
            checkout()

        elif choice == "4":
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Please try again.")

# Llamada a la función principal del cliente
if __name__ == "__main__":
    client_main()

