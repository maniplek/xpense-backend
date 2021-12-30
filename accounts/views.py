from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.decorators import api_view,permission_classes
from .serializers import AccountSerializer
from .models import Account

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_account(request):
    user = request.user
    name = request.data['name']
    currency = request.data.get('currency')

    if name and currency and user:
        account = Account(
            name=name,
            currency=currency,
            created_by=user
        )
        account.save()

        response = {
            "account":AccountSerializer(account).data,
            "message":"Account created successful. "
        }

        return Response(response, status=200)

    return Response({"detail": "Bad request."}, status=400)


class AccountList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Account.objects.all()

        return Account.objects.filter(created_by=user)


    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class AccountDetail(mixins.
                    RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)
        
    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)