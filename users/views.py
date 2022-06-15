from django.shortcuts import redirect, render
from .forms import NewuserForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form = NewuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('myapp/products')
        else:
            print(form.data['email'],form.data)
    form = NewuserForm()
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')