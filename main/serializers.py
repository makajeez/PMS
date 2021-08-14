# from typing_extensions import Required
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer	
from .models import *

class SupervisorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Supervisor
		fields = '__all__'


class RegistrationSerializer(RegisterSerializer):
	first_name = serializers.CharField(required=False)
	last_name = serializers.CharField(required=False)

	def custom_signup(self, request, user):
		user.first_name = self.validated_data.get('first_name', '')
		user.last_name = self.validated_data.get('last_name', '')

		user.save(update_fields=['first_name', 'last_name'])

# Student Activity Model Serializer Begins
class UploadProposalSerializer(serializers.ModelSerializer):
	class Meta:
		model = UploadProposal
		fields = ['id', 'proposal_title', 'proposal_file', 'supervisor', 'student', 'status']

class UploadChapterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UploadChapter
		fields = ['id', 'chapter_number', 'chapter_file', 'student', 'supervisor', 'status']

class RequestMeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = RequestMeeting
		fields = ['id','date', 'time', 'student', 'supervisor', 'status']

# Student Activity Model Serializer Ends




# Supervisor Activity Model Serializer Begins
class UploadTopicSerializer(serializers.ModelSerializer):
	class Meta:
		model = UploadTopic
		fields = ['id','title', 'date', 'supervisor']

class UploadProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = UploadProject
		fields = ['id', 'student', 'project_title', 'project_file', 'year', 'supervisor']

class SendInviteSerializer(serializers.ModelSerializer):
	class Meta:
		model = SendInvite
		fields = ['id','date', 'time', 'student', 'supervisor', 'venue']
	

# Student Activity Model Serializer Ends