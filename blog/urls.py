from django.urls import path
<<<<<<< HEAD
from . import views
urlpatterns = [
    path('<int:value>/', views.single_post_page),
    path('', views.index),
=======
from .	import views
urlpatterns =	[
    path('',views.index),
>>>>>>> 4a42328b47e97d4012693f525441199a456f604b
]