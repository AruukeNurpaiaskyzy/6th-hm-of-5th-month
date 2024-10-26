from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response 
from rest_framework.views import APIView 
from .models import List
from .serializers import ListSerializer
# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
class DeleteAllListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        request.user.lists.all().delete()
        return Response({"message": "All tasks deleted."}, status=status.HTTP_204_NO_CONTENT)
