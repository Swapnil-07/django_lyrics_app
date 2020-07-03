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
    img_location = models.FilePathField(path=images_path)

class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    LABEL_TYPE_CHOICES = [
        ('admin', 'Administrator'),
        ('moderator', 'Moderator'),
        ('collaborator', 'Collaborator'),
    ]
    label_type = models.CharField(
        max_length=2,
        choices=LABEL_TYPE_CHOICES,
        default='collaborator',
    )

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    img_location = models.FilePathField(path=images_path)
    ARTIST_TYPE_CHOICES = [
        ('singer', 'Singer'),
        ('writer', 'Writer'),
        ('composer', 'Conposer'),
    ]
    artist_type = models.CharField(
        max_length=2,
        choices=ARTIST_TYPE_CHOICES
    )
    description = models.TextField

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    passwd = models.CharField(max_length=20)
    full_name = models.CharField(max_length=250)
    role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE)

class LyricContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField

class Lyric(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lyric_content_id = models.ForeignKey(LyricContent, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    music_company = models.CharField(max_length=250)
    STATUS_CHOICES = [
        ('draft', 'draft'),
        ('under_review', 'under_review'),
        ('published', 'published'),
        ('change_request', 'change_request'),
        ('declined', 'declined'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='draft'
    )
    genere = models.CharField(max_length=250)
    tags = models.CharField(max_length=11)

class artist_songs(models.Model):
    lyric_id = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

class lyrics_events(models.Model):
    id = models.AutoField(primary_key=True)
    lyric_id = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    type
    TYPE_CHOICES = [
        ('created', 'created'),
        ('approved', 'approved'),
        ('declined', 'declined'),
        ('published', 'published'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='created'
    )
    ocurred_at = models.DateTimeField
    user_email =  models.CharField(max_length=100)
    content = models.TextField
