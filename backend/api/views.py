from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer # This serializer handles the serialization and deserialization of Note objects
    permission_classes = [IsAuthenticated] # Only authenticated users can access this view


    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)

 
#Permission classes are used to restrict access to certain views based on user authentication status.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # This queryset is used to create a new user
    serializer_class = UserSerializer # This serializer handles the creation of user accounts
    permission_classes = [AllowAny]  # Allow any user to create an account


