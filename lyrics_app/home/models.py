import os
from django.conf import settings
from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

# Create your models here.
class Album(models.Model):
    class Meta:
        db_table = 'albums'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    directorName = models.CharField(max_length=250, db_column='director_name')
    imgLocation = models.FilePathField(path=images_path, db_column="img_location")

class UserRole(models.Model):
    class Meta:
        db_table = 'user_roles'
    id = models.AutoField(primary_key=True)
    LABEL_TYPE_CHOICES = [
        ('admin', 'Administrator'),
        ('moderator', 'Moderator'),
        ('collaborator', 'Collaborator'),
    ]
    lableType = models.CharField(
        max_length=50,
        choices=LABEL_TYPE_CHOICES,
        default='collaborator',
        db_column='lable_type'
    )

class Artist(models.Model):
    class Meta:
        db_table = 'artists'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    imgLocation = models.FilePathField(path=images_path, db_column="img_location")
    ARTIST_TYPE_CHOICES = [
        ('singer', 'Singer'),
        ('writer', 'Writer'),
        ('composer', 'Conposer'),
    ]
    artistType = models.CharField(
        max_length=50,
        choices=ARTIST_TYPE_CHOICES,
        db_column='artist_type'
    )
    description = models.TextField

class User(models.Model):
    class Meta:
        db_table = 'users'
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    passwd = models.CharField(max_length=20)
    fullName = models.CharField(max_length=250, db_column='full_name')
    roleId = models.ForeignKey(UserRole, blank=True, null=True, on_delete=models.SET_NULL, db_column='role_id')

class Lyric(models.Model):
    class Meta:
        db_table = 'lyrics'
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE, db_column='album_id')
    musicCompany = models.CharField(max_length=250, db_column='music_company')
    STATUS_CHOICES = [
        ('draft', 'draft'),
        ('under_review', 'under_review'),
        ('published', 'published'),
        ('change_request', 'change_request'),
        ('declined', 'declined'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='draft'
    )
    genere = models.CharField(max_length=250)
    tags = models.CharField(max_length=11)
    content = models.TextField

class ArtistSong(models.Model):
    class Meta:
        db_table = 'artist_songs'
    lyricId = models.ForeignKey(Lyric, on_delete=models.CASCADE, db_column='lyric_id')
    artistId = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, db_column='artist_id')

class LyricEvent(models.Model):
    class Meta:
        db_table = 'lyrics_events'
    id = models.AutoField(primary_key=True)
    lyricId = models.ForeignKey(Lyric, on_delete=models.CASCADE, db_column='lyric_id')
    type
    TYPE_CHOICES = [
        ('created', 'created'),
        ('approved', 'approved'),
        ('declined', 'declined'),
        ('published', 'published'),
    ]
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='created'
    )
    ocurredAt = models.DateTimeField(db_column='ocurred_at')
    userEmail =  models.CharField(max_length=100, db_column='user_email')
    content = models.TextField
