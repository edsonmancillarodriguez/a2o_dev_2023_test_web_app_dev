from rest_framework import serializers
from .models import A2Otest


class A2OtestSerializers(serializers.ModelSerializer):
    class Meta:
        model = A2Otest
        fields = ('name',)
