from django.conf.urls import url
from views import index, loginvalidate, registervalidate, success, logout, zipupdate, register, community, adoption, editprofile, updateprofile, profilepage, addpet
from . import views
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^loginvalidate$', loginvalidate, name='loginvalidate'),
    url(r'^registervalidate$', registervalidate, name='registervalidate'),
    url(r'^success$', success, name='success'),
    url(r'^register$', register, name='register'),
    url(r'^community$', community, name='community'),
    url(r'^adoption$', adoption, name='adoption'),
    url(r'^logout$', logout, name='logout'),
    url(r'^zipupdate$', zipupdate, name='zipupdate'),
    url(r'^editprofile$', editprofile, name='editprofile'),
    url(r'^updateprofile$', updateprofile, name='updateprofile'),
    url(r'^profilepage$', profilepage, name='profilepage'),
    url(r'^addpet$', addpet, name='addpet')
]
