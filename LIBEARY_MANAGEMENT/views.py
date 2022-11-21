from ast import If
from pyexpat import model

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from LIBEARY_MANAGEMENT.forms import SignUpForm, Userupdate ,profileupdate
from GALLERY.models import image
from GALLERY.models import courser
from PROFILE.models import profile
from django.contrib.auth.decorators import login_required
from MYBOOK.models import bookapp

# Create your views here.
def home(request): 
	return render(request, 'home.html', {})

def signup_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('home')
	else: 
		form = SignUpForm() 

	context = {'forms': form}
	return render(request, 'signup.html', context)

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('home') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'login.html', {})

@login_required(login_url="/login/")
def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('home')


@login_required(login_url="/login/")
def edit_profile(request):
	if request.method =='POST':
		u_form = Userupdate(request.POST, instance= request.user)
		p_form = profileupdate(request.POST,request.FILES, instance= request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			u_form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('profile')
	else: 		#passes in user information 
		u_form = Userupdate(instance= request.user) 
		p_form = profileupdate(instance= request.user.profile) 

	context = {'u_form': u_form,'p_form':p_form}
	return render(request, 'edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})


@login_required(login_url="/login/")
def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('home')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'change_password.html', context)

@login_required(login_url="/login/")
def register(request):
	if request.method =='POST':
		stud_id=request.POST.get("stud")
		email=request.POST.get("mail")
		number=request.POST.get("num")
		gender=request.POST.get("gender")
		dob=request.POST.get("dob")
		branch=request.POST.get("branch")
		semister=request.POST.get("semister")
		image=request.POST.get("img")

		stu=profile(stud_id=stud_id,number=number,gender=gender,dob=dob,branch=branch,semister=semister,photo=image,email=email)
		stu.save()
	return render(request, 'registration.html')



def gallery(request):
    img=image.objects.all()
    

    return render(request,"gallery.html",{"img":img})
def cour(request):
    slider=courser.objects.all()
    

    return render(request,"base.html",{"slider":slider})
	
@login_required(login_url="/login/")
def profil(request):
	
		
    return render(request,"profile.html")

def bookentry(request): 
	if request.method =='POST':
		usr=request.user
		stud_id=request.POST.get("stud")
		book_name=request.POST.get("book")
		auther_name=request.POST.get("auther")
		

		book=bookapp(user=usr,stud_id=stud_id,book_name=book_name,auther_name=auther_name)
		book.save()
		
	return render(request, 'book_entry.html', {})
def bookshow(request): 
	

	data=bookapp.objects.filter(user=request.user)
	return render(request, 'book_show.html', {'data':data})
