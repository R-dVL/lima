from django.shortcuts import redirect


def redirect_to_inventory(request):
    return redirect('/inventory/')