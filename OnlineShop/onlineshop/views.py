from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['price','name']

    # def get(self,*args,**kwargs):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products,many=True)
    #     filter_backends = (DjangoFilterBackend)
    #     filterset_fields = ['name','price']
    #     return Response(serializer.data,status=status.HTTP_200_OK)

    # def post(self,request,*args,**kwargs):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]

    # def get(self,*args,**kwargs):
    #     orders = Order.objects.all()
    #     serializer = OrderSerializer(orders,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    #
    # def post(self,request,*args,**kwargs):
    #     serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)


class UDOrderView(APIView):
    def put(self,request,*args,**kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'success'})

    def delete(self,request,*args,**kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.delete()
        return Response({'data':'success'})


class ProductToOrderView(APIView):
    def get(self,*args,**kwargs):
        orders = ProductToOrder.objects.all()
        serializer = ProductToOrderSerializer(orders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer = ProductToOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)