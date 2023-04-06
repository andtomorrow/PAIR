# posts/models.py
from django.db import models

# Create your models here.
class Post(models.Model):

    CATEGORY = [

    ]

    title=models.CharField(max_length=80)
    content=models.TextField(null=False)
    category=models.CharField(max_length=20, choices=CATEGORY)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# title	게시글 제목	Char	max_length=80
# content	게시글 내용	Text	null=False
# category	게시글 분류	Char	max_length=20
# created_at	생성 날짜	DateTime	auto_now_add=True
# updated_at	수정 날짜	DateTime	auto_now=True