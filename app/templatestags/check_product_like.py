from django import template

from app.models import ProductLike

register = template.Library()



def check_like(product, user):
    return ProductLike.objects.filter(product=product, user=user).exists()
register.filter(check_like)