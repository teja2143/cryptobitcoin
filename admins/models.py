from django.db import models

from django.utils import timezone



from datetime import datetime

class CryptoPrice(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.name} - {self.price} (as of {current_time})"
