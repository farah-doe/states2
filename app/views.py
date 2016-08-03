from django.shortcuts import render, redirect

from django.http import HttpResponse
from app.models import State, City, StateCapital
from app.forms import CitySearchForm, CityCreate, CityEdit, StateCreate, StateEdit 
from django.contrib.auth.decorators import login_required
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View

from django.views.generic.list import ListView  
from django.views.generic.detail import DetailView

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect 
from django.utils.decorators import method_decorator


from django.http import HttpResponse, HttpResponseRedirect

 
# Create your views here.


@login_required
def delete_city(request, pk):

    City.objects.get(pk=pk).delete()

    return redirect('/city_list/')


@login_required
def state_edit(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    form = EditState(request.POST or None, instance=state)

    context['form'] = form 

    if form.is_valid():
        form.save()

        return redirect('/state_list/')

    return render(request, 'state_edit.html', context) 

@login_required
def create_state(request):

    context = {}

    form = StateCreate(request.GET)

    context['form'] = form 

    if form.is_valid(): 
        form.save()

    return render(request, 'create_state.html', context)








def create_city(request):

    context = {}
    
    form = CityCreate(request.GET)

    context['form'] = form 

    if form.is_valid():
        form.save()

    return render(request, 'create_city.html', context)



@login_required
def city_edit(request, pk):
    
    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city 

    if request.method == 'POST':

        form = CityEdit(request.POST or None, instance=city)

        context['form'] = form
    
        if form.is_valid():
            form.save()

        return redirect('/city_list/')

    return render(request, 'city_edit.html', context)


class CityListView(ListView):
    model = City
    template_name = "city_list.html"
    context_object_name = "cities"

    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        print context
        context['states'] = State.objects.all()
        context['cities'] = City.objects.filter(state__pk=self.request.GET.get('state_number', 120))

        return context 

class CityDetailView(DetailView):
    model = City 
    template_name = "city_list.html"
    context_object_name = "city"



class StateListView(ListView):
    model = State 
    template_name = "state_list.html"
    context_object_name = "states"


class StateDetailView(DetailView):
    model = State
    template_name = "state_detail.html"
    context_object_name = "state"



def capital_detail(request, pk):

    context = {}

    context['capital'] = StateCapital.objects.get(pk=pk)

    return render(request, 'capital_detail.html', context)

def capital_list(request):

    context = {}

    context['capitals'] = StateCapital.objects.all()

    return render(request, 'capital_list.html', context)


def contact(request):
    
    context ={}

    contact_details = Contact.objects.all()

    context['contact_details'] = contact_details

    return render(request, 'contact.html', context)


def city_list(request):

    # state_pk = request.GET('state', 140)

    state_number = request.GET.get('state_number', 50)

    print request.GET

    print state_number

    context = {}

    context['states'] = State.objects.all()

    context['cities'] = City.objects.filter(state__pk=state_number)

    print context 

    return render(request, 'city_list.html', context)



def city_listall(request):

    context = {}

    context['cities'] = City.objects.all()

    return render(request, 'city_listall.html', context)



def city_detail(request, pk):

    context = {}

    state_number = request.GET.get('state_number', 120)
    city = City.objects.get(pk=pk)

    context['city'] = city 

    return render(request, 'city_detail.html', context)


def state_detail(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state 

    return render(request, 'state_detail.html', context)


def state_list(request):

    context = {}

    states = State.objects.all()

    context['states'] = states

    return render(request, 'state_list.html', context)


def template_view(request):
   
    context = {}

    AA = State.objects.all()

    context['CC'] = AA


    return render(request, 'base.html', context)




def first_view(request, starts_with):

    states = State.objects.all()

    text_string = ''

    for state in states:
        
        cities = state.city_set.filter(name_startswith=starts_with)

        for city in cities:

            print city.name

            text_string += 'state:%s -- city:%s <br>' % (state.name, city.name)

    return HttpResponse(text_string)


def list(request):

    context = {}

    states = State.objects.all()

    context['states'] = states

    # text_string = ''

    # for state in states:
        
    #     cities = state.city_set.all()   

    #     for city in cities:

    #         print city.name 

    #         text_string += 'state:%s -- city: %s <br>' % (state.name, city.name)

    return render(request, 'list.html', context)


def detail(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render(request, 'detail.html', context)



    # city = City.objects.get(pk=pk)

    # text_string = ''
    
    # text_string += 'city: %s --  latitude:%s -- longitude:%s -- county:%s -- zipcode:%s <br>' % (city.name, city.latitude, city.longitude, city.county, city.zipcode)

    # return HttpResponse(state)

def city_search(request):

    context = {}

    form = CitySearchForm(request.GET)

    context['form'] = form 

    if form.is_valid():
        state = form.cleaned_data.get("state", "Utah")
        city = form.cleaned_data.get("city", "Orem")
        
        cities = City.objects.filter(name__iexact=city, state__name=state)
        context['cities'] = cities
        context['form'] = form

    else:
        context['form'] = form 

    return render(request, 'city_search.html', context)



# def city_search_old(request):

#     context = {}

#     form = CitySearchForm(request.GET)

#     print form.data

#     print form.is_valid()

#     print form.cleaned_data

#     state = form.cleaned_data.get('state', 'Utah')
#     city = form.cleaned_data.get('city', 'Orem')

#     print "%s is a state" % state
#     print "%s is a city" % city 

#     cities = City.objects.filter(name=city, state__name=state)

#     context['cities'] = cities 

#     context['form'] = form 

#     return render(request, 'city_search.html', context)



def city_search_post(request):

    context = {}

    context['states'] = State.objects.all()

    form = CitySearchForm(request.POST)

    context['form'] = form 
 
    if request.method == 'POST':
       
        if form.is_valid():
            city = form.cleaned_data.get('city', 'Orem')
            state = form.cleaned_data.get('state', 'Utah')

            context['cities'] = City.objects.filter(name=city, state__name=state)

    return render(request, 'city_search_post.html', context)




