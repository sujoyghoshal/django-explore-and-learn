from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h3>Hey I am a Django Server.</h3>")
    peoples=[
        {'name':'Sujoy Ghoshal', 'age':21},
        {'name':'Subhadip', 'age':17},
        {'name':'Sumit', 'age':24},
        {'name':'Souvik', 'age':8}
    ]
    header="This is Template is returned by Django Server"
    vagetables=["Tomato","potato","Mango "]
    return render(request,"index.html", context={'peoples':peoples,'header':header ,'vagetables':vagetables})




def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def sucess_page(request):
    print("*" * 10)
    return HttpResponse("<h4>This is the sucess page.</h4>")