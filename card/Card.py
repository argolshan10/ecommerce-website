from core.models import product , Profile

class Card:
    def __init__(self, request):
        self.session = request.session
        # get request
        self.request = request
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.card = cart

    def add(self, product , quantity):
        product_qty = str(quantity)
        product_id = str(product.id)
        if product_id in self.card :
            pass 
        else :
            self.card[product_id] = int(product_qty)
            
        self.session.modified = True
        # deal with logged in user
        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id= self.request.user.id)
            carty = str(self.card)
            carty = carty.replace("\'" , "\"")
            # save carty to the profile model
            current_user.update(old_cart= str(carty))

    def totals(self):
            # Get product IDS
            product_ids = self.card.keys()
            # lookup those keys in our products database model
            products = product.objects.filter(id__in=product_ids)
            # Get quantities
            quantities = self.card
            # Start counting at 0
            cart_total = 0

            for key, value in quantities.items():
                # Convert key string  into so we can do math
                key = int(key)
                for item in products:
                    if item.id == key:
                        if item.is_sale:
                            cart_total = cart_total + (item.sale_price * value)
                        else:
                            cart_total = cart_total + (item.price * value)

            return cart_total

    def __len__(self):
        return len(self.card)
    
    def get_prods(self):
        # get ids from cart
        product_ids = self.card.keys()
        
        products = product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.card
        return quantities

    def update(self , our_product , quantity):
        product_id = str(our_product)
        product_qty = int(quantity)

        our_cart = self.card
        our_cart[product_id] = product_qty

        self.session.modified = True

        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.card)
            carty = carty.replace("\'", "\"")
            # save carty to the profile model
            current_user.update(old_cart=str(carty))

        sth = self.card
        return sth
    def delete(self , product):
        product_id = str(product)

        if product_id in self.card:
            del self.card[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id= self.request.user.id)
            carty = str(self.card)
            carty = carty.replace("\'" , "\"")
            # save carty to the profile model
            current_user.update(old_cart= str(carty))

    def db_add(self, product, quantity):
        product_qty = str(quantity)
        product_id = str(product)
        if product_id in self.card:
            pass
        else:
            self.card[product_id] = int(product_qty)

        self.session.modified = True
        # deal with logged in user
        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.card)
            carty = carty.replace("\'", "\"")
            # save carty to the profile model
            current_user.update(old_cart=str(carty))