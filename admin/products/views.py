from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import random

from .models import Product, User
from .serializers import ProductSerializer, UserSerializer
from .producer import publish

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        '''GET /api/products'''
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        '''POST /api/products'''
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # publish to rabbit mq
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): 
        '''GET /api/products/<str: id>'''
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): 
        '''PUT /api/products/<str: id>'''
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # publish to rabbit mq
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): 
        '''DELETE /api/products/<str: id>'''
        product = Product.objects.get(id=pk)
        product.delete()
        # publish to rabbit mq
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return Response({'id': user.id})
    
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)



