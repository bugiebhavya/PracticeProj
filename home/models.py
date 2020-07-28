from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(("Title"), max_length=50)
    topic = models.CharField(("Topic"), max_length=50)
    start_date = models.DateField(("Start"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(("End"), auto_now=False, auto_now_add=False)
    Email = models.EmailField(("Email Address"), max_length=254)
    

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("home", kwargs={"pk": self.pk})



class EventDetail(models.Model):
    
    event = models.ForeignKey("Event", verbose_name=("Event"), on_delete=models.CASCADE)
    time = models.TimeField(("Time"), auto_now=False, auto_now_add=False)
    description = models.CharField(("Description"), max_length=50)
    class Meta:
        verbose_name = ("Event Detail")
        verbose_name_plural = ("Event Details")

    def __str__(self):
        return self.event.title