from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import TodoSerializer, StatusSerializer

from .models import *

@csrf_exempt
def list(request):

    if request.method == 'GET':
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  

            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)
    

@csrf_exempt
def status(request):

    if request.method == 'GET':
            statuses = Status.objects.all()
            serializer = StatusSerializer(statuses, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  

            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)