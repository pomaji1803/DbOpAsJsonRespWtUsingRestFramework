from django.http import HttpResponse
from .models import ProductModel
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class AllProductView(View):
    def get(self,request):
        return HttpResponse('i am get')
    def post(self,request):
        return HttpResponse('i am post')
    def put(self,request):
        return HttpResponse('i am put')
    def delete(self,request):
        return HttpResponse('i am delete')