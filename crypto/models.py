from django.db import models

# Create your models here.
class CryptoCurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.symbol}) - ${self.price}"

class CryptoPrice(models.Model):
    crypto = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cryptocurrency.symbol} - ${self.price} at {self.timestamp}"