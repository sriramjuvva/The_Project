from rest_framework import serializers
from . models import *

class courseserializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_Model
        fields = ['id','Course_name']