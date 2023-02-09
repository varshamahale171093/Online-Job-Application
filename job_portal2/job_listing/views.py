from django.shortcuts import render

# Create your views here.
from functools import partial
from django.shortcuts import render
from .models import JobDB
from .serializers import JobDBSerializer
from django.views import View
# from rest_framework import viewsets


from requests import delete
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
import json
from rest_framework.decorators import api_view
# from rest_framework.response import Response


# class JobDB_api(viewsets.ModelViewSet):
#     queryset = jobDB.objects.all()
#     serializer_class = JobDBSerializer
    





@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
def JobDB_api(request):
    if request.method == 'GET':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        print(f"Steam",stream)
        python_data=JSONParser().parse(stream)
        print(f"Python Data -------",python_data)
        id=python_data.get('id',None)
        if id is not None:
            job=JobDB.objects.get(id=id)
            serializer=JobDBSerializer(job)
            print(f"data print by using serialiser ------",serializer)
            json_data=JSONRenderer().render(serializer.data)
            print(f"json data ------",json_data)
            return HttpResponse(json_data,content_type='application/json')
        
        job=JobDB.objects.all()
        serializer=JobDBSerializer(job,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')


    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)  
        python_data=JSONParser().parse(stream)
        serializer=JobDBSerializer(data=python_data)  
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')    

    if request.method=='PUT':
            json_data=request.body
            stream=io.BytesIO(json_data)  
            python_data=JSONParser().parse(stream)
            id=python_data.get('id')
            stu=JobDB.objects.get(id=id)

            serializer=JobDBSerializer(stu,data=python_data,partial=True)# if partial is false or not given then requird all filed to be completed 
            if serializer.is_valid():
                serializer.save()
                res={'msg':'Data Updated!!'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')


    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        job=JobDB.objects.get(id=id)
        job.delete()
        res={'msg':'data deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    json_data=JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')  
    return JsonResponse(res,safe=False)
    