from django.db import models
#====================================#
# This section is creating model from
#====================================#
class contact( models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    subject = models.CharField(max_length=165)
    message = models.TextField()
    
    def __str__(self):
        return self.name
#====================================#
# This section is uploading PDF
#====================================#
    
class ResumeModel(models.Model):
    pdf = models.FileField(upload_to="pdfs/")
    
    def __str__(self):
       return self.pdf.name