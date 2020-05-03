from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.album_title + ' - ' + self.artist

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'album_id': self.pk})

@property
def num_likes(self):
    return self.liked.all().count()

LIKE_CHOICE = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Album, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICE, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'user_id': self.pk})

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

