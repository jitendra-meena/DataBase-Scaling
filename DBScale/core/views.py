from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AddCustomerSerializer,CustomerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Customer,CustomerSupport

class AddCustomer(APIView): 
  def get(self,request):
    customer = CustomerSupport.objects.using('replica').all()
    serializer = AddCustomerSerializer(customer,many=True)
    return Response(serializer.data) 
  
  def post(self, request):
    serializer = AddCustomerSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
      serializer.save()
      
      print("DataBase Scaling",serializer)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Customer(ListCreateAPIView):
  queryset = CustomerSupport.objects.all()
  serializer_class = CustomerSerializer
  def post(self, request, *args, **kwargs):
    name = request.data.get('name')
    address = request.data.get('address')
    city = request.data.get('city')
    customer = CustomerSupport.objects.using('replica').create(name=name, address=address, city=city)
    print("DataBase Scaling")
    customer.save()
    customers = CustomerSupport.objects.all()  
    serializer = CustomerSerializer(customers,many=True)
    return Response({'msg':'Custom List','data':serializer.data})   


