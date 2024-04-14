from django.shortcuts import render
import requests
import json


def ques(kw):
    api = "3e7626aae282444b87411b2d86eaa99d"
    # https://newsapi.org
    url = f'https://newsapi.org/v2/everything?q={kw}&apiKey={api}'
    response = requests.get(url)
    if response.status_code == 200:
        a = response.text
        art = json.loads(a)
    else:
        art = "Not Found!"
    return art

def getBookInfo(kw):
    url = f"https://www.googleapis.com/books/v1/volumes?q={kw}"
    response = requests.get(url)
    if response.status_code == 200:
        a = response.text
        art = json.loads(a)
    else:
        art = "Not Found!"
    return art

# Create your views here.
def faqs(request):
    context = {
        "FAQs" : "active",
    }
    return render(request, "blogs/faqs.html", context)

def about_us(request):
    context = {
        "About_us" : "active",
    }
    return render(request, "blogs/about_us.html", context)

def contact_us(request):
    context = {
        "Contact_us" : "active",
    }
    return render(request, "blogs/contact_us.html", context)

def motivation(request):
    context = {
        "Motivation" : "active",
    }
    return render(request, "blogs/motivation.html", context)

def articalsread(request):
    if request.method == "POST":
        kw = request.POST["kw"]
        art = ques(kw)
    else:
        art = ques("india news")
    context = {
        "data": art,
    }
    return render(request, "blogs/articalsread.html", context)

def getbookdetails(request):
    if request.method == "POST":
        kw = request.POST["kw"]
        art = getBookInfo(kw)
    else:
        art = getBookInfo("Motivation")
    context = {
        "json_data": art,
    }
    return render(request, "blogs/getbookdetails.html", context)
