from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),

	path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    
	path("profile/<str:id>", views.profile, name="profile"),
	path("edit/<str:id>", views.edit, name="edit"),
	path("update/<str:id>",views.update,name="update"),

	path("contact",views.contact,name="contact"),

	path("details/<str:id>",views.details,name="details"),
	path("d_details",views.d_details,name="d_details"),

	path("category",views.category,name="category"),
	path("adidas",views.adidas,name="adidas"),
	path("nike",views.nike,name="nike"),
	path("puma",views.puma,name="puma"),
	path("fila",views.fila,name="fila"),

	path("cart/<str:id>/<str:pk>",views.cart,name="cart"),
	path("showcart/<str:id>",views.showcart,name="showcart"),
	path("clearcart/<str:id>",views.clearcart,name="clearcart"),

	path("checkout/<str:id>",views.checkout,name="checkout"),
	path("shipping_address/<str:pk>",views.shipping_address,name="shipping_address"),
	path("confirmation/<str:id>",views.confirmation,name="confirmation"),

	path("gmail",views.gmail,name="gmail"),
	path("gmail1",views.gmail1,name="gmail1"),

]







