from django.urls import path
from django.views import View
from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.index, name = 'index'),
  path('funcky', views.funcky, name= 'cats'),
  path('danger/<int:guess>', views.danger),
  path('main/<int:guess>', views.MainView.as_view(), name= 'second-view'),
  path('bounce', views.bounce, name='dogs'),
  path('game/<slug:guess>', views.GameView.as_view(), name='dog'),
  path('guess', views.guess),
  path('loop', views.loop, name='first-view'),
  path('second', views.SecondView.as_view()),
  path('guesspost', views.ClassyView.as_view())
]