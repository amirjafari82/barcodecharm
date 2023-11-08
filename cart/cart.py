from django.conf import settings
from decimal import Decimal
from products.models import Product

class Cart(object):
    
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self,product,color,override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'color': []}
            
        if self.cart[product_id]['color'] == []:
            self.cart[product_id] = {'color': [color],'price':str(product.price),'quantity':0}
        else:
            self.cart[product_id]['color'].append(color)
            
        if override_quantity:
            self.cart[product_id]['quantity'] = 1
        else:
            self.cart[product_id]['quantity'] += 1
                
        self.save()
        
    def save(self):
        self.session.modified = True
        
    def remove(self,product):
        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids).values()
        
        cart = self.cart.copy()
        for product in products:
            cart[str(product['id'])]['product_id'] = product['id']
        
        cart = self.cart.copy()
            
        for item in cart.values():
            item['price'] = item['price'].replace(',','')
            item['total_price'] = int(item['price']) * len(item['color'])
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
            
    def get_total_price(self):
        return sum(Decimal(int(item['price']) * item['quantity']) for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()