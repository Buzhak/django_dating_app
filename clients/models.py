from codecs import getencoder
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def file_size(value): # add this to some file where you can import it from
        limit = 2 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('Файл слишком большой. Размер файла должен быть не более 2 Mb.')

class Client(models.Model):
    GENDER_CHOICES = [
        ('women', 'жен'),
        ('man', 'муж'),
        ('other', 'другое'),
    ]
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        verbose_name="Пол"
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="Email"
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        validators=[file_size],
        verbose_name="Аватарка"
        )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    

    