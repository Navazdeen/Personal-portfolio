from django.db import models


class Job(models.Model):
    # name
    name = models.CharField(max_length=100)
    # image
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.TextField()
    # project date
    date = models.DateTimeField()
    # type
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
