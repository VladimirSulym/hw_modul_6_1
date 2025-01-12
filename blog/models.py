from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to='blogs/images/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    active = models.BooleanField(default=True, verbose_name="Признак публикации")
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    class Meta:
        verbose_name_plural = 'Блоги'
        verbose_name = 'Блог'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
