from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import views
from .views import *

urlpatterns = [
    url(r'^proposal/$', ProposalView.as_view()),
    path('proposal/<int:pk>/', ProposalView.as_view()),
    url(r'^chapter/$', ChapterView.as_view()),
    url(r'^project/$', ProjectView.as_view()),
    url(r'^req_meeting/', ReqMeetingApi),
    url(r'^upload_topic/', UploadTopicApi),
    url(r'^invite/', SendInviteApi),
    url(r'^user/', UserApi)
]
urlpatterns = format_suffix_patterns(urlpatterns)