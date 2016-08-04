from django import forms 
from django.core.urlresolvers import reverse 
from django.core.validators import RegexValidator

from django.utils.html import escape

# crispy imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div, Field  
from crispy_forms.bootstrap import FormActions 

# import models
from app.models import State, City




# class CityCreate(forms.ModelForm):
#     class Meta:
#         model = City 



class CitySearchForm(forms.Form):
   # alphanumeric = RegexValidator(r'^[a-zA-Z]+$')
    letters_only = RegexValidator(r'^[a-zA-Z]+$',
                                'Only letters are allowed!'
                                )

    city = forms.CharField(required=True, 
                            initial="Orem", 
                            validators=[letters_only]
                            )
    
    state = forms.CharField(required=True,              
                             initial='Utah', 
                             validators=[letters_only]
                             )

    def __init__(self, *args, **kwargs):
        super(CitySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_action = 'city_search'
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                    Div('city', css_class='col-sm-5 col-md-5'),
                    Div('state', css_class='col-sm-5 col-md-5'),
                    Div(
                    FormActions(
                        Submit('submit', 'Search')
                        ),
                    css_class='col-sm-2 col-md-2', 
                    style='margin-top:25px;'
                    )
            )


            

class CityEdit(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityEdit, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('city_edit', kwargs={'pk': self.instance.pk})
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                    Div('state', 'name', 'county', css_class='col-sm-6'), 
                    Div('latitude', 'longitude', 'zipcode', css_class='col-sm-6'),
                    Div(FormActions(Submit('submit', 'Save')), css_class='col-sm-12'),       
            )

class StateEdit(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StateEdit, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('state_edit', kwargs={'pk': self.instance.pks})
        self.helper.layout = Layout(
                    Div(
                        Div('name', css_class='col-md-10'),
                        Div('abbreviation', css_class='col-md-2'),
                        css_class='row'
                    ),
                    Div(
                        Div(FormActions(Submit('submit', 'Submit')), css_class="col-md-12"),
                        css_class='row'
                    )
            )


class StateCreate(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'


class CityCreate(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CityCreate, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'get'
            self.helper.form_action =  'create_city'

            self.helper.layout=Layout(
                        Div('state', 'name', 'county', css_class='col-sm-6'), 
                        Div('latitude', 'longitude', 'zipcode', css_class='col-sm-6'),
                        Div(FormActions(Submit('submit', 'Save')), css_class='col-sm-12'),       
                        )

    # NOT DONE WITH CODE FOR CITYCREATE !!!!!!!



                         
                            
                
                    
                

        
            

    # STATES = [['Texas', 'Utah'], ['California', 'Colorado']]


    # STATES =(
    #             ('1', 'Texas'),
    #             ('2', 'Utah'),
    #             ('3', 'California')
    #     )

    # STATES = State.objects.all().values_list('id', 'name')

    # print STATES1
    # print STATES2 

    # state_select = forms.ChoiceField(choices=STATES)

    # Orem, Utah is a default feature

