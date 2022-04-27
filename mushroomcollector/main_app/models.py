from django.db import models
from django.urls import reverse

# Create your models here.


class Mushroom(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)
    edibility = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('detail', kwargs={'mushroom_id': self.id})


RAIN = (
    ('U', 'Unknown'),
    ('C', 'Currently raining'),
    ('H', 'Rained within last 24 hrs'),
    ('W', 'Rained within last week'),
    ('N', 'No recent rain'),
)

class Shroom_Hunt(models.Model):
    date = models.DateField('date of trip')
    location = models.CharField(max_length=100)
    recent_rain = models.CharField(
        max_length=1,
        choices=RAIN,
        default=RAIN[0][0]
    )

    mushroom = models.ForeignKey(Mushroom, on_delete=models.CASCADE)

    def __str__(self):
        # this method will gives us the friendly meal choices value, so like Breakfast instead of B
        return f"{self.location} on {self.date}; recent rain: {self.get_recent_rain_display()}"

    class Meta:
	    ordering = ['-date']