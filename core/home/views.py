from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   peoples = [
       {'s no' : 1  ,  'name': 'Aadarsh' , 'age' : 20 },
        {'s no' : 2 ,'name': 'alok' , 'age' : 10 },
      {'s no' : 3 ,'name': 'vivrk' , 'age' : 40 },
      {'s no' : 4 ,'name': 'deepanshu' , 'age' : 30 },
      {'s no' : 5 ,'name': 'Abhishek' , 'age' : 78 },  
      
   ]
   vegetables = ['tomato' , 'potato' , 'reddish']
    
   
   return render(request , "home.html" , context = {'page': 'Django 2023 tutorial', 'peoples' : peoples ,'vegetables' : vegetables })



def about(request):
    context = {'page' : 'about'}
    return render(request , "about.html", context )

def contact(request):
    context = {'page' : 'contact'}
    return render( request , "contact.html", context)

def success_page(request):
    return HttpResponse("<h2>Hey, this is a success page</h2>")


