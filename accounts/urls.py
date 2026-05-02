from django.urls import path
from accounts.views import activate_email, login_page, register_page, cart, add_to_cart, remove_from_cart

urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/', cart , name="cart"),
   path('add_to_cart/<uid>/', add_to_cart , name="add_to_cart"),
   path('remove_from_cart/<cart_item_uid>/', remove_from_cart , name="remove_from_cart"),
]