from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if username or password:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Redirect to a success page.
                return redirect(request.POST['next'])
            else:
                # Return a 'disabled account' error message
                pass
        else:
            # Return an 'invalid login' error message.
            pass
    else:
        # Display login page
        context = {'next': request.GET['next']}
        return render(request, 'accounts/login.html', context)
