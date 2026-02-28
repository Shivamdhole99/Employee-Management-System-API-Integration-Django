# from rest_framework import serializers
# from .models import Book

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'publish_date']

from rest_framework import serializers
from .models import employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'