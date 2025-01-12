# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# additional imports below
from rest_framework import generics
from .models import Cat, Feeding
from .serializers import CatSerializer, FeedingSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the cat-collector api home route!'}
    return Response(content)

class CatList(generics.ListCreateAPIView):
  queryset = Cat.objects.all()
  serializer_class = CatSerializer

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cat.objects.all()
  serializer_class = CatSerializer
  lookup_field = 'id'

class FeedingListCreate(generics.ListCreateAPIView):
  serializer_class = FeedingSerializer

  def get_queryset(self):
    cat_id = self.kwargs['cat_id']
    return Feeding.objects.filter(cat_id=cat_id)

  def perform_create(self, serializer):
    cat_id = self.kwargs['cat_id']
    cat = Cat.objects.get(id=cat_id)
    serializer.save(cat=cat)
    
class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeedingSerializer
  lookup_field = 'id'

  def get_queryset(self):
    cat_id = self.kwargs['cat_id']
    return Feeding.objects.filter(cat_id=cat_id)