from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^advanced', views.advanced, name='advanced'),
    url(r'^results', views.results),
]