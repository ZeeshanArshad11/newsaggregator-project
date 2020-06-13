import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from django.contrib import messages
from .models import Headline
import urllib3


urllib3.disable_warnings()
# Create your views here.
def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://metrowatch.com.pk/"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class":"pb-5 mb-10 block-post-smallrow col-lg-7 col-md-7 col-sm-16 col-xs-16 pl-0 pr-0"})
    #News = soup.find_all('li')
    for artcile in News:
        main = artcile.find_all('a')[0]
        link = main['href']
        image_src = str(main.find('img')['srcset']).split(" ")[-4]
        title = artcile.find_all('a')[1]
        if not Headline.objects.get(url = link):
            new_headline = Headline()
            new_headline.title = title.text
            new_headline.url = link
            new_headline.image = image_src
            new_headline.save()
    messages.info(request, "Your Record display successfully")
    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
    'object_list': headlines,
    }
    return render(request, "news/home.html", context)
