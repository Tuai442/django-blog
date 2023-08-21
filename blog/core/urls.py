from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  # Import this to serve media files in development

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:category_id>", views.home, name="home"),  

    path("add_recipe", views.add_recipe, name="add_recipe"),  
    path("recipe_details", views.recipe_details, name="recipe_details"),  

    path("login/", views.login_page, name="login"),
    path("registration/", views.registration_page, name="registration"),
    path("logout/", views.logout_page, name="logout"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
