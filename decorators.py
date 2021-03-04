from django.shortcuts import render, redirect


def security(view_name):
    """Checks if the user agreed conditions to run the website"""
    def wrapper(request,*args, **kargs):
        condition_accepted = request.session.get('conditions_accepted', False)
        if not condition_accepted:
            return redirect('requirements')
        else:
            return view_name(request, *args, **kargs)
    return wrapper
