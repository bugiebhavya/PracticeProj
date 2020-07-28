from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from . import models
from .forms import EventForm, EventDetailForm, EventDetailFormSet
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePage(View):
    login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    model = models.Event
    template_name = "home/index.html"
    def get(self, request):
        context = {}
        if self.request.POST:
            context["event_form"] = EventForm(self.request.POST, instance=self.object)
            # context["sponsor_form"] = SponsorForm(self.request.POST, instance=self.object)
            context["detail_form"] = EventDetailForm(self.request.POST, instance=self.object)
            # context["detail_formset"] = EventDetailFormSet(self.request.POST, instance=self.object)
        else:
            context["event_form"] = EventForm()
            # context["sponsor_form"] = SponsorForm()
            context["detail_form"] = EventDetailForm()
            # context["detail_formset"] = EventDetailFormSet()
        return render(request,self.template_name,context)
        
    def post(self, request):
        context = {}
        context['user'] = request.user
        form = EventForm(self.request.POST)
        detailForm = EventDetailForm(self.request.POST)
        if form.is_valid() and detailForm.is_valid():
            self.object = form.save()
            detailForm.save()
            return render(request,"home/thanks.html",context)
        else:
            context["event_form"] = EventForm()
            context["detail_form"] = EventDetailForm()
            context["form_errors"] = form.errors
            return render(request,self.template_name,context)

    # def form_valid(self, form):      
    #     self.object = form.save(commit=False)
    #     self.object.created_by = self.request.user

    #     context = self.get_context_data()
    #     EventForm = context['event_form']
    #     SponsorForm = context['sponsor_form']
    #     EventDetailForm = context['detail_form']
    #     import pdb
    #     pdb.set_trace()
    #     if form.is_valid():
    #         self.object = form.save()

    
