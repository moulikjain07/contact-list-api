from django.shortcuts import render

from rest_framework.views import APIView
from .models import Contact 
from .serializer import ContactSerializer
from rest_framework.response import Response
from rest_framework import status

class ContactList(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

class ContactCreate(APIView):
    def post(self, request):
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetail(APIView):
    def get_contact_by_pk(self, pk):
        try:
            contact = Contact.objects.get(pk=pk)
            return contact
        except:
            return Response({
            'error':'Contact not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        contact = self.get_contact_by_pk(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk):
        contact = self.get_contact_by_pk(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_contact_by_pk(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
