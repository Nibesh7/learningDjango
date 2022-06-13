from django.shortcuts import redirect, render
from .forms import NewuserForm

def register(request):
    if request.method =='POST':
        form = NewuserForm(data=request.POST)
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
