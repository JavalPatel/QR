from django.db import models

# Create your models here.

class user(models.Model):
    uname = models.CharField(max_length=25, primary_key=True) 
    password = models.CharField(max_length=32, null=False)

    def __str__(self) -> str:
        return self.uname


class info(models.Model):
    id = models.AutoField
    uname = models.OneToOneField(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, default="Patel Javal Kalpeshbhai")
    upi_id = models.CharField(max_length=25, null=False, default="6351489115@paytm")
    


    def __str__(self) -> str:
        return str(self.uname)


