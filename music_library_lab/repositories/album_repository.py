from db.run_sql import run_sql

from models.album import Album
import repositories.album_repository as album_repository


def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album
  

def delete_all():
    sql = "DELETE  FROM artists" 
    run_sql(sql)


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        album = Album(result['name'], result['genre'], result['artist'], result['id'] )
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        album = Album(row['name'], row['genre'], row['artist'], row['id'])
        albums.append(album)
    return albums