from rest_framework import serializers
from .models import User
from materials.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['material_id', 'materials', 'material_sub_type', 'thickness', 'finish', 'length', 'width', 'cost', 'vendor', 'user']

class UserSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['user', 'created_at']