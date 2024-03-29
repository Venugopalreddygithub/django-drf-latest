from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response 
from products.serializer import WriteProductSerializer, ReadProductSerializer 
from django.utils.text import slugify

# Create your views here.
class CreateProductView(APIView):
    
    def post(self, request):
        request_data = request.data 
        request_data.update({'slug': slugify(request_data.get('name'))})
        serializer = WriteProductSerializer(data=request_data)
        print("serializer:::::::::::", serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            product_instance = serializer.save()
            response_data = ReadProductSerializer(instance=product_instance).data 
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            print("error:::::::", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)