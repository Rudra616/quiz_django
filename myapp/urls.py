# from django.urls import path
# from .views import *

# urlpatterns = [
#     # path('api/',get_quiz,name='get_quiz'),
#     path('a/',home,name='home'),
#     path('q',quiz,name='quiz')
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('quiz/', views.quiz, name='quiz'),  # Quiz page
]
