from quizzes.models import Test
from rest_framework import serializers

from .models import Lesson, Step, StepUser
from quizzes.serializers import TestSerializer


class StepSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)

    class Meta:
        model = Step
        fields = ['id', 'likes', 'number', 'dislikes', 'title', 'test']

    def create(self, validated_data):
        return Step(**validated_data)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title']


class StepUserSerializer(serializers.ModelSerializer):
    step = StepSerializer(many=True, read_only=True)

    class Meta:
        model = StepUser
        fields = ['id', 'passed', 'user', 'step', 'feedback', 'score']
