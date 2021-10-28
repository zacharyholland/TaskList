from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse("Welcome to TaskList")

def aboutPageView(request) :
    return HttpResponse("This program will help you manage all the school tasks that are keeping you busy and stressed.")

def seeTaskPageView(request) :
    return HttpResponse("This page will be where your tasks are displayed")

def createTaskPageView(request) :
    return HttpResponse("This page will be where you create a new task")

def editTaskPageView(request) :
    return HttpResponse("This page will be where you edit an exisiting task")