import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # Create the fake data for the entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.simple_profile()['mail']

        # Create the new user entry
        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
