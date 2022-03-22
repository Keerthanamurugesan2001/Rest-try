from rest_framework import serializers
from . models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author']
        fields = '__all__'

    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)
    # date = serializers.DateTimeField()
    #
    # def create(self, validated_data):
    #     return Article.objects.all(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('title', instance.author)
    #     instance.email = validated_data.get('title', instance.email)
    #     instance.date = validated_data.get('title', instance.date)
    #
    #     instance.save()
    #
    #     return instance