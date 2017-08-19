#from django.shortcuts import render
# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person , Article
from django.views import View
from django.views.generic import TemplateView , YearArchiveView

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
	return render(request, 'hello_world.html', {
        	'current_time': str(datetime.now()),
    	})
def home(request):
    person_list = Person.objects.all()
    return render(request, 'home.html', {
        'person_list': person_list,
    })

class MyView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse('Hello, World!')

class AboutView(TemplateView):
	template_name = "about.html"

class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
