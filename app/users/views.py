from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    """
    Handle user login.

    If the request method is POST, authenticate the user with the provided
    username and password. If authentication is successful, log the user in
    and redirect to the 'next' URL if provided, otherwise redirect to the home page.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered login page or redirect to the next URL.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            return redirect(next_url or 'home')
        else:
            messages.error(request, 'Credenciales incorrectas')
    return render(request, 'login.html')

def logout_view(request):
    """
    Handle user logout.

    Log out the user and redirect to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        Redirect to the login page.
    """
    logout(request)
    return redirect('login')  # Redirect to the login URL after logout
