from django.shortcuts import render
from django.http import JsonResponse


def post_data(request):
    
    data = request.POST
    
    print(data)
    
    return JsonResponse(data)
