from rest_framework import serializers
from core.models import Customer,CustomerSupport
from users.models import User, Company

class AddCustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields ='__all__'


class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerSupport

    fields ='__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Company

    fields ='__all__'        