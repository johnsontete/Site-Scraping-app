from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .models import Scrapeinks
# Create your views here.

def scraper(request):
    
    if request.method == 'POST' and request.POST.get('scrape')!= "":
        req_link = request.POST.get('scrape')
        page = requests.get(req_link)
        if page:
            soup = BeautifulSoup(page.text,'html.parser')
            my_soup = soup.find_all('h3')

            for link in (my_soup):
                address = link.getText()
                name = link.string
                Scrapeinks.objects.create(address=address,name=name)
            link_data = Scrapeinks.objects.all()
            return render(request, 'links.html',{'page':link_data})
        else:
            return render(request, 'links.html',{'page':Scrapeinks.objects.all()})
    return render(request, 'links.html',{'page':Scrapeinks.objects.all()})


def clear(request):
    Scrapeinks.objects.all().delete()
    return HttpResponseRedirect('/links/')