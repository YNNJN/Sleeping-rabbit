from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request, article_pk):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    serializer = CommentSerializer(data=request.data)
    article = get_object_or_404(Article, pk=article_pk)
    if serializer.is_valid(raise_exception=True):
        comment = serializer.save(commit=False)
        comment.user=request.user
        comment.article=article
        comment.save()
        return Response(serializer.data)
