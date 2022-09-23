from unittest import TextTestRunner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerialiazer
from .models import Product

@api_view(['GET'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerialiazer(products, many=True)
        return Response(serializer.data)


