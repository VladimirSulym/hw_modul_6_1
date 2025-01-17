from django.urls import path
from . import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("registr_user/", views.RegistrUserView.as_view(), name="registr_user"),
    path("update_user//<int:pk>/", views.UpdateUserView.as_view(), name="update_user"),
]
