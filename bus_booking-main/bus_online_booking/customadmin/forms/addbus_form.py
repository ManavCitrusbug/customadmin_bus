# from xmlrpc.client import Transport
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from bus.models import Transport
from django.contrib.auth import get_user_model


class AddbusCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    # busname = forms.CharField(label="Enter The Busname", widget=forms.TextInput)
    # busnumber = forms.CharField(label="Enter The Busnumber", widget=forms.TextInput)
    # seats = forms.IntegerField(label="Enter The Seat", widget=forms.TextInput)
    # price = forms.IntegerField(label="Enter The Price", widget=forms.TextInput)
    # category=forms.CharField(label="Enter The Category", widget=forms.TextInput)
    # date=forms.DateTimeField(label="Enter The Date and Time",widget=forms.DateTimeInput)



    class Meta:
        model = Transport
        fields = ["transport_name",
            "number_plate",
            "seats_available",
            "price_per_person",
            "bus_category",
            "date_time_dpt"]
        labels={'transport_name':'Enter the Bus name','number_plate':'Enter the Bus Number','seats_available':'Enter the Seats','price_per_person':'Enter the Price','bus_category':'Enter the Category','date_time_dpt':'Enter the Date and Time'}

    def clean(self) :
        cleaned_data = super(AddbusCreationForm, self).clean()
        # Check that the two password entries match
        busname = cleaned_data.get("transport_name")
        busnumber = cleaned_data.get("number_plate")
        seats = cleaned_data.get("seats_available")
        price = cleaned_data.get("price_per_person")
        category = cleaned_data.get("bus_category")
        date = cleaned_data.get("date_time_dpt")
       
        if busname =='':
            raise forms.ValidationError("Enter The Bus Name")
            

        elif busnumber =='':
            raise forms.ValidationError("Enter The Bus Number")
            
        elif seats == '' :
            raise forms.ValidationError("Enter The Bus Seats")
        elif price == '':
            raise forms.ValidationError("Enter The Bus Price")
        elif category == '':
            raise forms.ValidationError("Enter The Bus Category")
        elif date == '':
            raise forms.ValidationError("Enter The Bus Date")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format+
        cleaned_data = super(AddbusCreationForm, self).clean()
        addbus = super(AddbusCreationForm, self).save(commit=False)
        addbus.transport_name =  cleaned_data["transport_name"]
        addbus.number_plate = cleaned_data["number_plate"]

        
        print("*********************/////////////",addbus.number_plate)
        addbus.seats_available = cleaned_data["seats_available"]

        addbus.price_per_person = cleaned_data["price_per_person"]
        addbus.bus_category = cleaned_data["bus_category"]
        addbus.date_time_dpt = cleaned_data["date_time_dpt"]
      
        if commit:
            addbus.save()
        return addbus


class AddbusUpdateForm(forms.ModelForm):
    class Meta():
        model = Transport

        fields = [
           "transport_name",
            "number_plate",
            "seats_available",
            "price_per_person",
            "bus_category",
            "date_time_dpt",
        ]

    def clean(self):
        # print(type(self.instance))
        cleaned_data = super(AddbusUpdateForm, self).clean()
        busname = cleaned_data.get("transport_name")
        busnumber = cleaned_data.get("number_plate")
        seats = cleaned_data.get("seats_available")
        price = cleaned_data.get("price_per_person")
        category = cleaned_data.get("bus_category")
        date = cleaned_data.get("date_time_dpt")
        
        if busname =='':
            raise forms.ValidationError("Enter The Bus Name")
      

        elif busnumber =='':
            raise forms.ValidationError("Enter The Bus Number")
            
        elif seats == '' :
            raise forms.ValidationError("Enter The Bus Seats")
        elif price == '':
            raise forms.ValidationError("Enter The Bus Price")
        elif category == '':
            raise forms.ValidationError("Enter The Bus Category")
        elif date == '':
            raise forms.ValidationError("Enter The Bus Date")
        

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            
        
            instance.save()
       

        return instance