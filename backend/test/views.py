from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response
# Create your views here.

class ReactView(APIView):
    def get(self, request):
        output = [{ 'employee': output.employee, 'department': output.department } for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# This Python code is a Django REST Framework view that handles HTTP GET and POST requests for the React model. Here's a breakdown:
# Imports: The necessary modules and classes are imported. This includes Django's render function, the APIView class from Django REST Framework, all models from the current directory (models.py), all serializers from the current directory (serializer.py), and the Response class from Django REST Framework.
# ReactView class: This class inherits from APIView, which is a class-based view that provides methods to handle HTTP requests.
# get method: This method handles HTTP GET requests. It retrieves all React objects from the database, creates a list of dictionaries where each dictionary contains an 'employee' and 'department' key (both set to the employee attribute of the React object), and returns this list as a HTTP response. However, there seems to be a mistake here: the 'department' key should likely be set to the department attribute of the React object, not the employee attribute.
# post method: This method handles HTTP POST requests. It creates a ReactSerializer instance with the data from the request, checks if the data is valid, and if it is, saves the data to the database and returns the saved data as a HTTP response. If the data is not valid, it returns the validation errors as a HTTP response.