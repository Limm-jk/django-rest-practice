from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser

from .models import Article
from .serializers import ArticleSerializer

def article_list(request):
    if request.method == 'GET':
        # DB의 모든 Article들을 불러오겠다
        articles = Article.objects.all()
        # 그 다음에 직렬화 시켜버리겠다
        # 쿼리셋(다수)일 경우는 many를 True로 줘야한다
        serializer = ArticleSerializer(articles, many=True)
        # dict형태가 아니라면 safe에 False를 준다
        return JsonResponse(serializer.data, safe = False)
    
    # 새로운 기사 추가
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # invalid한 경우
        return JsonResponse(serializer.errors, status=400)