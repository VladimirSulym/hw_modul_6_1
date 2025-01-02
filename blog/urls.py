from django.urls import path
from . import views
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog_update/<int:pk>/", views.BlogUpdateView.as_view(), name="blog_update"),
]