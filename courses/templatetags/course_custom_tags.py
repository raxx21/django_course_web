from django import template
import math
register = template.Library()

# Calculation of the sell price adding discount
#  formula sellprice = mrp - (mrp * discount * 0.01)
# It is a simple tag that is a template tags which can take two or more perameters 
@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount is 0:
        return price
    sellprice = price - (price * discount * 0.01)
    return math.floor(sellprice)

@register.filter
def rupee(price):
    return f'₹{price}'