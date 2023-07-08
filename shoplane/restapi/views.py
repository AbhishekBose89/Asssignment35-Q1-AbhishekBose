from django.views import View
import json
from django.http import JsonResponse
from .models import *
from .serializers import *


# Create your views here.
class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        serialized_category = CategorySerializer(category, many=True).data
        return JsonResponse(serialized_category, safe=False, status=200)

    def post(self, request):
        category = json.loads(request.body)
        serialized_category = CategorySerializer(data=category)
        try:
            if serialized_category.is_valid():
                Category.objects.create(**category)
                return JsonResponse(serialized_category.data, safe=False, status=201)
        except:
            return JsonResponse(serialized_category.errors, safe=False)


class ProductView(View):
    def get(self, request):
        product = Product.objects.all()
        serialized_product = ProductSerializer(product, many=True).data
        return JsonResponse(serialized_product, safe=False, status=200)

    def post(self, request):
        product = json.loads(request.body)
        serialized_product = ProductSerializer(data=product)
        try:
            if serialized_product.is_valid():
                Product.objects.create(**product)
                return JsonResponse(serialized_product.data, safe=False, status=200)
        except:
            return JsonResponse(serialized_product.errors, safe=False)
