from django.shortcuts import render
from rest_framework.views import APIView
from models import Content
from models import Question
from serializers import *
from rest_framework.response import Response


class AddContent(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(AddContent, self).dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        objs = Content.objects.all()
        con = ContentSerializer(objs, many=True)
        return Response(con.data)

    def post(self, request, format=None):
        # todo
        data = request.data
        serializer = ContentPostSerializer(data=data)
        if not serializer.is_valid():
            err = {}
            err['msg'] = serializer.errors
            return Response(err)
        obj = Content()
        obj.entry = data['entry']
        obj.save()
        con = ContentSerializer(obj)
        return Response(con.data)

    def put(self, request, id, format=None):
        # todo
        data = request.data
        serializer = ContentPostSerializer(data=data)
        if not serializer.is_valid():
            err = {}
            err['msg'] = serializer.errors
            return Response(err)
        obj = Content.objects.get(id=id)
        if obj:
            obj1 = Content()
            obj1.entry = data['entry']
            obj1.save()
            con = ContentSerializer(obj1)
            return Response(con.data)

#    def delete(self, request, id, format=None):
#	obj = Content.objects.get(id)
#	obj.delete()
#	con = ContentSerializer(obj)
#        return Response(con.data)

#	return Response(status=status.HTTP_204_NO_CONTENT)

class AddQuestion(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(AddQuestion, self).dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        objs = Question.objects.all()
        con = QuestionSerializer(objs, many=True)
        return Response(con.data)

    def post(self, request, subject, format=None):
        # todo
        data = request.data
	model = Question()
        serializer = QuestionPostSerializer(data=data,many=True)
        if not serializer.is_valid():
            err = {}
            err['msg'] = serializer.errors
            return Response(err)
	li=[]
	for i in data:
            obj1 = Content.objects.get(entry=subject)
    	    if obj1:
                obj = Question()
                obj.que = i['que']
                obj.subject = subject
                obj.difficulty = i['difficulty']
                obj.ref = obj1
                obj.save()
		li.append(obj)
	con = QuestionSerializer(li,many=True)
        return Response(con.data)

#    def put(self, request, id, format=None):
#        # todo
#        data = request.data
#        serializer = QuestionPostSerializer(data=data)
#        if not serializer.is_valid():
#            err = {}
#            err['msg'] = serializer.errors
#            return Response(err)
#        obj = Question.objects.get(id=id)
#        if obj:
#	    obj1 = Question()
#            obj1.entry = data['entry']
#            obj1.save()
#            con = QuestionSerializer(obj1)
#           return Response(con.data)


class Output(APIView):
     def dispatch(self, request, *args, **kwargs):
        return super(Output, self).dispatch(request, *args, **kwargs)

     def get(self, request, subject, difficulty, format=None):
        lis = {}
        lis["count"] = Question.objects.filter(subject=subject,difficulty=difficulty).count()
	objs = Question.objects.filter(subject=subject,difficulty=difficulty)
        con = OutputSerializer(objs, many=True)
        return Response([con.data,lis])

    


# Create your views here.
