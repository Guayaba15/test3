# myapp/urls.py
from django.urls import path
from .views import login_view, home, item_create, item_update, item_delete, logout_view, register_view

urlpatterns = [
    path('', home, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home, name='home'),
    path('item/create/', item_create, name='item_create'),
    path('item/<int:item_id>/update/', item_update, name='item_update'),
    path('item/<int:item_id>/delete/', item_delete, name='item_delete'),
    path('logout/', logout_view, name='logout'),
]
