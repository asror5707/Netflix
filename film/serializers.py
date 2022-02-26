from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Actor, Movie, Comment


class ActorSerializer(ModelSerializer):

    class Meta:
        model = Actor
        fields = ["id", 'name', 'gander','birth_date']


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id","title","janr","data","actor"]
    def validate_title(self, q):
        if len(q) <= 3:
            raise ValidationError(detail="Bunaqa movie yoq")
        return q

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
