from django.http import JsonResponse
from .models import book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET','POST'])
def book_list(request,format=None):
    # //get all the drinks
    if(request.method=='GET'):
     books=book.objects.all()
     serializer=BookSerializer(books, many=True)
     return Response(serializer.data)
    
    if(request.method=='POST'):
       serializer=BookSerializer(data=request.data)
       if(serializer.is_valid()):
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])    
def book_detail(request, id,format=None):
   try:
      one=book.objects.get(pk=id)
   except book.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)  
   
   if(request.method=='GET'):
     serializer=BookSerializer(one)
     return Response(serializer.data)
   
   elif (request.method == 'PUT'):
      serializer=BookSerializer(one,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   elif request.method=='DELETE':
      one.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)