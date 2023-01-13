from django.db import models
#	Create	your	models	here.
class Post(models.Model):
    name	=	models.CharField(max_length=30)	#	데이터베이스의 필드(컬럼)
    created_at =	models.DateTimeField(auto_now_add=True)
    updated_at =	models.DateTimeField(auto_now=True)
    introduce	=	models.TextField()

#	author는 추후 작성
def __str__(self):
<<<<<<< HEAD
    return f'[{self.pk}]{self.title}'

def get_absolute_url(self):
    if
    glob 
    
    return f'/blog/{self.pk}/'
=======
    return f'[{self.pk}] {self.title}'
>>>>>>> 4a42328b47e97d4012693f525441199a456f604b
