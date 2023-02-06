#item1 = 'Phone'
#item1_price = 100
#item1_quantity = 5
#item1_price_total = item1_price *item1_quantity

#print(type(item1))

class Item:
    pay_rate = 0.8 # The Pay rate after 20% Discount
    all = []

    def __init__(Book,name,price,quantity):
        print(f"Create From {name} using __iniy__ Method") #Check for print all the names of items first

        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not Grater Than Zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal zero! "

        # Assign Values to Book Object
        Book.name = name
        Book.price = price
        Book.quantitiy = quantity
        Book.totalOfPrice = Book.calculate_total_price(Book.price,Book.quantitiy)

        # Action to execute
        Item.all.append(Book)

    def calculate_total_price(self, x, y):
        return x * y

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantitiy}')"


item1 = Item("Phone",100,5)
item2 = Item("Laptop",75,10)
item3 = Item("Cable",10,5)
item4 = Item("Mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

item2.pay_rate = 0.7

#print(item1.pay_rate)
#print(Item.pay_rate)
# print(item2.pay_rate)

print(type(item1.price))
print(item1.name.upper())
print(item1.totalOfPrice)

print("Total of Item2 : ",item2.totalOfPrice)

print(Item.__dict__) # All the attributes for Class level
print(item1.__dict__) # All the attributes for instance Level

item1.apply_discount()
print(item1.price)

item2.apply_discount()
print(item2.price)

print(Item.all)

for instance in Item.all:
    print(instance.name)