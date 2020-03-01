from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from .models import ProductModel
import json
#-----------------------------------------------------------------------------------------------------------------------
#In this we are using Python BuiltIn Package 'json'
class ViewAllProduct(View):
    def get(self,request):
        queryset = ProductModel.objects.all()
        data = {}
        for row in queryset:
            d1 = {
             row.No:{
                 "ProductName" : row.Name,
                 "ProductPrice" : row.Price,
                 "ProductQuantity" : row.Quantity
             }
            }
            data.update(d1)
        json_data = json.dumps(data)
        return HttpResponse(json_data,content_type="application/json")
#-----------------------------------------------------------------------------------------------------------------------
#In this we are using Django BuiltIn 'Serializes'
class ViewAllProductDJ(View):
    def get(self,request):
        queryset = ProductModel.objects.all()
        json_data = serialize('json',queryset)
        return HttpResponse(json_data,content_type="application/json")
#-----------------------------------------------------------------------------------------------------------------------
#In thsi we are using Python BuiltIn Package 'json'
class ViewOneProduct(View):
    def get(self,request,Product):
        try:
            queryset = ProductModel.objects.get(No=Product)
            data = {
                "ProductName" : queryset.Name,
                "ProductPrice" : queryset.Price,
                "ProductQuantity" : queryset.Quantity
            }
            json_data = json.dumps(data)
        except ProductModel.DoesNotExist:
            Error = {
                "Error" : "Product Number is Not Available...!!"
            }
            json_data = json.dumps(Error)
        return HttpResponse(json_data,content_type='application/json')
#-----------------------------------------------------------------------------------------------------------------------
#In this we are using Django BuiltIn 'Serializers'
class ViewOneProductDJ(View):
    def get(self,request,Product):
        try:
            response = ProductModel.objects.get(No=Product)
            json_data = serialize('json',[response])
        except ProductModel.DoesNotExist:
            Error = {
                'Error' : 'Product Number is Not Available...!!'
            }
            json_data = json.dumps(Error)
        return HttpResponse(json_data,content_type='application/json')
#-----------------------------------------------------------------------------------------------------------------------
#In this Example we are doing post Operation.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import ProductForm

@method_decorator(csrf_exempt,name='dispatch')
class InsetOneProduct(View):
    def post(self,request):
        #print(request.body)
        data = request.body
        json_data = json.loads(data)
        pf = ProductForm(json_data)
        if pf.is_valid():
            pf.save()
            json_data = json.dumps({"Success" : "Product is Successfully Inserted...!!"})
        else:
            json_data = json.dumps(pf.errors)
        return HttpResponse(json_data,content_type='application/json')

#-----------------------------------------------------------------------------------------------------------------------
#In this Example we are doing put Operation.
@method_decorator(csrf_exempt,name='dispatch')
class UpdateOneProduct(View):
    def put(self,request,Product):
        try:
            old_product = ProductModel.objects.get(No=Product)
            new_product = json.loads(request.body)
            pf = ProductForm(new_product,instance=old_product)
            if pf.is_valid():
                pf.save()
                json_data = json.dumps({'Success' : 'Product is Successfully Updated...!!'})
            else:
                json_data = json.dumps(pf.errors)
            return HttpResponse(json_data,content_type='application/json')
        except ProductModel.DoesNotExist:
            json_data = json.dumps({'Error' : 'Invalid Product Number Dude...!!'})
            return HttpResponse(json_data, content_type='application/json')
#-----------------------------------------------------------------------------------------------------------------------
@method_decorator(csrf_exempt,name='dispatch')
class UpdateOneProductAnotherWar(View):
    def put(self,request,Product):
        try:
            old_product = ProductModel.objects.get(No=Product)
            new_product = json.loads(request.body)

            data = {
                "No" : old_product.No,
                "Name" : old_product.Name,
                "Price" : old_product.Price,
                "Quantity" : old_product.Quantity
            }

            for key,value in new_product.items():
                data[key] = value
                pf = ProductForm(data,instance=old_product)
                if pf.is_valid():
                    pf.save()
                    json_data = json.dumps({'Success' : "Produce is Successfully Updated...!!"})
                else:
                    json_data = json.dumps(pf.errors)
                return HttpResponse(json_data, content_type='application/json')
        except ProductModel.DoesNotExist:
            json_data = json.dumps({'Error' : 'Invalid Product Number Dude...!!'})
        return HttpResponse(json_data,content_type='application/json')
#-----------------------------------------------------------------------------------------------------------------------
#In this Example we are doing delete Operation.
@method_decorator(csrf_exempt,name='dispatch')
class DeleteOneProduct(View):
    def delete(self,request,Product):
        try:
            result = ProductModel.objects.get(No=Product).delete()
            if result[0] == 1:
                json_data = json.dumps({'Message' : 'Product is Successfully Deleted...!!'})
                return HttpResponse(json_data,content_type='application/json')
        except ProductModel.DoesNotExist:
            json_data = json.dumps({'Error' : 'Invalid Product Number Dude...!!'})
        return HttpResponse(json_data,content_type='application/json')
#-----------------------------------------------------------------------------------------------------------------------


"""

[
	{
		"No" : 109,
		"Name" : "Filla Shoes",
		"Price" : 1500,
		"Quantity" : 3
	},
	{
		"No" : 110,
		"Name" : "Nokia",
		"Price" : 2500,
		"Quantity" : 3		
	},
	{
		"No" : 111,
		"Name" : "Samsung",
		"Price" : 3500,
		"Quantity" : 3
	},
	{
		"No" : 112,
		"Name" : "Vivo",
		"Price" : 4500,
		"Quantity" : 3
	}
]

"""