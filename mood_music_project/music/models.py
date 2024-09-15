from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mood(models.Model):
    MOOD_CHOICES = [
        ('Happy','Happy'),
        ('Sad','Sad'),
        ('Relaxed','Relaxed'),
        ('Energetic','Energetic'),
        ('Focused','Focused'),
    ]

    name = models.CharField(max_length=100, choices=MOOD_CHOICES)
    
    def __str__(self):
        return self.name
    

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    playlist_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.mood.name} Playlist"
    