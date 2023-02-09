from models.db.database import session
from models.Entity.Albums import Albums
from models.Entity.Artists import Artists
from models.Entity.Genres import Genres
from models.Entity.MediaTypes import MediaTypes
from models.Entity.Playlists import Playlists
from models.Entity.PlaylistTracks import PlaylistTracks
from models.Entity.Tracks import Tracks


def insert():
    # Artists

    artist1 = Artists(Name="Miyagi")
    artist2 = Artists(Name="Max Korzh")
    artist3 = Artists(Name="Zemfira")
    artist4 = Artists(Name="Imagine Dragons")
    artist5 = Artists(Name="Avicii")
    artist6 = Artists(Name="One Republic")
    artist7 = Artists(Name="Pain")
    artist8 = Artists(Name="Metallica")
    artist9 = Artists(Name="Anacondaz")
    artist10 = Artists(Name="Lube")

    session.add_all([artist1, artist2, artist3, artist4, artist5,
                    artist6, artist7, artist8, artist9, artist10])

    # Albums

    album1 = Albums(Title="Hattori", ArtistId=1)
    album2 = Albums(Title="Domashniy", ArtistId=2)
    album3 = Albums(Title="Borderline", ArtistId=3)
    album4 = Albums(Title="Origins", ArtistId=4)
    album5 = Albums(Title="True", ArtistId=5)
    album6 = Albums(Title="Human", ArtistId=6)
    album7 = Albums(Title="Coming Home", ArtistId=7)
    album8 = Albums(Title="Master Of Puppets", ArtistId=8)
    album9 = Albums(Title="Ya tebya nikogda", ArtistId=9)
    album10 = Albums(Title="Atas", ArtistId=10)

    session.add_all([album1, album2, album3, album4, album5,
                    album6, album7, album8, album9, album10])

    # Genres

    genre1 = Genres(Name="Folk-Rock")
    genre2 = Genres(Name="Kantri")
    genre3 = Genres(Name="Latinoomerican music")
    genre4 = Genres(Name="Blues")
    genre5 = Genres(Name="Ritm-n-blues")
    genre6 = Genres(Name="Jazz")
    genre7 = Genres(Name="Shanson")
    genre8 = Genres(Name="Romans")
    genre9 = Genres(Name="Electronic music")
    genre10 = Genres(Name="Author")

    session.add_all([genre1, genre2, genre3, genre4, genre5,
                    genre6, genre7, genre8, genre9, genre10])

    # MediaTypes

    mediaType1 = MediaTypes(Name="mass-media")
    mediaType2 = MediaTypes(Name="direct-media")
    mediaType3 = MediaTypes(Name="media-native")
    mediaType4 = MediaTypes(Name="social-media")
    mediaType5 = MediaTypes(Name="retro wave")
    mediaType6 = MediaTypes(Name="old school")
    mediaType7 = MediaTypes(Name="multi-media")
    mediaType8 = MediaTypes(Name="multi-media art")
    mediaType9 = MediaTypes(Name="art")
    mediaType10 = MediaTypes(Name="tra")

    session.add_all([mediaType1, mediaType2, mediaType3, mediaType4, mediaType5,
                    mediaType6, mediaType7, mediaType8, mediaType9, mediaType10])

    # PlayLists

    playlist1 = Playlists(Name="New Hits")
    playlist2 = Playlists(Name="Winter News")
    playlist3 = Playlists(Name="Noisy")
    playlist4 = Playlists(Name="Training")
    playlist5 = Playlists(Name="100 superhits")
    playlist6 = Playlists(Name="Fonk")
    playlist7 = Playlists(Name="Russian electronic")
    playlist8 = Playlists(Name="News FM")
    playlist9 = Playlists(Name="Tik-Tok music")
    playlist10 = Playlists(Name="Bass")

    session.add_all([playlist1, playlist2, playlist3, playlist4, playlist5,
                    playlist6, playlist7, playlist8, playlist9, playlist10])

    # PlaylistTracks

    playlistTrack1 = PlaylistTracks(PlaylistId=1, TrackId=10)
    playlistTrack2 = PlaylistTracks(PlaylistId=2, TrackId=9)
    playlistTrack3 = PlaylistTracks(PlaylistId=3, TrackId=8)
    playlistTrack4 = PlaylistTracks(PlaylistId=4, TrackId=7)
    playlistTrack5 = PlaylistTracks(PlaylistId=5, TrackId=6)
    playlistTrack6 = PlaylistTracks(PlaylistId=6, TrackId=5)
    playlistTrack7 = PlaylistTracks(PlaylistId=7, TrackId=4)
    playlistTrack8 = PlaylistTracks(PlaylistId=8, TrackId=3)
    playlistTrack9 = PlaylistTracks(PlaylistId=9, TrackId=2)
    playlistTrack10 = PlaylistTracks(PlaylistId=10, TrackId=1)

    session.add_all([playlistTrack1, playlistTrack2, playlistTrack3, playlistTrack4, playlistTrack5,
                    playlistTrack6, playlistTrack7, playlistTrack8, playlistTrack9, playlistTrack10])

    # Tracks

    track1 = Tracks(
        Name="Angel",
        AlbumId=1,
        MediaTypeId=1,
        GenreId=1,
        Composer="Miyagi & Andy Panda",
        Milliseconds=234000,
        Bytes=3.45,
        UnitPrice=56.9,
    )
    track2 = Tracks(
        Name="Attestat",
        AlbumId=2,
        MediaTypeId=2,
        GenreId=2,
        Composer="Korzh",
        Milliseconds=190000,
        Bytes=7.3,
        UnitPrice=39,
    )
    track3 = Tracks(
        Name="Hochesh",
        AlbumId=3,
        MediaTypeId=3,
        GenreId=3,
        Composer="Zemfira",
        Milliseconds=300000,
        Bytes=3.5,
        UnitPrice=10,
    )
    track4 = Tracks(
        Name="Monster",
        AlbumId=4,
        MediaTypeId=4,
        GenreId=4,
        Composer="Endru Garfield",
        Milliseconds=270000,
        Bytes=1.9,
        UnitPrice=12.4,
    )
    track5 = Tracks(
        Name="Brothers",
        AlbumId=5,
        MediaTypeId=5,
        GenreId=5,
        Composer="Duffers",
        Milliseconds=236000,
        Bytes=12.9,
        UnitPrice=40,
    )
    track6 = Tracks(
        Name="Secrets",
        AlbumId=6,
        MediaTypeId=6,
        GenreId=6,
        Composer="Grinch Gaya",
        Milliseconds=198000,
        Bytes=6.8,
        UnitPrice=54,
    )
    track7 = Tracks(
        Name="Pain",
        AlbumId=7,
        MediaTypeId=7,
        GenreId=7,
        Composer="Charli Shok",
        Milliseconds=189000,
        Bytes=4.8,
        UnitPrice=10,
    )
    track8 = Tracks(
        Name="Metallica",
        AlbumId=8,
        MediaTypeId=8,
        GenreId=8,
        Composer="Composer of Metallica",
        Milliseconds=120000,
        Bytes=3.4,
        UnitPrice=90,
    )
    track9 = Tracks(
        Name="Mama, Ya lublu",
        AlbumId=9,
        MediaTypeId=9,
        GenreId=9,
        Composer="Piter Choril",
        Milliseconds=320000,
        Bytes=12,
        UnitPrice=49,
    )
    track10 = Tracks(
        Name="Kon`",
        AlbumId=10,
        MediaTypeId=10,
        GenreId=10,
        Composer="Kube composer",
        Milliseconds=134000,
        Bytes=7.3,
        UnitPrice=90,
    )

    session.add_all([track1, track2, track3, track4, track5,
                    track6, track7, track8, track9, track10])

    session.commit()
