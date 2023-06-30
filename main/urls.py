from django.urls import path
from .templates.main import views

urlpatterns = [
    path('', views.index),
    path('update', views.update),
    path('single', views.single),
    path('single/move', views.singleMove),
    path('motion', views.motion),
    path('ezbot', views.ezbot),
    path('ezbot-side', views.choose_ezbot_side),
    path('hardbot-side', views.choose_hardbot_side),
    path('hard-move', views.hard_move),
    path('easy-move', views.easy_move),
]
