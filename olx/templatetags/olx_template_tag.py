from django import template
from olx.models import Product
register = template.Library()
@register.inclusion_tag('prod.html')
def get_category_list(prod = None):
    return {'prod':Product.objects.filter(is_sold=False),'sell_prod':prod}