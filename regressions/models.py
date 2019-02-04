from django.db import models

class Run(models.Model):
    label = models.CharField(max_length=256)
    status = models.CharField(max_length=30)
    duration = models.IntegerField()
    submitter = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start = models.DateTimeField(auto_now=False, null=True)
    end = models.DateTimeField(auto_now=False, null=True)

class Test(models.Model):
    label = models.CharField(max_length=256)
    status = models.CharField(max_length=30)
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start = models.DateTimeField(auto_now=False, null=True)
    end = models.DateTimeField(auto_now=False, null=True)
    run = models.ForeignKey(Run, on_delete=models.CASCADE) 
