from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # parece ser que al inicializar los atributos del modelo Post (y 
    # cualquiera en general), es necesario indicar el tipo de dato con 
    # las fuciones, como, .CharField, TextFiel, etc.
    # Dentro de los métodos (como en este caso publish), ya no es necesario
    # indicar el tipo de dato.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')