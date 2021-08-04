from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


status = (
			("Accepted", "Accepted"),
			("Rejected", "Rejected"),	
			("Pending", "Pending")		
		)
chapters = (
	("Chapter One", "Chapter One"),
	("Chapter Two", "Chapter Two"), 
	("Chapter Three", "Chapter Three"),
	("Chapter Four", "Chapter Four"),
	("Chapter Five", "Chapter Five"),
	)

# Create your models here.
class Supervisor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=50, default="")

	def __str__(self):
		return f'{self.user}'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)		
	fullname = models.CharField(max_length=50, default="")

	def __str__(self):
		return f'{self.user}'
		

def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)	

post_save.connect(create_profile, sender=User)




# Student Activity Model Begin
class UploadChapter(models.Model):
	chapter_number = models.CharField(max_length=50, choices=chapters)
	chapter_file = models.FileField(upload_to="files")
	student = models.ForeignKey(User,on_delete=models.CASCADE)
	supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	status = models.CharField(max_length=100, choices=status, default="Pending")

	def __str__(self):
		return f'{self.student} - {self.chapter_number}'

class UploadProposal(models.Model):
	proposal_title = models.CharField(max_length=100, default='')
	proposal_file = models.FileField(upload_to="files", null=True)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	status = models.CharField(max_length=10, choices=status, default="Pending")

	def __str__(self):
		return f'{self.student} - {self.proposal_title}'

# def create_proposal(sender, instance, created, **kwargs):
# 	if created:
# 		UploadProposal.objects.create(student = instance)
# post_save.connect(create_proposal, sender=User)


class RequestMeeting(models.Model):
	date = models.CharField(max_length=15)
	time = models.CharField(max_length=6, default='12/12/2021')
	student = models.CharField(max_length=50)
	supervisor = models.CharField(max_length=50)
	status = models.CharField(max_length=15, choices=status, default="Pending")

	def __str__(self):
		return f'{self.student} - {self.supervisor} - {self.date} - {self.time}'

# Send Activity Model End





# Supervisor Activity Begins
class UploadTopic(models.Model):
	title = models.CharField(max_length=100, null=False)
	date = models.DateTimeField(auto_now_add=True)
	supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title} - {self.date} - {self.supervisor}'

class UploadProject(models.Model):
	student = models.CharField(max_length=50)
	project_title = models.CharField(max_length=100)
	project_file = models.FileField(upload_to="files")
	year = models.CharField(max_length=15)
	supervisor = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.project_title} - {self.student} - {self.supervisor}'

class SendInvite(models.Model):
	date = models.CharField(max_length=15)
	time = models.CharField(max_length=6)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	venue = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.supervisor} - {self.date} - {self.time} - {self.student}'

# Supervisor Activity Ends
