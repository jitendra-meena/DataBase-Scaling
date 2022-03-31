from rest_framework import serializers
from core.models import Customer,CustomerSupport

class AddCustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields ='__all__'


class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerSupport

    fields ='__all__'
        