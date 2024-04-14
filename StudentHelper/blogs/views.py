from django.shortcuts import render
import requests
import json


# Create your views here.
def faqs(request):
    return render(request, "blogs/faqs.html")

def about_us(request):
    return render(request, "blogs/about_us.html")

def contact_us(request):
    return render(request, "blogs/contact_us.html")

def motivation(request):
    return render(request, "blogs/motivation.html")


def articalsread(request):
    def ques(kw):
        api = "your_api"
        # https://newsapi.org
        url = f'https://newsapi.org/v2/everything?q={kw}&apiKey={api}'
        response = requests.get(url)
        if response.status_code == 200:
            a = response.text
            art = json.loads(a)
        else:
            art = "Not Found!"
        return art

    if request.method == "POST":
        kw = request.POST["kw"]
        art = ques(kw)
    else:
        art = ques("india news")
    return render(request, "blogs/articalsread.html", {"data": art})

    