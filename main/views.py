from django.http.request import QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from django.http.response import JsonResponse

from django.core.files.storage import default_storage

from .serializers import *
from .models import *

# Create your views here.
for user in User.objects.all():
	Token.objects.get_or_create(user=user)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })

@csrf_exempt
def ReqMeetingApi(request, id=0):
    if request.method == 'GET':
        meeting = RequestMeeting.objects.all()
        meetingSerializer = RequestMeetingSerializer(meeting, many=True)
        return JsonResponse(meetingSerializer.data, safe=False)
    elif request.method == 'POST':
        reqData = JSONParser().parse(request)
        reqMeetingSerializer = RequestMeetingSerializer(data=reqData)
        if reqMeetingSerializer.is_valid():
            reqMeetingSerializer.save()
            return JsonResponse('Meeting Request Sent', safe=False)
        return JsonResponse('Error while trying to send your request', safe=False)
    elif request.method=='PUT':
        reqData=JSONParser().parse(request)
        req = RequestMeeting.objects.get(id=reqData['id'])
        reqDataSerializer= RequestMeetingSerializer(req, data=reqData)
        if reqDataSerializer.is_valid():
            reqDataSerializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('An Error Occured, Thats all we know', safe=False)


@csrf_exempt
def UploadTopicApi(request, id=0):
    if request.method == 'GET':
        topic = UploadTopic.objects.all()
        topicSerializer = UploadTopicSerializer(topic, many=True)
        return JsonResponse(topicSerializer.data, safe=False)
    elif request.method == 'POST':
        topicData = JSONParser().parse(request)
        topicSerializer = UploadTopicSerializer(data=topicData)
        if topicSerializer.is_valid():
            topicSerializer.save()
            return JsonResponse('Project Topic Upload Successfully', safe=False)
        return JsonResponse('There is an error somewhere', safe=False)
    elif request.method=='PUT':
        topicData=JSONParser().parse(request)
        topic = UploadTopic.objects.get(id=topicData['id'])
        topicSerializer= UploadTopicSerializer(topic, data=topicData)
        if topicSerializer.is_valid():
            topicSerializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('An Error Occured, Thats all we know', safe=False)








# This is where my problem is, how to submit texts and file to server
@csrf_exempt
def ChapterApi(request):
    if request.method == 'POST':
        chapter = UploadChapter(request.POST, request.FILES)
        chaptersSerializer=UploadChapterSerializer(data=chapter)
        if chaptersSerializer.is_valid():
            chaptersSerializer.save()
            return JsonResponse('Chapter Added Successfully', safe=False)
    else:
        chapter = UploadChapter()
    return JsonResponse('upload fail', safe=False)
