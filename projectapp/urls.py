from django.urls import path
from projectapp import views

urlpatterns = [
    path('show/', views.show, name='show'),
    path('', views.front, name='home'),  # Home page
    path('msg/', views.msg, name='page'),  # Main page with books
    path('signup/', views.signup_view, name='signup'),  # Signup
    path('login/', views.login_view, name='login'),  # Login
    path('logout/', views.logout_views, name='logout'),  # Logout

    # Cart operations
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout')
]

