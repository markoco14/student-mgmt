from rest_framework import serializers

from curriculum.models.module_type import ModuleType


class ModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleType
        fields = '__all__'