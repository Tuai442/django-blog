from django.urls import path
from . import views

urlpatterns = [
    path('recepi-liked-toggle',  views.toggleLike, name="toggle-like"),
    # path('rooms/', views.getRooms),
    # path('rooms/<str:pk>/', views.getRoom),
]
