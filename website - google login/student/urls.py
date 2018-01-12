from django.conf.urls import url
from . import views

urlpatterns = [
    # /student/
    url(r'^$', views.index, name='index'),

    # /student/grace
    url(r'^grace', views.grace, name='grace'),

    # /student/face
    url(r'^face', views.face, name='face')
]
