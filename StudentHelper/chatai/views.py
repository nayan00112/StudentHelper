from django.shortcuts import render
from django.contrib import messages
import google.generativeai as genai


# import markdown
# def mtheb(your_text_string):
#     return markdown.markdown(your_text_string, extensions=['abbr', 'admonition', 'attr_list', 'codehilite', 'def_list', 'extra', 'fenced_code', 'footnotes', 'legacy_attrs', 'legacy_em', 'md_in_html', 'meta', 'nl2br', 'sane_lists', 'smarty', 'tables', 'toc', 'wikilinks'])
#     # return markdown.markdown(your_text_string, extensions=['abbr', 'admonition', 'attr_list', 'codehilite', 'def_list', 'extra', 'fenced_code', 'footnotes', 'legacy_attrs', 'legacy_em', 'md_in_html', 'meta', 'nl2br', 'sane_lists', 'smarty', 'tables', 'toc', 'wikilinks']).replace('\n', '<br>')

# Create your views here.

def getchatresponsehistory(c):
    GOOGLE_API_KEY = 'put_your_api'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(c)

    return [response.text, chat.history]

    
def letchat(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.method == "POST":
                c = request.POST["userchatmessage"]
                responsetext, historytext = getchatresponsehistory(c)
            return render(request, "chatai/chatpage.html", {'parts':historytext})
        else:
            messages.info(request, 'Login Required')
    return render(request, "chatai/chatpage.html")