
import json
from django.http.request import QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User
from rest_auth.registration.views import RegisterView

from django.core.files.storage import default_storage

from .serializers import *
from .models import *

# Create your views here.
for user in User.objects.all():
	Token.objects.get_or_create(user=user)

@csrf_exempt
def UserApi(request):
    if request.method == 'GET':
        user = User.objects.all()
        userSerializer = RegisterSerializer(user, many=True)
        return JsonResponse(userSerializer.data, safe=False)

def SupervisorApi(request):
    if request.method == 'GET':
        supervisor = Supervisor.objects.all()
        superSerializer = SupervisorSerializer(supervisor, many=True)
        return JsonResponse(superSerializer.data, safe=False)

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
            'username': user.username,
            # 'fullname': user.fullname,
            # 'lastname': user.last_name,
            # 'supervisor': user.supervisor
        })


# student activity views begin
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

class ProposalView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self, pk):
        try: 
            return UploadProposal.objects.get(pk = pk)
        except UploadProposal.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        file_serializer = UploadProposalSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse('Proposal Sent Successfully', safe=False)
        else:
            return JsonResponse('upload fail', safe=False)
    def put(self, request, pk):
        prop = self.get_object(pk)
        file_serializer = UploadProposalSerializer(prop, data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        else:
            return JsonResponse('update fail', safe=False)
    def get(self, request):
        files = UploadProposal.objects.all()
        filesSerializer = UploadProposalSerializer(files, many=True)
        return JsonResponse(filesSerializer.data, safe=False) 

class ChapterView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        chapter_serializer = UploadChapterSerializer(data=request.data)
        if chapter_serializer.is_valid():
            chapter_serializer.save()
            return JsonResponse('Chapter Sent Successfully', safe=False)
        else:
            return JsonResponse('upload fail', safe=False)
    def get(self, request):
        chapter = UploadChapter.objects.all()
        chapterSerializer = UploadChapterSerializer(chapter, many=True)
        return JsonResponse(chapterSerializer.data, safe=False) 
    def put(self, request, pk):
        chapter = UploadChapter.objects.get(pk = pk)
        chapterSerializer = UploadChapterSerializer(chapter, data=request.data)
        if chapterSerializer.is_valid():
            chapterSerializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        else:
            return JsonResponse('update fail', safe=False)

# student activity views ends


# Supervisor activity views begin
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

@csrf_exempt
def SendInviteApi(request, id=0):
    if request.method == 'GET':
        invite = SendInvite.objects.all()
        inviteSerializer = SendInviteSerializer(invite, many=True)
        return JsonResponse(inviteSerializer.data, safe=False)
    elif request.method == 'POST':
        inviteData = JSONParser().parse(request)
        inviteSerializer = SendInviteSerializer(data=inviteData)
        if inviteSerializer.is_valid():
            inviteSerializer.save()
            return JsonResponse('Invitation Sent', safe=False)
        return JsonResponse('There is an error somewhere', safe=False)

class ProjectView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        project_serializer = UploadProjectSerializer(data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse('Sent Successfully', safe=False)
        else:
            return JsonResponse('upload fail', safe=False)
    def get(self, request):
        project = UploadProject.objects.all()
        projectSerializer = UploadProjectSerializer(project, many=True)
        return JsonResponse(projectSerializer.data, safe=False) 

# Supervisor activity views ends