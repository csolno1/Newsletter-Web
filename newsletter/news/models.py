from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name_choice = [
        ("全球", "全球"),
        ("政治", "政治"),
        ("科技", "科技"),
        ("科学", "科学"),
        ("体育", "体育"),
        ("健康", "健康"),
    ]
    name = models.CharField(max_length=10, choices=name_choice)
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=40)
    pub_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pub_news")
    author = models.CharField(max_length=40, default="unknown")
    review_pass_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="pass_news", blank=True, null=True)
    cover_image = models.URLField(blank=True, null=True)
    pub_date = models.DateTimeField()
    content = models.TextField()
    favorited = models.ManyToManyField(User, related_name="favorite_news", blank=True)
    tags = models.ManyToManyField(Tag, related_name="news")
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    pub_date = models.DateTimeField()
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    def __str__(self):
        return self.content




    