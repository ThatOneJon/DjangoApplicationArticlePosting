from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_view, name="register_view"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('new_Post/', views.new_Post, name= "new_Post"),
    path('<int:id>/', views.one_Article, name= "one_Article"),
    path('edit/<int:id>', views.edit, name= "edit"),
    path('profile/<int:id>', views.profile, name= "profile"),

]
