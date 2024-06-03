#used to convert a complex data type to a native python data type so that it can be easily rendered into JSON format

from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['employee', 'department']

# from rest_framework import serializers: This line imports the serializers module from Django's REST Framework. Serializers allow complex data types, like Django models, to be converted to Python data types that can then be easily rendered into JSON.
# from .models import *: This line imports all the models from the current directory's models.py file. These models define the structure of the database tables.
# class ReactSerializer(serializers.ModelSerializer): This line defines a new serializer class ReactSerializer that inherits from serializers.ModelSerializer. A ModelSerializer is a shortcut for creating serializer classes - an automatically determined set of fields.
# Inside the ReactSerializer class, a nested Meta class is defined. This is a Django convention. The Meta class within a Django class provides metadata about the enclosing class.
# model = React: This line tells the ReactSerializer to serialize the React model. The React model should be defined in your models.py file.
# fields = ['employee', 'department']: This line specifies that only the 'employee' and 'department' fields of the React model should be serialized. If there are other fields in the React model, they will not be included in the serialized output.