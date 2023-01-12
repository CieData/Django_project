from django.db import models
#	Create	your	models	here.
class Post(models.Model):
    name	=	models.CharField(max_length=30)	#	데이터베이스의 필드(컬럼)
    created_at =	models.DateTimeField(auto_now_add=True)
    updated_at =	models.DateTimeField(auto_now=True)
    introduce	=	models.TextField()

#	author는 추후 작성
def __str__(self):
    return f'[{self.pk}] {self.title}'