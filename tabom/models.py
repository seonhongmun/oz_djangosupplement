from django.db import models


class User(models.Model):
    name = models.CharField("이름", max_length=50)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    created_at = models.DateTimeField("생성일", auto_now_add=True)


class Article(models.Model):
    title = models.CharField("제목", max_length=255)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    created_at = models.DateTimeField("생성일", auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    created_at = models.DateTimeField("생성일", auto_now_add=True)
