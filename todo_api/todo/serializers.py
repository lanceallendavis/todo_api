from rest_framework import serializers
from .models import *

class StatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)

    class Meta:
        model = Status
        fields = ['id', 'name'] 


class TodoSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only = True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    pub_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    status_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'pub_date', 'status', 'status_id'] 
    

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        print(validated_data)
  
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    

