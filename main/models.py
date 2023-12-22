from django.db import models

# Create your models here.
class Articles(models.Model):
    name = models.CharField('Название',max_length=100)
    preview = models.CharField('Анонс',max_length=250)
    cover = models.ImageField()
    description = models.TextField('Статья')
    time = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'