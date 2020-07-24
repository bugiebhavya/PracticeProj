from django.contrib import admin
from .models import Event, Sponsor, EventDetail

# Register your models here.
admin.site.register(Event)
admin.site.register(Sponsor)
admin.site.register(EventDetail)