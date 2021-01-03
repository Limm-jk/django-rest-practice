from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # 어떤 모델로 만드는지, 어떤 필드를 사용하는 지 정보 제공
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author', 'email']
        # 하나하나 할 필요 없이 이걸로 한번에 다 지정이 가능하다
        fields = '__all__'
        


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()
    
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance
        