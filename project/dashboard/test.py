import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

# your imports, e.g. Django models
from .models import *

if __name__ == '__main__':
    # e.g. add a new location
    # l = Instagram()
    # l.name = 'Berlin'
    # l.save()

    # this is an example to access your model
    instagram = Instagram.objects.all()
    print(instagram)

    # # e.g. delete the location
    # berlin = Location.objects.filter(name='Berlin')
    # print berlin
    # berlin.delete()
