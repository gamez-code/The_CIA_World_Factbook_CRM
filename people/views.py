from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from people.forms import RegisterForm
from people.models import Person
# Create your views here.

@csrf_protect
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        person = Person.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            father=data['father'],
            active=data['active']
        )
        for country in data['nacionality']:
            person.nacionality.add(country)
        return JsonResponse(
            {
                'name': person.first_name,
                'father': str(person.father),
                'nacionality': ', '.join([str(country) for country in person.nacionality.all()]),
                'active': person.active,
            }
        )
    return render(request, "people/register.html", {'form': form})
