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

    # TODO look into doing this a different way for perf (annotate?)
    @property
    def successes(self):
        return self.test_set.filter(status='success').count()

    # TODO look into doing this a different way for perf
    @property
    def failures(self):
        return self.test_set.filter(status='failed').count()

    # TODO look into doing this a different way for perf
    @property
    def total_tests_run(self):
        return self.test_set.count()

class Test(models.Model):
    label = models.CharField(max_length=256)
    status = models.CharField(max_length=30)
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start = models.DateTimeField(auto_now=False, null=True)
    end = models.DateTimeField(auto_now=False, null=True)
    run = models.ForeignKey(Run, on_delete=models.CASCADE) 
