from personalBlog.models import Article
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer




@api_view(["GET"])
def data_get(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)