from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^date$',views.date,name = 'date'),
    url(r'^github$',views.github,name='search'),
    url(r'^movie$',views.movie,name='movie'),
    url(r'^youtube$',views.search_youtube,name='youtube'),
    url(r'^netflix$',views.netflix,name='netflix')
]