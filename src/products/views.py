from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError, ValidationError
from .models import Product
from .serializers import ProductSerializer
from .baseresponse import BaseResponse

@api_view(['GET'])
def getProducts(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    # raise ParseError
    return BaseResponse(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return BaseResponse(serializer.data)