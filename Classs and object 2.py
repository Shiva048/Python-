#Classes and Objects - (Amazon Card)
class Card:
    def __init__(self, id, imageUrl, deviceType, price, rating):
        self.id = id
        self.imageUrl = imageUrl
        self.deviceType = deviceType
        self.price = price
        self.rating = rating

def productdetails(self):
    print("Product -", self.id, ":")
    print("imageUrl:", self.imageUrl)
    print("deviceType:", self.deviceType)
    print("price:", self.price)
    print("rating:", self.rating)
    


product1 = Card(id=1, imageUrl="Dummy-url 1", deviceType="Mobile", price=56000, rating=4.5)
product2 = Card(id=2, imageUrl="Dummy-url 2", deviceType="Laptop", price=94000, rating=4.8)
product3 = Card(id=3, imageUrl="Dummy-url 3", deviceType="Smart-watch", price=18000, rating=3.5)


productdetails(product1)
print()
productdetails(product2)
print()
productdetails(product3
