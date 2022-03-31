from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AddCustomerSerializer,CustomerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Customer,CustomerSupport
import logging
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# TEST DataBase Scaling ...
class AddCustomer(APIView): 
  def get(self,request):
    customer = CustomerSupport.objects.all()
    serializer = AddCustomerSerializer(customer,many=True)
    logging.info("User Data Created")
    return Response(serializer.data) 
  
  def post(self, request):
    serializer = AddCustomerSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
      serializer.save() 
      return Response(serializer.data, status=status.HTTP_200_OK)
    logging.warning("Data Not Valid Error")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add Multiples users in same time using this api
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


