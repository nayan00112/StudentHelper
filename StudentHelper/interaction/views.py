from django.shortcuts import render
from django.contrib import messages
from .models import AddQuestions, AnsOfQue


def showque(request):
    if request.user.is_authenticated:
        data = AddQuestions.objects.all()
        return render(request, "interaction/dashbord.html", {"data" : data})
    else:
        messages.info(request, 'Login Required')
        return render(request, "interaction/dashbord.html")

def addquestion(request):
    data = AddQuestions.objects.filter(visiable = True)
    if request.method == "POST":
        if request.user.is_authenticated:
            que = request.POST["que"]
            loggeduser = str(request.user.id)
            aq = AddQuestions(question = que,questionownerid = loggeduser)
            aq.save()
            messages.info(request, 'saved question successfully!')
        else:
            messages.info(request, 'Login Required')
    return render(request, "interaction/add_questions.html", {"dataque" : data})

def addans(request, queid):
    qn= AddQuestions.objects.filter(id = queid, visiable = True)
    if request.method == "POST":
        if request.user.is_authenticated:
            ans = request.POST["ans"]
            loggeduser = str(request.user.id)
            getstrqid = queid
            a = AnsOfQue(qid = getstrqid, ansstr= ans ,ansownerid = loggeduser)
            a.save()
            messages.info(request, 'saved answer successfully!')
        else:
            messages.info(request, 'Login Required')
    answers = AnsOfQue.objects.filter(qid = queid, visiable = True)
    return render(request, "interaction/addand.html", {"qn":qn, "ansdata" : answers})
