from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def catalog_get_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'catalog'
    catalog = cache.get(key)
    if catalog is not None:
        return catalog
    catalog = Product.objects.all()
    cache.set(key, catalog, 60 * 60)  # Cache for 1 hour
    return catalog

def catalog_filter(products, filters):
    if filters == 'Все категории':
        return products.filter(is_active=True)
    return products.filter(is_active=True, category=Category.objects.get(name=filters))
