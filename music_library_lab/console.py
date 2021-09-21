
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist("Chris De Burgh")
artist_repository.save(artist1)

album1 = Album("Spanish Train And Other Stories", "Easy Listening", "Chris De Burgh")
album_repository.save(album1)

# artist_repository.delete_all()
# album_repository.delete_all()

