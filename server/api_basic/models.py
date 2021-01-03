from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    # auto_now_add?
    # 데이터 생성 시 생성 date 자동입력 
    # vs auto_now? 
    # auto_now는 생성 시만이 아닌, 수정시마다 입력
    date = models.DateTimeField(auto_now_add=True)
    
    # 접근자?
    def __str__(self):
        return self.title
