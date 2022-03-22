from django.urls import path, include
from .views import art_list, art_detail, ArticleApiview, \
    ArticleDetail, GenericApiview, \
    ArticleViewSets, Genericviewset, Ariticlemodelview
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('article', ArticleViewSets, basename='article')
rout = DefaultRouter()
rout.register('art', Genericviewset, basename='art')
r= DefaultRouter()
r.register('article', Ariticlemodelview, basename='article')

urlpatterns = [
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls)),
    path('genericviewset/', include(rout.urls)),
    path('genericviewset/<int:pk>/', include(rout.urls)),
    path('modelviewset/', include(r.urls)),
    path('modelviewset/<int:pk>/', include(r.urls)),
    # path('article/<int:id>/', GenericApiview.as_view()),
    # path('article/', GenericApiview.as_view()),
    # path('article/', ArticleApiview.as_view()),
    # path('article/<int:id>', ArticleDetail.as_view()),
    # path('article/', art_list),
    # path('article/<int:pk>', art_detail),
]