from django.urls import path
from nowandthen import views

app_name = 'nowandthen'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('add_picture/', views.add_picture, name="add_picture"),
    path('search/', views.search_results, name='search_results'),
    path('photos/', views.search_results, name='photos'),
]