from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *



class AccountRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ['username','name','last_name','email','password','password2']

    def save(self,**kwargs):
        account = Account(username=self.validated_data['username'],
                          email=self.validated_data['email'],
                          name=self.validated_data['name'],
                          last_name=self.validated_data['last_name'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise ValidationError('Passwords dont match')

        account.set_password(password)
        account.save()
        return account



