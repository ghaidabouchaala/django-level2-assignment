from django.shortcuts import render
from level_two_app.models import Users
from level_two_app.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'level_two_app/index.html')

def users(request):
   
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True  )
            return index(request)
        else:
            print('Error form invalid')
    
    return render(request, 'level_two_app/users.html', {'form':form})

def form_name_view(request):
    form = forms.FormName() 
    print("before")
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print("Name  " + form.cleaned_data['name'])
            print("Email  " + form.cleaned_data['email'])
            print("Text  " + form.cleaned_data['text'])

    return render(request, 'level_two_app/forms_page.html', {'form':form}) 