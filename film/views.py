from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Actor, Movie, Comment
from .serializers import ActorSerializer, MovieSerializer, CommentSerializer


class Home(APIView):
    def get(self, request):
        xabar = {"message": "Hello World"}
        return JsonResponse(xabar)
    def post(self, request):
        data = request.POST.data
        xabar = {"messege":"Jo'natkan xabaringiz qabul  qilindi"}
        return JsonResponse(xabar)
class ActorAPIViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    def movie(self ,  request, *args, **kwargs):
        actor = self.get_object()
        act = Movie.objects.filter(actor=actor)
        ser = MovieSerializer(act, many=True)
        return Response(ser.data)

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    @action(detail=True, methods=['GET'])
    def comment(self, request, *args, **kwargs):
        movie = self.get_object()
        com = Comment.objects.filter(movie=movie)
        ser = CommentSerializer(com,many=True)
        return Response(ser.data)



class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


