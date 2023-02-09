from rest_framework import serializers
from .models import JobDB
from rest_framework import generics



class JobDBSerializer(serializers.ModelSerializer):
       
        
    class Meta:
        model = JobDB
        fields ='__all__'
        
    
    
    
    def create(self,validated_data):
      return JobDB.objects.create(validated_data)


    def update(self,instance,validated_data):
        # print(instance.name)
        instance.title=validated_data.get('title',instance.title)
        # print(instance.name)
        instance.location=validated_data.get('location',instance.location)
        instance.salary=validated_data.get('salary',instance.salary)
        instance.experience=validated_data.get('experience',instance.experience)
        
        instance.save()      
        return instance
