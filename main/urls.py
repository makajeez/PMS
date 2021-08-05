from django.conf.urls import url
from rest_framework import views
from .views import *

urlpatterns = [
    url(r'^chapter/$', ChapterApi),
    url(r'^req_meeting/', ReqMeetingApi),
    url(r'^upload_topic/', UploadTopicApi)
]