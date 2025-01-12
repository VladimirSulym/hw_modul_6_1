from django.urls import path
from . import views
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog_update/<int:pk>/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("add_blog/", views.BlogCreateView.as_view(), name="add_blog"),
    path("add_blog_success/", views.AddBlogSuccessView.as_view(), name="add_blog_success"),
    path("blog/<int:pk>/delete", views.BlogDeleteView.as_view(), name="blog_delete"),
]