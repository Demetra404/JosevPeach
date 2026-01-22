from django.db import models

# Create your models here.
class Blog(models.Model):
    title_blog = models.CharField(max_length=150, verbose_name='Заголовок')
    content_blog = models.TextField()
    image_blog = models.ImageField(upload_to='images/', verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True)
    is_publication = models.BooleanField(default=True)
    views_blog = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return self.title_blog

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'страницы блога'
        ordering =['is_publication']