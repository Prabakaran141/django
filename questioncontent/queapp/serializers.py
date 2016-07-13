
from rest_framework import serializers
from models import Question

class ContentPostSerializer(serializers.Serializer):
    entry = serializers.CharField()

class ContentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    entry = serializers.CharField()

class QuestionPostSerializer(serializers.ModelSerializer):
    def __init__(self,*args,**kwargs):
        many = kwargs.pop('many',True)
	super(QuestionPostSerializer,self).__init__(many=many,*args,**kwargs)

    class Meta:
        model = Question
	fields = ('que','difficulty')

#    que = serializers.CharField()
#    subject = serializers.CharField()
#    difficulty = serializers.CharField()


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    que = serializers.CharField()
    subject = serializers.CharField()
    difficulty = serializers.CharField()
   # ref = serializers.IntegerField()

class OutputSerializer(serializers.Serializer):
    que = serializers.CharField()
    subject = serializers.CharField()
    difficulty = serializers.CharField()


