class Binary_Tree:

    def __init__(self, product_code=None, name=None, price=None):
        self.left = None
        self.right = None
        self.product_code=product_code
        self.name=name
        self.price=price

    def put_elements(self, product_code, name, price):
    """ puts information about products into a tree and sorting it by product_code """

        if not isinstance(product_code,int) or not isinstance(price,float) and not isinstance(price,int):
                raise TypeError
        if price<0 or product_code<0:
            raise RuntimeError
        if self.product_code:
            if product_code < self.product_code:
                if self.left is None:
                    self.left = Binary_Tree(product_code, name, price)
                else:
                    self.left.put_elements(product_code, name, price)
            elif product_code > self.product_code:
                if self.right is None:
                    self.right = Binary_Tree(product_code, name, price)
                else:
                    self.right.put_elements(product_code, name, price)
        else:
            self.product_code=product_code
            self.name=name
            self.price=price

    def search_elements(self,product_code,quantity):
    """ returns the product that was searched by product_code """

        if not isinstance(product_code,int) or not isinstance(quantity,int):
                raise TypeError
        if quantity<0 or product_code<0:
            raise RuntimeError
        if product_code==self.product_code:
            return self.name+': '+str(quantity)+" of them="+str(self.price*quantity)
        elif product_code < self.product_code:
            if self.left is not None:
                return self.left.search_elements(product_code,quantity)
            else:
                return "there isn't product with this code"
        elif product_code > self.product_code:
            if self.right is not None:
                return self.right.search_elements(product_code,quantity)
            else:
                return "there isn't product with this code"
            

order = Binary_Tree()
order.put_elements(6,"apples",3.12)
order.put_elements(14,"meat",20)
order.put_elements(3,"boots",45.75)
order.put_elements(7,"banana",3.2)
order.put_elements(9,"phone",125.89)
print(order.search_elements(14,20))