from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from music.models import Categories, User, Music

from .serializers import CategoriesSerializer, UserRegistrationSerializer, LatestMusicSerializer

class categoriesList(APIView):
	permission_classes = [permissions.AllowAny]
	def get(self,request, format=None):
		query = Categories.objects.all().order_by('-id')
		serializer = CategoriesSerializer(query, many=True)
		if serializer:
			return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		data = request.data
		serializer = CategoriesSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class categoriesDetails(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get_object(self,id):
		instance = get_object_or_404(Categories, id=id)
		return instance

	def get(self, request, pk, format=None):
		instance = self.get_object(pk)
		serializer = CategoriesSerializer(instance)
		if serializer:
			return Response(serializer.data, status= status.HTTP_200_OK)
		return Response(status=HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format= None):
		instance = self.get_object(pk)
		data = request.data
		serializer = CategoriesSerializer(data=data, instance=instance)
		if serializer.is_valid():
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		instance = self.get_object(pk)
		delete = instance.delete()

		if delete:
			return Response(status= status.HTTP_200_OK)

class registerUser(APIView):

	def post(self, request, format=None):
		data = request.data
		serializer = UserRegistrationSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class latestMusic(APIView):
	def get(self, request, format=None):
		latest = Music.objects.all().order_by('-id')[:8]
		serializer = LatestMusicSerializer(latest, many=True)
		if serializer:
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(status=status.HTTP_400_BAD_REQUEST)
