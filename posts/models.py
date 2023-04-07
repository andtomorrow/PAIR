# posts/models.py
from django.db import models

# Create your models here.

class Post(models.Model):
    DEVELOPMENT = 'DEV'
    COMPUTER_SCIENCE = 'CS'
    NEW_TECHNOLOGY = 'NEW_TECH'
    CATEGORY = [
        (DEVELOPMENT, '개발'),
        (COMPUTER_SCIENCE, 'CS'),
        (NEW_TECHNOLOGY, '신기술'),
    ]

    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    category = models.CharField(
        max_length=20, choices=CATEGORY, default=DEVELOPMENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    category_names = ['개발', 'CS', '신기술',]
    
    category_dct = {
        'DEV': '개발',
        'CS': 'CS',
        'NEW_TECH': '신기술',
    }


# title	게시글 제목	Char	max_length=80
# content	게시글 내용	Text	null=False
# category	게시글 분류	Char	max_length=20
# created_at	생성 날짜	DateTime	auto_now_add=True
# updated_at	수정 날짜	DateTime	auto_now=Tru
