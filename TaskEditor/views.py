from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'taskeditor/index.html')
    #return HttpResponse("WelcomeToTaskList")

def aboutPageView(request) :
    return render(request, 'taskeditor/about.html')
    #return HttpResponse("This program will help you manage all the school tasks that are keeping you busy and stressed.")

def seeTaskPageView(request) :
    return render(request, 'taskeditor/seetask.html')
    #return HttpResponse("This page will be where your tasks are displayed")

def createTaskPageView(request) :
    return render(request, 'taskeditor/createtask.html')
    #return HttpResponse("This page will be where you create a new task")

def editTaskPageView(request) :
    return render(request, 'taskeditor/edittask.html')
    #return HttpResponse("This page will be where you edit an exisiting task")

def deleteTaskPageView(request) :
    return render(request, 'taskeditor/deletetask.html')
    #return HttpResponse("This page will be where you delete an exisiting task")