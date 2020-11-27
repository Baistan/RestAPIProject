from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ['id','endpoint']


class ProductToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductToOrder
        fields = ['id','products','order']

class OrderSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    endpoint = EndpointSerializer(many=True)
    to_order = ProductToOrderSerializer(many=True,read_only=True)
    # total_price = serializers.SerializerMethodField('get_total_price')
    class Meta:
        model = Order
        fields = ['id','to_order','start_date','end_date','status','endpoint','account']

    def create(self, validated_data):
        endpoints = validated_data.pop('endpoint')
        order = Order.objects.create(**validated_data)
        for endpoint in endpoints:
            Adress.objects.create(order=order,**endpoint)
        return order

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status',instance.status)
        endpoints = validated_data.pop('endpoint')
        for endpoint in endpoints:
            Adress.objects.update(**endpoint)
            if endpoint not in endpoints:
                endpoint.delete()
        instance.save()
        return instance



    # def get_total_price(self,to_representation):
    #     orders = ProductToOrder.objects.all()
    #     total_price = 0
    #     for order in orders:
    #         total_price = order.products.price
    #     return total_price


    # def validate(self,attrs):
    #     start_date = self.validated_data['start_date']
    #     end_date = self.validated_data['end_date']
    #     if start_date > end_date:
    #         raise ValidationError('Incorrect dates')

