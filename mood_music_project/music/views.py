from django.shortcuts import render, redirect
from .models import Mood, Playlist
from django.contrib.auth.decorators import login_required
import random

# Mock playlist data (replace with actual API calls in production)
MOOD_PLAYLISTS = {
    'Happy': 'https://open.spotify.com/playlist/0aL9ZENstRnWaAVTAAfz4A',
    'Sad': 'https://open.spotify.com/playlist/2sOMIgioNPngXojcOuR4tn',
    'Relaxed': 'https://open.spotify.com/playlist/37i9dQZF1DWX76Z8XDsZzF',
    'Energetic': 'https://open.spotify.com/playlist/3mSm688yR6UeaAJNf93Ydr',
    'Focused': 'https://open.spotify.com/playlist/1S5FWtaDXYrcpQwz1SVaxR',
}

@login_required
def mood_selection(request):
    if request.method == 'POST':
        selected_mood = request.POST.get('mood')
        mood = Mood.objects.get(name=selected_mood)

        # Get playlist URL based on selected mood (you can fetch this from an API)
        playlist_url = MOOD_PLAYLISTS[selected_mood]

        # Save the playlist URL and related info to the database
        Playlist.objects.create(user=request.user, mood=mood, playlist_url=playlist_url)

        return redirect('view_playlist')

    moods = Mood.objects.all()
    return render(request, 'music/mood_selection.html', {'moods': moods})
