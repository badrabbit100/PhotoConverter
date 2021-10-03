from django.db import models


class Photo(models.Model):
    """ This model define income photo and date created + save session key for each Anonymous user """

    photo_input = models.ImageField(upload_to='photo_input', verbose_name='Photo', null=True)
    session = models.CharField(max_length=50, verbose_name='Session Key', null=True)
    action = models.CharField(max_length=50, verbose_name='Action', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')

    def __str__(self):
        return 'DATE: {}'.format(self.date_created)

    class Meta:
        ordering = ['-date_created']
