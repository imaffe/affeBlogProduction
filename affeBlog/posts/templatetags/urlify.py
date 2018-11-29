try:
    from urllib import quote_plus #python 2
except :

    pass
## TODO what is the suggested way of using except
## TODO what is this module used for?
try:
    from urllib.parse import quote_plus #python 3
except :
    pass


from django import template

register = template.Library()

@register.filter
def urlify(value):
    return quote_plus(value)