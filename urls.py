from django.urls import path
from .views import BolimView, ClientView, Clients_updateView, ProductView, Product_updateView, LogoutView
urlpatterns = [
    path('bolim/', BolimView.as_view(), name='bolim'),
    path('client/', ClientView.as_view(), name='clients'),
    path('client_update/', Clients_updateView.as_view(), name='client_update'),
    path('product/', ProductView.as_view(), name='goods'),
    path('product_update/<int:son>/', Product_updateView.as_view(), name='product-update'),
    path('logout/', LogoutView.as_view(), name='logout'),
]