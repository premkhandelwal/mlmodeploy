from rest_framework import serializers
from .models import Predict

class PredictSerializer(serializers.ModelSerializer):
    sepal_length = serializers.IntegerField()
    sepal_width = serializers.IntegerField()
    petal_length = serializers.IntegerField()
    petal_width = serializers.IntegerField()

    class Meta:
        model = Predict
        fields = '__all__'