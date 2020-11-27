from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('orders',OrderView)

urlpatterns = [
    path('products/',ProductView.as_view(),name='product-list'),
    # path('orders/',OrderView.as_view(),name='order-list'),
    path('pt_orders/',ProductToOrderView.as_view(),name='to-order'),
    path('modify-order/<int:pk>/',UDOrderView.as_view()),
    path('',include(router.urls)),
]
