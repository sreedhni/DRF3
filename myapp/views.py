from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import SnippetCreateSerializer, SnippetDetailsSerializer,UserCreateSerializer
from .models import Snippet
from django.contrib.auth.models import User


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateMyAppView(CreateAPIView):
    serializer_class = SnippetCreateSerializer
    def post(self, request, *args, **kwargs):
        snip_serializer = self.get_serializer(data=request.data)
        if snip_serializer.is_valid():
            snip_serializer.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Failed", "errors": snip_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class CreateMyAppapiView(APIView):
    def post(self, request, *args, **kwargs):
        snip_serializer = SnippetCreateSerializer(data=request.data)
        if snip_serializer.is_valid():
            snip_serializer.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Failed", "errors": snip_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class MyAppDetailView(APIView):
    def get(self, request, *args, **kwargs):
        instance = Snippet.objects.filter(pk=kwargs.get("pk"))
        if instance.exists():
            serializer = SnippetDetailsSerializer(instance.first())
            return Response(serializer.data)
        else:
            return Response({"message": "Snippet not found"}, status=status.HTTP_404_NOT_FOUND)
        
class MyAppDetailView(RetrieveAPIView):
    serializer_class = SnippetDetailsSerializer
    queryset = Snippet.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)