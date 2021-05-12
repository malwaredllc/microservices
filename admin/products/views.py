from django.shortcuts import render
from django import viewsets

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        '''GET /api/products'''
        pass

    def create(self, request):
        '''POST /api/products'''
        pass

    def retrieve(self, request, pk=None): 
        '''GET /api/products/<str: id>'''
        pass 

    def update(self, request, pk=None): 
        '''PUT /api/products/<str: id>'''
        pass 

    def destroy(self, request, pk=None): 
        '''DELETE /api/products/<str: id>'''
        pass 