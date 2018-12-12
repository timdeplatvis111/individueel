from django.db import models

class Serie(models.Model):
    serieid = models.IntegerField(db_column='serieID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=255)
    rating = models.IntegerField()
    studio = models.CharField(max_length=255)
    serienaam = models.CharField(db_column='serieNaam', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie'

class Soundtrack(models.Model):
    soundtrackid = models.IntegerField(db_column='soundtrackID', primary_key=True)  # Field name made lowercase.
    catagory = models.CharField(max_length=11)
    rating = models.IntegerField()
    description = models.CharField(max_length=11)
    seriessoundtrackid = models.ForeignKey(Serie, models.DO_NOTHING, db_column='SeriesSoundtrackID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'soundtrack'

class Componist(models.Model):
    componistid = models.IntegerField(db_column='componistID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'componist'

class Song(models.Model):
    songid = models.IntegerField(db_column='songID', primary_key=True)  # Field name made lowercase.
    singer = models.CharField(max_length=255)
    songsoundtrackid = models.ForeignKey('Soundtrack', models.DO_NOTHING, db_column='SongSoundtrackID')  # Field name made lowercase.
    songcomponistid = models.ForeignKey(Componist, models.DO_NOTHING, db_column='SongComponistID')  # Field name made lowercase.
    songnaam = models.CharField(db_column='songNaam', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'song'

class User(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'

class Usercomponistfavorite(models.Model):
    usercomponistfavoriteid = models.IntegerField(db_column='UserComponistFavoriteID', primary_key=True)  # Field name made lowercase.
    useridcomponistfavorite = models.ForeignKey(User, models.DO_NOTHING, db_column='UserIDComponistFavorite')  # Field name made lowercase.
    componistiduserfavorite = models.ForeignKey(Componist, models.DO_NOTHING, db_column='ComponistIDUserFavorite')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usercomponistfavorite'

class Usersoundtrackrating(models.Model):
    usersoundtrackratingid = models.IntegerField(db_column='UserSoundtrackRatingID', primary_key=True)  # Field name made lowercase.
    useridsoundtrackrating = models.ForeignKey(User, models.DO_NOTHING, db_column='UserIDSoundtrackRating')  # Field name made lowercase.
    soundtrackuseridrating = models.ForeignKey(Soundtrack, models.DO_NOTHING, db_column='SoundtrackUserIDRating')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usersoundtrackrating'
