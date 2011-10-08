import random
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template
from kennedy.models import *


def get_random_name(gender):
    if gender not in ['male', 'female']:
        return None
    
    fn = FirstName.objects.filter(gender=gender).order_by('?')[0].name
    nn = '"%s"' % NickName.objects.filter(gender=gender).order_by('?')[0].name
    ln = LastName.objects.all().order_by('?')[0].name
    if gender == 'male':
        suffixes = ['Jr.', 'II', 'III']
        try:
            suffix = suffixes[random.randrange(0,7)]
        except IndexError:
            suffix = ''
    else:
        suffix = ''
    return u' '.join([fn.strip(), nn.strip(), ln.strip(), suffix]).strip()
    


def index(request):
    context = {}
    if request.method == 'GET':
        first_name = request.GET.get('first_name', None)
        gender = request.GET.get('gender', None)
        if first_name and gender:
            context.update({'first_name': first_name, 'gender': gender,})
            kennedy_name = get_random_name(gender)
            if kennedy_name:
                context.update({'kennedy_name': kennedy_name})
            
    return direct_to_template(request, 'kennedy/index.html', context)
