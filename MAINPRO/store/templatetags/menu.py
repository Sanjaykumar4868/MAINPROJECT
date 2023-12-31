from django import template
from store.models import Category
register = template.Library()

@register.inclusion_tag('App/menu.html')
def menu():
    categories = Category.objects.all()
    return {'categories':categories}