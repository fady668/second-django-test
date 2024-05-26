from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import *

# Home Page
def home(request):
    records = Record.objects.all()

    # Login Check
    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']
        
        user = authenticate(request, username=username, password=password)  # Pass as keyword arguments
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been logged in :)')
            return redirect('Home')
        else:
            messages.error(request, 'There was an error, please try again')  # Change to error message
            return redirect('Home')
    else:
        return render(request, 'home.html', {'records':records})


# logout Page
def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been logged out :(')
    return redirect('Home')

# Register Page
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(request, username=username , password=password)
        login(request, user)
        messages.success(request, 'You Have Successfully Registering :|')
        return redirect('Home')
    else :
        form = SignUpForm()
    
    return render(request, 'register.html', {'form':form})
    
# Show Records
def record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        context = {'record_details':record,
                   'id':pk}
        return render(request, 'record.html', context)
    else:
        messages.success(request, 'You Must logging in befor Visit any Record')
        return redirect('Home')
    
# Add Records
def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordFrom(request.POST)
        if request.method == 'POST':
            if form.is_valid:
                form.save()
                messages.success(request, 'Record Added Successfully...')
                return redirect('Home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'You Must logging in befor add Records')
        return redirect('Home')
    
# Update Records
def update_record(request, pk):
    if request.user.is_authenticated:
        updated_record = Record.objects.get(id=pk)
        if request.method == 'POST':
            form = AddRecordFrom(request.POST, instance=updated_record)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Updated Successfully...')
                return redirect('Home')
        else:
            form = AddRecordFrom(instance=updated_record)
        return render(request, 'update_record.html', {'updated_record': updated_record, 'form': form})
    else:
        messages.success(request, 'You Must log in before updating any Record')
        return redirect('Home')
    
    
# Delete Records
def delete_record(request, pk):
    if request.user.is_authenticated:
        deleted_record = Record.objects.get(id=pk)
        deleted_record.delete()
        messages.success(request, 'Record Deleted Successfully...')
        return redirect('Home')
    else:
        messages.success(request, 'You Must logging in befor Delete any Record')
        return redirect('Home')