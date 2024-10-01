class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == None:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        valid_order = False
        if flavor in self.flavors and 1 <= scoops <= 3:
            print("Order Created!")
            valid_order = True
        elif flavor in self.flavors and not 1 <= scoops <= 3:
            print("Choose between 1-3 scoops")
        elif flavor not in self.flavors and 1 <= scoops <= 3:
            print("Sorry, we don't have that flavor")
        else:
            print("Incrrect flavor and scoops")
          
        if valid_order:
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders.items:
            print(f"Customer: {order["customer"]} -- Flavor: {order["flavor"]} -- Scoops: {order["scoops"]}")
       
    def next_order(self):
        print("\nNext Order Up!")
        next_order = self.orders.dequeue()
        print(f"Customer: {next_order["customer"]} -- Flavor: {next_order["flavor"]} -- Scoops: {next_order["scoops"]}")

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
