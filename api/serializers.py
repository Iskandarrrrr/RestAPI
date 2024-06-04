from rest_framework import serializers
from my_app.models import User, Client


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('FirstName', 'LastName', 'UserName', 'CreatedAt')  # Soralgan sorov boyicha berilvoti


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = ('FirstName', 'LastName', 'CarModel', 'CarNumber', 'PhoneNumber', 'CreatedUserId')

