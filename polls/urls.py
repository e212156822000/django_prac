from django.conf.urls import url

from . import views
from polls.views import MyView , AboutView

urlpatterns = [
    url(r'^mine/$', MyView.as_view()),
    url(r'^about/$', AboutView.as_view()),

]
