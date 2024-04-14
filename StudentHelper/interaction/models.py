from django.db import models

# Create your models here.
class AddQuestions(models.Model):
    question = models.CharField(max_length=200)
    visiable = models.BooleanField(default=True)
    questionownerid = models.CharField(max_length=50)
    queaddeddate = models.DateTimeField(auto_now=False, auto_now_add=True)

class AnsOfQue(models.Model):
    qid = models.CharField(max_length=50)
    ansstr = models.TextField()
    ansownerid = models.CharField(max_length=50)
    visiable = models.BooleanField(default=True)
    ansdate =  models.DateTimeField(auto_now=False, auto_now_add=True)