from django.db import models

# Create your models here.

class Math(models.Model):
    operation = models.CharField(max_length=10)          # null = true ole mozę być puste
    wart1 = models.IntegerField()
    wart2 = models.IntegerField()
#    user = models.ForeignKey(User, on_delete=models.)          # kolejny krok do zabezpieczenia dostepu do pewnej częsci portalu prze logowanie
    def __str__(self):
        return f"Math operatoon: {self.operation} {self.wart1} {self.wart2}"