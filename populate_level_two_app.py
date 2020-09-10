import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level_two_project.settings')


import django
django.setup()

import random
from level_two_app.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=10):
    
    for entry in range(N):

        fake_first_name =fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        users = Users.objects.get_or_create(first_name = fake_first_name, last_name =fake_last_name, email = fake_email)[0]


if __name__=='__main__':
    print("population script!")
    populate(20)
    print("population complete!")
