from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=40)
    pub_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pub_news")
    review_pass_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="pass_news", blank=True, null=True)
    cover_image = models.URLField(blank=True, null=True)
    pub_date = models.DateTimeField()
    content = models.TextField()
    favorited = models.ManyToManyField(User, related_name="favorite_news", blank=True)
    def __str__(self):
        return self.title



    