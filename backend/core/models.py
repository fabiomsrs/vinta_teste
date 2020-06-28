from django.db import models

# Create your models here.

class Repo(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    owner = models.CharField(max_length=150, verbose_name="Proprietário")
    date = models.DateTimeField(verbose_name="Data")
    user = models.CharField(max_length=150, verbose_name="Usuário")

    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)        

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Repo'
        verbose_name_plural = 'Repos'


class Commit(models.Model):
    author = models.CharField(max_length=150, verbose_name="Autor")
    url = models.URLField(max_length=200, verbose_name="url")
    date = models.DateTimeField(verbose_name="Data")
    repo = models.ForeignKey('Repo', related_name='commits', on_delete=models.CASCADE, verbose_name='Repositório')

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Commit'
        verbose_name_plural = 'Commits'