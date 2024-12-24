from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("contacts/", views.contacts, name="contacts"),
    path("product/<int:product_id>/", views.product_info, name="product"),
    path("add_product/", views.add_product, name="add_product"),
]