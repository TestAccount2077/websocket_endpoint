from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Data

import json

@csrf_exempt
def post_data(request):
    
    data =  json.loads(request.POST['data'])
    
    data_obj, created = Data.objects.get_or_create(id=1)
    
    data_obj.revenue_items = str(data['revenue_items'])
    data_obj.expense_items = str(data['expense_items'])
    data_obj.order_percentages = str(data['order_percentages'])
    
    data_obj.save()
    
    return JsonResponse(data)
