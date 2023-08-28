class Store:
    def __init__ (self,name):
        self.name = name
        self.list_products = []

    def add_product(self, new_product):
        self.list_products.append(new_product)
    
    def sell_product(self, id):
        self.list_products.pop(id)
        print(f"")
    
    def inflation(self, percent_increase) :
        for product in self.list_products:
            product.price += product.price * (percent_increase / 100)
    
    def set_clearance(self, category, percent_discount):
        for product in self.list_products:
            if product.category == category:
                product.price -= product.price*(percent_discount / 100)




class Product:
    def __init__ (self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


    def update_price(self, percent_change, is_increased) :
        if Product.update_price(self.price, is_increased):
            self.price += self.price * (percent_change / 100)
            return True
        else:
            self.price -= self.price * (percent_change / 100)
            return False
    
    def print_info(self):
        print (f"Product: {self.name}, Category: {self.category},Price: {self.price}")
    

    Product1 = Product("Phone", 1500,"Samsung")
    Product2 = Product("Earbuds",700, "Oppo")
    Store.add_product(Product1)
    Store.add_product(Product2)
  
