from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
