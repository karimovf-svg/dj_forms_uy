from django.db import models

class Fanlar(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='student')
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_bool = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "NEW"
        verbose_name_plural = "NEWS"
        ordering = ['-created_ed']
