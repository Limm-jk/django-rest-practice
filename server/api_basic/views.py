from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer

# 다양한 view에서 정의한 기능들을 담고있는 set
# 뭐야 개사기잖아? 내 100줄 돌려줘
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        # DB의 모든 Article들을 불러오겠다
        articles = Article.objects.all()
        # 그 다음에 직렬화 시켜버리겠다
        # 쿼리셋(다수)일 경우는 many를 True로 줘야한다
        serializer = ArticleSerializer(articles, many=True)
        # # dict형태가 아니라면 safe에 False를 준다
        # return JsonResponse(serializer.data, safe = False)
        # 알아서 response의 형태를 잡아줌
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # invalid한 경우
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # post가 아니기 때문에 status는 필요 없다
            return Response(serializer.data)
        # invalid한 경우
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

# mix in. 상속을 통해서 새로운 내용을 추가하겠어!
class GenericAPIViews(generics.GenericAPIView, 
                      mixins.ListModelMixin, 
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    lookup_field = 'id'
    
    # 세션과 basic 인증을 해야함
    # basic은 usernaem, password, email...
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

class ArticleAPIView(APIView):
    def get(self, request):
        # DB의 모든 Article들을 불러오겠다
        articles = Article.objects.all()
        # 그 다음에 직렬화 시켜버리겠다
        # 쿼리셋(다수)일 경우는 many를 True로 줘야한다
        serializer = ArticleSerializer(articles, many=True)
        # # dict형태가 아니라면 safe에 False를 준다
        # return JsonResponse(serializer.data, safe = False)
        # 알아서 response의 형태를 잡아줌
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # invalid한 경우
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetails(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # post가 아니기 때문에 status는 필요 없다
            return Response(serializer.data)
        # invalid한 경우
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # rest framework는 sensetive해서 이런 걸 달아줘야 한다
# @csrf_exempt
# 어떤 HTTP Method를 허용할 것인지 지정
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        # DB의 모든 Article들을 불러오겠다
        articles = Article.objects.all()
        # 그 다음에 직렬화 시켜버리겠다
        # 쿼리셋(다수)일 경우는 many를 True로 줘야한다
        serializer = ArticleSerializer(articles, many=True)
        # # dict형태가 아니라면 safe에 False를 준다
        # return JsonResponse(serializer.data, safe = False)
        # 알아서 response의 형태를 잡아줌
        return Response(serializer.data)
    
    # 새로운 기사 추가
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # invalid한 경우
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
        
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # article's'가 아니기 때문에, many option을 빼준다.
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 업데이트를 해주는 역할을 함. 이때 pk는 변하지 않음
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # post가 아니기 때문에 status는 필요 없다
            return Response(serializer.data)
        # invalid한 경우
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        