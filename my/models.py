from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class MyVarity(models.Model):
    MY_TYPE_CHOICE=[
     ('EY','EYE'),
     ('EA','EAR'),
     ('NO','NOSE'),
     ('MO','MOUTH'),
     ('LI','LIPS'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='mine/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=MY_TYPE_CHOICE)
    description=models.TextField(default='')


    def __str__(self):
        return self.name
    
# one to many

class MyReview(models.Model):
    my=models.ForeignKey(MyVarity,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.my.name}'
    

#many to many
class store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    my_varities=models.ManyToManyField(MyVarity,related_name='stores')

    def __str__(self):
        return self.name
    
#one to one

class MyCertificate(models.Model):
    my= models.OneToOneField(MyVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issued_date =models.DateTimeField(default=timezone.now)
    valid_untill=models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.name.my}'