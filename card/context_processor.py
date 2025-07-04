from .Card import Card     

# create context processors so the cart works on all pages 

def card(request) : 
    # return default data from cart 
    return {'card' : Card(request)} 
