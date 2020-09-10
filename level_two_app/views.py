from django.shortcuts import render
from level_two_app.models import Users
# Create your views here.
def index(request):
    return render(request,'level_two_app/index.html')

def users(request):
    users_dict ={'list_users': Users.objects.all(), 'count': Users.objects.count()}
    return render(request, 'level_two_app/users.html', context = users_dict )