# Model Serializer 실습

```python
# 어떤 모델로 만드는지, 어떤 필드를 사용하는 지 정보 제공
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
```

```
>>> serializer = ArticleSerializer()
>>> print(repr(serializer)) 
ArticleSerializer():
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    email = EmailField(max_length=100)
    date = DateTimeField()
```