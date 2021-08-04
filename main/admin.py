from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Supervisor)
admin.site.register(Profile)
admin.site.register(RequestMeeting)
admin.site.register(UploadChapter)
admin.site.register(UploadProposal)
admin.site.register(UploadProject)
admin.site.register(UploadTopic)
admin.site.register(SendInvite)

