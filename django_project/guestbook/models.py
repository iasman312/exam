from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Feedback(models.Model):
    author = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    text = models.TextField(max_length=2000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=status_choices,
                              default="active",
                              null=False, blank=False)

    class Meta:
        db_table = 'feedback'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.id}. {self.author}: {self.email}'
