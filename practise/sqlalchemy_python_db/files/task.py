from models.db.database import session

from models.Entity.Albums import Albums
from models.Entity.Artists import Artists
from models.Entity.Genres import Genres
from models.Entity.Playlists import Playlists
from models.Entity.PlaylistTracks import PlaylistTracks
from models.Entity.Tracks import Tracks

from sqlalchemy.sql import func


def tasks(number: int):
    if number == 1:
        task = session.query(Tracks.Name, Tracks.Composer, Tracks.Milliseconds) \
            .order_by(Tracks.Name).all()

        print("Task 1\n")

        for t in task:
            print(f"Name: {t.Name}; ",
                  f"Composer: {t.Composer}; ",
                  f"Time(sec): {t.Milliseconds / 1000};")

        print("\n")

    if number == 2:
        print("Task 2\n")
        print(session.query(Tracks).count())
        print("\n")

    if number == 3:
        task = session.query(Albums).limit(10).all()
        print("Task 3\n")
        for t in task:
            print(f'Title: {t.Title}; ', f'ArtistId: {t.ArtistId}; ')
        print("\n")

    if number == 4:
        task = session.query(Genres).filter(Genres.Name.ilike("%ic"))
        print("Task 4\n")
        for t in task:
            print(f'Name: {t.Name}')
        print("\n")

    if number == 5:
        print("Task 5\n")
        task = session.query(
            Albums.AlbumId,
            Albums.Title,
            Tracks.Composer,
            func.sum(Tracks.Bytes),
            func.sum(Tracks.UnitPrice)
        ).join(Tracks) \
            .group_by(Tracks.Composer) \
            .filter(Tracks.AlbumId == Albums.AlbumId).all() \

        for t in task:
            print(t)
        print("\n")

    if number == 6:
        print("Task 6\n")
        print(session.query(Artists) \
              .join(Tracks, Albums.AlbumId == Tracks.AlbumId)
              .join(Albums, Artists.ArtistId == Albums.ArtistId) \
              .distinct(Artists.Name).count())
        print("\n")

    if number == 7:
        print("Task 7\n")
        print(session.query(Artists).select_from(Tracks, Albums, Playlists, PlaylistTracks) \
              .filter(Artists.ArtistId == Albums.ArtistId,
                      Albums.AlbumId == Tracks.AlbumId,
                      Tracks.TrackId == PlaylistTracks.TrackId,
                      Playlists.PlaylistId == PlaylistTracks.PlaylistId,
                      Playlists.PlaylistId == 2) \
              .count())
