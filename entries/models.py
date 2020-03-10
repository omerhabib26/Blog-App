from django.db import models

from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f'{self.entry_title}'


class Comment(models.Model):
    text = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='comment')

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.comment_text}'

