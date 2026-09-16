from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Heredero
from .serializers import HerederoSerializer


@api_view(["GET", "POST"])
def herederos(request):
    if request.method == "GET":
        herederos = Heredero.objects.all()
        serializer = HerederoSerializer(herederos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = HerederoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def heredero_detail(request, pk):
    heredero = get_object_or_404(Heredero, pk=pk)

    if request.method == "GET":
        serializer = HerederoSerializer(heredero)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = HerederoSerializer(heredero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    heredero.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
