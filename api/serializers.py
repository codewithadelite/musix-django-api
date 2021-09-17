from rest_framework import serializers
from music.models import Categories,User,Music

class CategoriesSerializer(serializers.ModelSerializer):
	category_total_music = serializers.SerializerMethodField()
	created_at = serializers.DateTimeField(read_only=True)
	updated_at = serializers.DateTimeField(read_only=True)

	class Meta:
		model = Categories
		fields = '__all__'

	def get_category_total_music(self, attr):
		total = Music.objects.filter(category=attr).count()
		return total

class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	password2 = serializers.CharField(write_only=True)
	class Meta:
		model=User
		fields=('names','username','email','password','password2')

	def validate_password2(self, attr):
		data = self.get_initial()
		if attr == data['password']:
			return attr
		raise serializers.ValidationError('Password doesnt match')

	def create(self, data):
		user = User.objects.create_user(data['username'],data['email'],data['password']
			)
		user.names = data['names']
		return user

class LatestMusicSerializer(serializers.ModelSerializer):
	category = serializers.SerializerMethodField()
	artist = serializers.SerializerMethodField()
	musicType = serializers.SerializerMethodField()
	less_details = serializers.CharField(source='get_less_details')
	class Meta:
		model = Music
		fields = '__all__'

	def get_category(self, obj):
		return obj.category.name

	def get_artist(self, obj):
		return obj.artist.names

	def get_musicType(self, obj):
		return obj.musicType.name