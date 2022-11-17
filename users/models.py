from pyexpat.errors import messages
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    Division=(
        ('ঢাকা','ঢাকা'),
        ('রাজশাহী','রাজশাহী'),
        ('যশোর','যশোর')
    )
    District=(
        ('মানিকগঞ্জ','মানিকগঞ্জ'),
        ('টাঙ্গাইল','টাঙ্গাইল'),
        ('ফরিদপুর','ফরিদপুর'),
        ('গাজিপুর','গাজিপুর'),
        ('রাজবারি','রাজবারি'),
        ('পাবনা','পাবনা'),
        ('নাটোর','নাটোর'),
        ('চাপাইনবাবগঞ্জ','চাপাইনবাবগঞ্জ'),
        ('বগুরা','বগুরা')

        
    )
    Thana=(
        ('মানিকগঞ্জ সদর','মানিকগঞ্জ সদর'),
        ('হরিরামপুর','হরিরামপুর'),
        ('শিবালয়','শিবালয়'),
        ('ঘিয়র','ঘিয়র'),
        ('সিংগাইর','সিংগাইর'),
        ('পাবনা সদর উপজেলা','পাবনা সদর উপজেলা'),
        ('বগুরা','বগুরা')

    )
    Busy=(
        ('কর্মরত আছে','কর্মরত আছে'),
        ('খালি আছে','খালি আছে')
        )
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, blank=True,null=True)
    short_intro=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)

    email=models.EmailField(max_length=500, blank=True, null=True)
    username=models.CharField(max_length=200, blank=True,null=True)
    mobile=models.CharField(max_length=200, blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/', default='profiles/user-default.png')
    
    social_facebook=models.CharField(max_length=200, blank=True,null=True)
    youtube=models.CharField(max_length=200, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    rate=models.CharField(max_length=200, blank=False,null=True)
    busy=models.CharField(max_length=50,blank=False,null=True,choices=Busy)
    division=models.CharField(max_length=200,blank=True,choices=Division)
    district=models.CharField(max_length=200,blank=True,choices=District)
    thana=models.CharField(max_length=200,blank=True,choices=Thana)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,blank=True)
    name=models.CharField(max_length=200, blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name



class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=12, blank=True, null =True)
    thana= models.CharField(max_length=200, blank=True, null=True)
    union= models.CharField(max_length=200, blank=True, null=True)
    village= models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']

class Order(models.Model):
    name=models.CharField(max_length=150)
    sender_email=models.EmailField(max_length=200, null=True, blank=True)
    reciepient_email= models.EmailField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
