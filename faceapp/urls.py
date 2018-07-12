from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addface/', views.add_face),
    path('get_face_feat/', views.ret_gender_and_age),
    path('search/', views.search_face),
    path('pick/', views.pick_face),
    path('namelist/', views.get_namelist)
]
