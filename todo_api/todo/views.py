from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import TodoSerializer, StatusSerializer

from .models import *

@csrf_exempt
def list(request):
    """
    Get all tasks or create one
    """
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
    Get, update or delete task by <id>
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
    """
    Get all statuses or create one
    """

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
    

@csrf_exempt
def reorder(request):
    """
    Rearrange positions of tasks by "front-end" payload(Postman)
    """

    if request.method != 'PUT':
        return
    data = JSONParser().parse(request)
    for task in data['order']:
        try:
            todo = Todo.objects.get(pk=task['id'])
            serializer = TodoSerializer(todo, data=task)
            if serializer.is_valid():
                serializer.save()
            else:
                return JsonResponse(serializer.errors, status=400)
        except Todo.DoesNotExist:
            return HttpResponse(status=404)

        
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)

    return JsonResponse(serializer.data, safe=False)
        