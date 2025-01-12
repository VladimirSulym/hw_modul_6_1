from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.CatalogView.as_view(), name="catalog"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", views.ProductInfoView.as_view(), name="product"),
    path("add_product/", views.AddProductView.as_view(), name="add_product"),
    path("add_success/", views.AddSuccessView.as_view(), name="add_success"),
]