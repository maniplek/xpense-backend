from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.decorators import api_view,permission_classes
from .serializers import CategorySerializer
from .models import Category

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_category(request):
    user = request.user
    name = request.data['name']
    type = request.data.get('type')

    if name and type and user:
        categ = Category(
            name=name,
            type=type,
            created_by=user
        )
        categ.save()

        response = {
            "user":CategorySerializer(categ).data,
            "message":"Category created successful. "
        }

        return Response(response, status=200)

    return Response({"detail": "Bad request."}, status=400)

class CategoryList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        print(user.id)
        if user.is_superuser or user.is_staff:
            return Category.objects.all()

        return Category.objects.filter(created_by=user)


    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class CategoryDetail(mixins.
                    RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)
        
    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)