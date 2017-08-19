from django.conf.urls import url

from . import views
from polls.views import MyView , AboutView , ArticleYearArchiveView
from django.views.generic.dates import ArchiveIndexView
from polls.models import Article

urlpatterns = [
    url(r'^mine/$', MyView.as_view()),
    url(r'^about/$', AboutView.as_view()),
	url(r'^archive/$',ArchiveIndexView.as_view(model=Article, date_field="pub_date"), name="article_archive"),
	url(r'^(?P<year>[0-9]{4})/$', ArticleYearArchiveView.as_view(), name="article_year_archive"),
]
