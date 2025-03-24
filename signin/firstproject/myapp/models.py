from django.db import models

# Create your models here.

class staffs(models.Model): #員工資料
    cName = models.CharField(max_length=20, null=False)
    cPhone = models.CharField(max_length=50, blank=False, default='')
    cLine = models.CharField(max_length=20, blank=True, default='')
    cpassword = models.CharField(max_length=20, blank=True, default='')
    def __str__(self):
        return self.cName
    