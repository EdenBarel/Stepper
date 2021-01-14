from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"), # http://127.0.0.1:8000/vanilla-app
    path("get-random/<str:name>", views.getRandomString, name = "get-random-string"), # http://127.0.0.1:8000/vanilla-app/get-random/eden
    path("is-correct-random/<str:param1>/<str:param2>", views.isCorrectRandom, name="is-correct-random"), # http://127.0.0.1:8000/vanilla-app/is-correct-random/eden/eden
]