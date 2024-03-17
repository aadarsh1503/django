from django.shortcuts import render, redirect
from .models import *  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Student, SubjectMarks
 
@login_required(login_url="/login1_page/")
def receipes(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = request.FILES.get('receipe_image')
        receipe_price=data.get('receipe_price')

      
        
        Receipe.objects.create(
             receipe_name=receipe_name,
             receipe_descriptions=receipe_descriptions, 
             receipe_image=receipe_image,
             receipe_price=receipe_price
             )        

        return redirect('/receipes/')
    
    queryset=Receipe.objects.all()


    if request.GET.get('search') :
     queryset = queryset.filter(receipe_name__icontains= request.GET.get('search'))

    context={'receipes': queryset}
    return render(request, 'receipes.html', context)

@login_required(login_url="/login_page/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
       
        data = request.POST
        files = request.FILES  

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = files.get('receipe_image')  
        receipe_price=data.get('receipe_price')

        queryset.receipe_name = receipe_name
        queryset.receipe_descriptions = receipe_descriptions
        queryset.receipe_price=receipe_price

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()

        return redirect('/receipes/')

    context = {'receipes': queryset}
    return render(request, 'update_receipe.html', context)


  

@login_required(login_url="/login_page/")
def delete_receipe(request,id):
    print(id)
    queryset=Receipe.objects.get(id=id)
    
    queryset.delete()
    return redirect('/receipes/')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login_page/')
            

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login_page/')
        
        else: 
            login(request, user)
            return redirect('/user_receipe/')


    return render(request, 'login.html')

    

def register(request): 
 if request.method == 'POST':
     First_Name = request.POST.get('First_Name')
     Last_Name = request.POST.get('Last_Name')
     UserName = request.POST.get('username')
     Password = request.POST.get('password')

     if User.objects.filter(username=UserName).exists():
            messages.info(request, "Username Already Exists")
            return redirect('/register/')

     user=User.objects.create(
       first_name=First_Name,
       last_name=Last_Name,
       username=UserName,
       
       )
     

     user.set_password(Password)
     user.save()
     messages.info(request, "Account Created")

     return redirect('/login_page/')
 
     
 return render(request, 'register.html')
 
def logout_page(request):
    logout(request)
    return redirect('/login_page/')


from django.db.models import Q , Sum


def get_student(request):
    queryset=Student.objects.all()
    


    if request.GET.get('search') :
     search = request.GET.get('search')
     queryset = queryset.filter(
         Q(student_name__icontains = search)|
         Q(department__department__icontains = search)|
         Q(student_age__icontains = search)|
         Q(student_email__icontains = search)|
         Q(student_id__student_id__icontains = search)
        )
    
    paginator = Paginator(queryset, 25) 

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)


    return render(request , 'students.html',{'queryset': page_obj})
   

 


def see_marks(request, student_id):
    student = get_object_or_404(Student, student_id__student_id=student_id)
    queryset = SubjectMarks.objects.filter(student=student)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    current_rank= -1
    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i=1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
           current_rank=i
           break
        i=i+1

    
    return render(request, 'see_marks.html', {'student': student, 'queryset': queryset , 'total_marks' : total_marks , 'current_rank' : current_rank})


def rate_receipe(request, receipe_id):
    if request.method == 'POST':
        
        rating = int(request.POST.get('rating'))

      
        receipe = Receipe.objects.get(id=receipe_id)
        receipe.rating = rating
        receipe.save()

        return redirect('recipe_page')  

   
    return render(request, 'rate_receipe.html') 

def user_receipe(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = request.FILES.get('receipe_image')
        receipe_price=data.get('receipe_price')

      
        
        Receipe.objects.create(
             receipe_name=receipe_name,
             receipe_descriptions=receipe_descriptions, 
             receipe_image=receipe_image,
             receipe_price=receipe_price
             )        

        return redirect('/user_receipe/')
    
    queryset=Receipe.objects.all()


    if request.GET.get('search') :
     queryset = queryset.filter(receipe_name__icontains= request.GET.get('search'))

    context={'receipes': queryset}
    return render(request, 'user_receipe.html', context)



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def login1_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Changed to 'username'
        password = request.POST.get('password')  # Changed to 'password'

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login1_page/')
            
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login1_page/')
        else: 
            login(request, user)
            return redirect('/receipes/')

    return render(request, 'login1.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register1(request): 
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        UserName = request.POST.get('username')  # Changed to 'username'
        Password = request.POST.get('password')  # Changed to 'password'

        if User.objects.filter(username=UserName).exists():
            messages.info(request, "Username Already Exists")
            return redirect('/register1/')

        user = User.objects.create(
            first_name=First_Name,
            last_name=Last_Name,
            username=UserName,
        )

        user.set_password(Password)
        user.save()
        messages.info(request, "Account Created")

        return redirect('/login1_page/')
    else:
        return render(request, 'register1.html')

from django.shortcuts import render, redirect
from .models import Burger

@login_required(login_url="/login1_page/")
def burger(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = request.FILES.get('receipe_image')
        receipe_price=data.get('receipe_price')
       
        Burger.objects.create(
            receipe_name=receipe_name,
            receipe_descriptions=receipe_descriptions, 
            receipe_image=receipe_image,
            receipe_price=receipe_price
        )
        return redirect('/burger/')  
    
    
    burger = Burger.objects.all()
    context = {'burger': burger}
    return render(request, 'burger.html', context)

def delete_receipe1(request,id):
    print(id)
    queryset=Burger.objects.get(id=id)
    queryset.delete()
    return redirect('/burger/')

@login_required(login_url="/login1_page/")
def update_receipe1(request, id):
    queryset = Burger.objects.get(id=id)

    if request.method == "POST":
       
        data = request.POST
        files = request.FILES  

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = files.get('receipe_image')  
        receipe_price=data.get('receipe_price')

        queryset.receipe_name = receipe_name
        queryset.receipe_descriptions = receipe_descriptions
        queryset.receipe_price=receipe_price

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()

        return redirect('/burger/')

    context = {'burger': queryset}
    return render(request, 'update_receipe1.html', context)

@login_required(login_url="/login1_page/")
def rate_receipe1(request, receipe_id):
    if request.method == 'POST':
        
        rating = int(request.POST.get('rating'))

        
        burger= Burger.objects.get(id=receipe_id)
        burger.rating = rating
        burger.save()

        return redirect('recipe_page')  

    
    return render(request, 'rate_receipe1.html')  


from django.shortcuts import render, redirect
from .models import Pizza

@login_required(login_url="/login1_page/")
def pizza(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = request.FILES.get('receipe_image')
        receipe_price=data.get('receipe_price')
       
        Pizza.objects.create(
            receipe_name=receipe_name,
            receipe_descriptions=receipe_descriptions, 
            receipe_image=receipe_image,
            receipe_price=receipe_price
        )
        return redirect('/pizza/')  
    
    
    pizza = Pizza.objects.all()
    context = {'pizza': pizza}
    return render(request, 'pizza.html', context)

@login_required(login_url="/login1_page/")
def delete_receipe_pizza(request,id):
    print(id)
    queryset=Pizza.objects.get(id=id)
    queryset.delete()
    return redirect('/pizza/')

@login_required(login_url="/login1_page/")
def update_receipe_pizza(request, id):
    queryset = Pizza.objects.get(id=id)

    if request.method == "POST":
       
        data = request.POST
        files = request.FILES  

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = files.get('receipe_image')  
        receipe_price=data.get('receipe_price')

        queryset.receipe_name = receipe_name
        queryset.receipe_descriptions = receipe_descriptions
        queryset.receipe_price=receipe_price

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()

        return redirect('/pizza/')

    context = {'pizza': queryset}
    return render(request, 'update_receipe_pizza.html', context)

def user_burger(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = request.FILES.get('receipe_image')
        receipe_price=data.get('receipe_price')

      
        
        Burger.objects.create(
             receipe_name=receipe_name,
             receipe_descriptions=receipe_descriptions, 
             receipe_image=receipe_image,
              receipe_price=receipe_price
             )        

        return redirect('/user_burger/')
    
    queryset=Burger.objects.all()


    if request.GET.get('search') :
     queryset = queryset.filter(receipe_name__icontains= request.GET.get('search'))

    context={'burger': queryset}
    return render(request, 'user_burger.html', context)

def user_pizza(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = request.FILES.get('receipe_image')
        receipe_price=data.get('receipe_price')

      
        
        Pizza.objects.create(
             receipe_name=receipe_name,
             receipe_descriptions=receipe_descriptions, 
             receipe_image=receipe_image,
             receipe_price=receipe_price
             )        

        return redirect('/user_pizza/')
    
    queryset=Pizza.objects.all()


    if request.GET.get('search') :
     queryset = queryset.filter(receipe_name__icontains= request.GET.get('search'))

    context={'pizza': queryset}
    return render(request, 'user_pizza.html', context)

def payment(request):
    if request.method == 'POST':
        
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        cardname = request.POST.get('cardname')
        cardnumber = request.POST.get('cardnumber')
        expmonth = request.POST.get('expmonth')
        expyear = request.POST.get('expyear')
        cvv = request.POST.get('cvv')
        sameadr = request.POST.get('sameadr')

        
        order = Payment.objects.create(
            firstname=firstname,
            email=email,
            address=address,
            city=city,
            state=state,
            zip=zip_code,
            cardname=cardname,
            cardnumber=cardnumber,
            expmonth=expmonth,
            expyear=expyear,
            cvv=cvv,
            sameadr=sameadr
        )

        

    return render(request, 'payment.html')



from django.shortcuts import render, redirect
from .models import Burger  # Import your Burger model here

def addcart(request, id):
    # Fetch the burger based on the provided ID
    burger = Burger.objects.get(id=id)

    if request.method == "POST":
        # Handle POST request
        data = request.POST
        files = request.FILES  

        receipe_name = data.get('receipe_name')
        receipe_descriptions = data.get('receipe_descriptions')
        receipe_image = files.get('receipe_image')  
        receipe_price = data.get('receipe_price')

        # Create or update the cart in session
        cart = request.session.get('cart', [])
        cart.append({
            'id': id,
            'receipe_name': receipe_name,
            'receipe_descriptions': receipe_descriptions,
            'receipe_price': receipe_price,
            'receipe_image': receipe_image.url if receipe_image else None
        })
        request.session['cart'] = cart

        # Redirect back to the same page after adding the recipe to the cart
        return redirect('addcart', id=id)

    # If it's a GET request, render the addcart.html template with the current burger and cart content
    return render(request, 'addcart.html', {'burger': burger, 'cart': request.session.get('cart', [])})


