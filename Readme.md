# Serializer 실습

```
>>> from api_basic.models import Article
>>> from api_basic.serializers import ArticleSerializer
>>> from rest_framework.renderers import JSONRenderer 
>>> from rest_framework.parsers import JSONParser 
>>> a = Article(title='article title', author='junkyu', email='ad@ad.ad')
>>> a.save()

# 여기서 admin페이지 확인 시 객체 생성
>>> a = Article(title='new title', author='jyu', email='ad@ad.pr')        
>>> a.save()

# 직렬화 시켜보자
>>> serializer = ArticleSerializer(a)
>>> serializer.data
{'title': 'new title', 'author': 'jyu', 'email': 'ad@ad.pr', 'date': '2021-01-03T02:19:02.404491Z'}

# json파일로 render
>>> content = JSONRenderer().render(serializer.data) 
>>> content
b'{"title":"new title","author":"jyu","email":"ad@ad.pr","date":"2021-01-03T02:19:02.404491Z"}

# 많이도 가능
>>> serializer = ArticleSerializer(Article.objects.all(), many=True)  
>>> serializer.data
[OrderedDict([('title', 'article title'), ('author', 'junkyu'), ('email', 'ad@ad.ad'), ('date', '2021-01-03T02:15:36.275589Z')]), OrderedDict([('title', 'new title'), ('author', 'jyu'), ('email', 'ad@ad.pr'), ('date', '2021-01-03T02:19:02.404491Z')])]

# json화 시키면 정상적으로 나뉘어서 나온다.
>>> content = JSONRenderer().render(serializer.data) 
>>> content
b'[{"title":"article title","author":"junkyu","email":"ad@ad.ad","date":"2021-01-03T02:15:36.275589Z"},{"title":"new title","author":"jyu","email":"ad@ad.pr","date":"2021-01-03T02:19:02.404491Z"}]'
```