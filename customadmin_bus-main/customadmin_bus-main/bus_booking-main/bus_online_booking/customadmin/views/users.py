from xml.sax.saxutils import prepare_input_source

from requests import request
from bus.models import Transport
from customadmin.forms.addbus_form import AddbusCreationForm
from customadmin.forms.addbus_form import AddbusUpdateForm
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyDetailView,
    MyLoginRequiredView,
    MyUpdateView,
)
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView, DetailView
from django_datatables_too.mixins import DataTableMixin
from django.contrib.auth.models import User
from ..forms import UserChangeForm, UserCreationForm
from django.shortcuts import redirect, reverse, render

from django.contrib.auth.models import User
from datetime import datetime
class IndexView(LoginRequiredMixin,TemplateView):

    template_name = "customadmin/index.html"
    context = {}

    def get(self, request):
        self.context['user_count']=User.objects.all().exclude(is_staff=True).count()
        list1 = []
        self.context['list1']=list1

        
        q=Transport.objects.all()
        for query in q:
            list1.append(query. date_time_dpt)

        return render(request, self.template_name, self.context)
    # def post(self,request):
        # month=request.POST['month']
        # print(month.split('-')[0])
        # # year=request.POST['year']
        # # transport=Transport.objects.all()
        # # for t in transport:
        # #     t1=t.date_time_dpt

        # datetime_object = datetime.strptime(month, "%Y-%m")
        # print(datetime_object.date(),"*******************************************")
        # q=Transport.objects.filter(date_time_dpt__year=month.strip('-')[0])
        # print(q)
        # return redirect(IndexView)


class UserListView(MyListView):
    model = User
    template_name = 'customadmin/adminuser/user_list.html'
    ordering = ["id"]

    def get_queryset(self):
        return self.model.objects.filter(is_staff=False)
    

    # def get_queryset(self):
    #     return render(request,self.template_name)


class UserCreateView(MyCreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'customadmin/adminuser/user_form.html'

    def get_form_kwargs(self) :
        print("**********************")
        print(super().get_form_kwargs)
        return super().get_form_kwargs()
    
    def get_success_url(self):
        return reverse("customadmin:user-list")


class UserDetailView(MyDetailView):
    template_name = "customadmin/adminuser/user_detail.html"
    context = {}

    def get(self, request, pk):
        self.context['user_detail'] = User.objects.filter(pk=pk).first()
        return render(request, self.template_name, self.context)


class UserUpdateView(MyUpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'customadmin/adminuser/user_form_update.html'

    def get_success_url(self):
        return reverse("customadmin:user-list")


class UserDeleteView(MyDeleteView):
    model = User
    template_name = 'customadmin/confirm_delete.html'

    def get_success_url(self):
        return reverse("customadmin:user-list")


class UserAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = User
    queryset = User.objects.all().order_by("last_name")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        # ctx.update({"obj": obj})
        # print(ctx)
        return t.render({"o": obj})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
                # | Q(state__icontains=self.search)
                # | Q(year__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data

    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""


    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        # ctx.update({"obj": obj})
        # print(ctx)
        return t.render({"o": obj})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
                # | Q(state__icontains=self.search)
                # | Q(year__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data