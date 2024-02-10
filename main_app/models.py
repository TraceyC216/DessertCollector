from django.db import models
from django.urls import reverse

STEPS = (
    ('R', 'Check Recipe'),
    ('I', 'Buy Ingredients'),
    ('B', 'Baking Day!')
)

# Create your models here.
class Dessert(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    allergens = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dessert_id': self.id})

class Process(models.Model):
    date = models.DateField()
    step = models.CharField(
        max_length=1,
        choices=STEPS,
        default=STEPS[0][0]
        )
    
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_step_display()} on {self.date}"
    
    class Meta:
        ordering = ['date']
