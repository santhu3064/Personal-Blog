from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = now()
        self.save()

    def approve_comments(self):
        self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.text


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=now)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
