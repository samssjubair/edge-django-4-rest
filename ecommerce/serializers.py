from symtable import Class
from rest_framework import serializers
from .models import User, Category, Product, Order

# TODO: Add more validation here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['name', 'email']
        extra_kwargs = {
            'name': {
                'max_length': 100,
                'min_length': 3,
                'error_messages': {
                    'max_length': 'Name must be less than 100 characters',
                    'min_length': 'Name must be more than 3 characters',
                },
            },
            'email': {
                'max_length': 100,
                'error_messages': {
                    'max_length': 'Email must be less than 100 characters',
                },
            },
            'phone': {
                'max_length': 100,
            },
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'max_length': 100,
                'min_length': 3,
                'error_messages': {
                    'max_length': 'Name must be less than 100 characters',
                    'min_length': 'Name must be more than 3 characters',
                },
            },
        }

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'max_length': 100,
                'min_length': 3,
                'error_messages': {
                    'max_length': 'Name must be less than 100 characters',
                    'min_length': 'Name must be more than 3 characters',
                },
            },
            'price': {
                'max_digits': 10,
                'decimal_places': 2,
                'error_messages': {
                    'max_digits': 'Price must be less than 10 digits',
                    'decimal_places': 'Price must be 2 decimal places',
                },
            },
            'category': {
                'error_messages': {
                    'required': 'Category is required',
                },
            },
        }

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Order
        fields = '__all__'
