class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
            yield from self.slots

    def inventory_value(self):
        total_value = 0
        for item in self.slots:
            total_value += (item.quantity * item.price)
        print(total_value)
        return total_value

class Item:
    def __init__(self, name, price, id, quantity):
        self.name = name
        self.price = price
        self.id = id
        self.quantity = quantity

    def __repr__(self):
        return '{}: {} pieces.'.format(self.name, self.quantity)

#create a product instance
def add_item():
    item = Item(input('Product name: '), float(input('Product price: ')), input('Product ID: '), int(input('Product Quantity: ')))
    print('{} has been added!'.format(item))
    return item

#main program
def main():
    print("This is Mark's Inventory List")
    print("Type 'DONE' if you want to quit")
    print("Type 'SHOW' if you want to see your inventory list")
    print("Type 'VALUE' if you want to see inventory's total value")
    print("Type 'ADD' if you want to add an item")

    inventory = Inventory()

    while True:
        user_input = input('> ')
        if user_input.upper() == 'ADD':
            inventory.add(add_item()) #create a product instance and add directly to inventory
            continue

        elif user_input.upper() == 'SHOW':
            for item in inventory:
                print(item)
            continue

        elif user_input.upper() == 'DONE':
            break

        elif user_input.upper() == 'VALUE':
            inventory.inventory_value()


main()
