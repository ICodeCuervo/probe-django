from django.db import models

from django.contrib.auth.forms import User

class Category(models.Model):
    name = models.CharField('Nombre', db_column = 'name', max_length = 20, blank = False, null = False)

    class Meta:
        managed = True
        db_table = 'Category'

    def __str__(self):
        return '{}'.format(self.name)

# Create your models here.
class Post(models.Model):
    id_user = models.ForeignKey(User, db_column = 'id_user', blank = False, null = False)
    title = models.CharField('Título del post', db_column = 'title', max_length = 60, blank = False, null = False)
    descr = models.TextField('Descripción', db_column = 'descrip', blank = False, null = False, max_length = 200)
    body = models.TextField('Cuerpo', db_column = 'body', blank = False, null = False, max_length = 500)
    id_category = models.ForeignKey(Category, db_column = 'id_category', blank = False, null = False, default = None)
    created_at = models.DateTimeField('Fecha de publicación', db_column = 'created_at', auto_now_add = True, blank = True, null = False)

    class Meta:
        managed = True
        db_table = 'Post'

    def __str__(self):
        return '{}'.format(self.title)
