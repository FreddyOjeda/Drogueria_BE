from rest_framework import viewsets
from django.http import HttpResponse
from .serializer import UserSerializer,CategorySerializer,ProductSerializer,RegisterSerializer
from .models import User,Category,Product,Regiter
from django.views.decorators.csrf import csrf_protect

def index(request):
    return HttpResponse("Hello world")


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RegiterViewSet(viewsets.ModelViewSet):
    queryset = Regiter.objects.all()
    serializer_class = RegisterSerializer
