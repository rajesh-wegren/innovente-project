from django.db import models

# Create your models here.
class Member_inno(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth = models.DateField()
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Address(models.Model):
    address_type=models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=100, null=True)
    address_line2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=45, null=True)
    pin = models.IntegerField()
    country = models.CharField(max_length=45, null=True)

    member = models.ForeignKey(Member_inno, on_delete=models.CASCADE)