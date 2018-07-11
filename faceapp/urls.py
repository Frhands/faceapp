from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faceapp/upload1/',views.upload1,name="upload1"),
    path('faceapp/get_face_feat/', views.ret_gender_and_age, name="upload2")
]