from django.db import models


class BaseModel(models.Model):
    updated_at = models.DateTimeField("수정일", auto_now=True)
    created_at = models.DateTimeField("생성일", auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField("이름", max_length=50)


class Article(BaseModel):
    title = models.CharField("제목", max_length=255)


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "article"], name="uniqueconstraints")]
