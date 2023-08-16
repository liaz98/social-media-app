from core.abstract.serializers import AbstractSerializer
from rest_framework import serializers
from core.post.models import Post

from core.user.models import User
from core.user.serializers import UserSerializer

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset = User.objects.all(), slug_field='public_id')
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep["author"] = UserSerializer(author).data
        return rep
    
    def validate_author(self, value):
        if value != self.context['request'].user:
            raise serializers.ValidationError('You can not create a post for another user.')
        return value
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated', 'liked', 'likes_count']
        read_only_fields = ['edited']

    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        return super().update(instance, validated_data)
    
    def get_liked(self, instance):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked(instance)
    
    def get_likes_count(self, instance):
        return instance.liked_by_count()
