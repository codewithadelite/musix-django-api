from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	names = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.names

class Categories(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Artist(models.Model):
	names = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.names

class CountryType(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Music(models.Model):
	name = models.CharField(max_length=255)
	image= models.ImageField(upload_to='static/images/music', default='static/images/music/default.jpg')
	details = models.TextField()
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='musicCategory')
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musicArtist')
	musicType = models.ForeignKey(CountryType, on_delete=models.CASCADE, related_name='musicCountryType')
	musicAuthor = models.CharField(max_length=255)
	youtubeLink = models.URLField(blank=True)
	spotifyLink = models.URLField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='musicUploaded_by')

	def __str__(self):
		return f"{self.name} - {self.artist.names}"

	def get_less_details(self):
		if(len(self.details) > 50):
			brief = self.details[:50]
			return f"{brief}...."
		return self.details





