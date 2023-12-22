from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
# Create your views here.
class News_view(DetailView):
    model = Articles
    template_name = 'main/news_view.html'
    context_object_name = 'article'

def Mainpage(request):
    return render(request, 'main/index.html')


def About(request):
    return render(request, 'main/About_us.html')

def News(request):
    news = Articles.objects.order_by('-time')
    return render(request, 'main/news.html', {'news':news})


def Contacts(request):
    return render(request, 'main/Contacts.html')
