from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Senha(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarios')
    email = models.EmailField(max_length=320)
    senha = models.CharField(max_length=127)
    categoria = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('painel')
    
        
