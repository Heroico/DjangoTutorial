from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #parameter name changed to "pk", to connect to Django's generic view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #parameter name changed to "pk", to connect to Django's generic view
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]