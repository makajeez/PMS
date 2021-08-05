# PMS

## Help is needed with creating view to send data (texts and file) to the server

this is the models in my DB
```
class UploadProposal(models.Model):
	proposal_title = models.CharField(max_length=100, default='')
	proposal_file = models.FileField(upload_to="files", null=True)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	status = models.CharField(max_length=10, choices=status, default="Pending")

	def __str__(self):
		return f'{self.student} - {self.proposal_title}'
```
