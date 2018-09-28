from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_data(request):
    
    data = request.POST
    
    print(data)
    
    return JsonResponse(data)
