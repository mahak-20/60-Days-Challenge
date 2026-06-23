class User:
    def __init__(self, user_id, name, address):
        self.user_id = user_id
        self.name = name
        self.address = address
class Restaurant:
    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.orders = []
    def receive_order(self, order):
        self.orders.append(order)
        print(f"{self.name} received Order #{order.order_id}")

class DeliveryPartner:
    def __init__(self, partner_id, name):
        self.partner_id = partner_id
        self.name = name
    def deliver_order(self, order):
        order.status = "Delivered"
        print(f"Order #{order.order_id} delivered by {self.name}")

class Order:
    def __init__(self, order_id, user, restaurant, items):
        self.order_id = order_id
        self.user = user
        self.restaurant = restaurant
        self.items = items
        self.status = "Placed"
class FoodDeliverySystem:
    def __init__(self):
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        order.restaurant.receive_order(order)
        print("Order placed successfully.")
    def prepare_order(self, order):
        order.status = "Preparing"
        print(f"Order #{order.order_id} is being prepared")

    def assign_delivery(self, order, partner):
        order.status = "Out for Delivery"
        print(f"{partner.name} assigned to Order #{order.order_id}")
        partner.deliver_order(order)
customer = User(1, "Mahak", "Meerut")
restaurant = Restaurant(101, "Pizza Palace")
partner = DeliveryPartner(201, "Rahul")
order = Order(
    1001, 
    customer,
    restaurant,
    ["Margherita Pizza", "Garlic Bread"]
)
system = FoodDeliverySystem()
system.place_order(order)
system.prepare_order(order)
system.assign_delivery(order, partner)
print("Final Status:", order.status)