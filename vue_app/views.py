from django.shortcuts import render
from django.http import HttpResponse

from .models import MyFiles
from .serializers import MyFileSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

import string
import random

class MyFilesViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = MyFiles.objects.all()
    serializer_class = MyFileSerializer


def index(request):
    return render(request, 'vue_app/index.html')

def getRandomString(request, name):
    rand_str = generateRandStr(name)
    name_and_rand = mergeNameAndRand(name,rand_str)
    return HttpResponse(name_and_rand)


def generateRandStr(name):
    name_length = len(name)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(name_length))

def mergeNameAndRand(string1, string2):
    return ''.join(i for j in zip(string1, string2) for i in j)

def isCorrectRandom(request, param1, param2):
        if param1 == param2:
            return HttpResponse("correct random string")
        else:
            return HttpResponse("wrong random string")