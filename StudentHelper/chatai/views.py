from django.shortcuts import render

def letchat(request):
    return render(request, "chatai/chatpage.html")