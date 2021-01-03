from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIViews, ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('article/', article_list),
    
    # as_view() 메소드에서 클래스의 인스턴스를 생성한다.
    # 생성된 인스턴스의 dispatch() 메소드를 호출한다.
    # dispatch() 메소드는 요청을 검사해서 HTTP의 메소드(GET, POST, ...)를 알아낸다.
    # 인스턴스 내에 해당 이름을 갖는 메소드로 요청을 중계한다.
    # 해당 메소드가 정의되어 있지 않으면, HttpResponseNotAllowd 예외를 발생시킨다.
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIViews.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]