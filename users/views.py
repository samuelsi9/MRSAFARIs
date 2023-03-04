from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from users.models import Message
from users.forms import MessageForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profileupdate') 
           
        else:  
            messages.success(request, "Une erreur s'est produite lors de la connexion,verifier votre nom utilisateur et mot de pass .Et essayez à nouveau... ")     
            return redirect('login')
        
    else:
         return render(request, 'users/login.html')

def logout_user(request):
    logout(request)     
    messages.success(request,("You were logged out !!"))    
    return redirect('HOMES')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Bienvenue {username}   A  SAFARI TRAVEL !  Votre Compte a été Créé Avec Succès   ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
 
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre compte a été actualisé !')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html',context)


def profileupdate(request):

    return render(request, 'users/profileupdate.html')



@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            try:
                recipient_user = User.objects.get(username=recipient)
            except User.DoesNotExist:
                messages.error(request, f'User "{recipient}" does not exist')
                return redirect('send_message')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            file_upload = form.cleaned_data['file_upload']
            sender = request.user
            message = Message.objects.create(
                recipient=recipient_user,
                subject=subject,
                message=message,
                file_upload=file_upload,
                sender=sender
            )
            messages.success(request, 'Message sent successfully')
            
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request,'users/send_message.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-date_sent')
    return render(request, 'users/inbox.html', {'messages': messages})

def view_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'users/view_message.html', {'message': message})


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('password_change_done')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

def password_change_done(request):
    return render(request, 'users/password_change_done.html')
@login_required
def admin_only_view(request):
    if request.user.is_superuser:
        # Render the admin-only page here
        return redirect('blog-home')
    else:
        # Redirect non-admin users to home page
        return redirect('HOMES')
    


