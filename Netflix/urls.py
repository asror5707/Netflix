
from django.contrib import admin
from django.urls import path, include

from film.views import Home,  MovieViewSet, ActorAPIViewSet  # MovieAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("movie",MovieViewSet)
rout = DefaultRouter()
router.register('actor',ActorAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home.as_view()),
    # path('actor/', ActorAPIView.as_view()),
    # path('actor/<int:pk>/', ActorAPIView.as_view()),
    path('', include(router.urls)),
    path('', include(rout.urls)),
    # path('movie/', MovieAPIView.as_view()),
    # path('movie/<int:pk>/', MovieAPIView.as_view()),
]
