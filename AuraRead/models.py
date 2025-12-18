from django.db import models

# Create your models here.

class PdfDocumnet(models.Model):
    File = models.FileField(upload_to= 'pdfs/')
    upload_date = models.DateTimeField(auto_now_add= True)
    audio_file = models.FileField(upload_to= 'audio/', null= True, blank= True)

    def __str__(self):
        return f"PDF {self.id} uploaded on {self.upload_date}."