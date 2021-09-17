from django.contrib import admin
from .models import(
		User,
		Categories,
		Artist,
		CountryType,
		Music
	)

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Artist)
admin.site.register(CountryType)
admin.site.register(Music)
