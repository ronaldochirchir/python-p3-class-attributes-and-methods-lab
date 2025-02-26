# lib/testing/song_test.py
from song import Song

# Create some songs
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
single_ladies = Song("Single Ladies", "Beyonce", "Pop")
empire_state_of_mind = Song("Empire State of Mind", "Jay-Z", "Rap")

# Test class attributes
def test_song_count():
    assert Song.count == 4

def test_genres():
    assert set(Song.genres) == {"Rap", "Pop"}

def test_artists():
    assert set(Song.artists) == {"Jay-Z", "Beyonce"}

def test_genre_count():
    assert Song.genre_count == {"Rap": 2, "Pop": 2}

def test_artist_count():
    assert Song.artist_count == {"Jay-Z": 2, "Beyonce": 2}