from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.decorators import api_view,permission_classes
from .serializers import IncomeSerializer
from .models import Income
from accounts.models import Account
from transactions.models import Transaction
from categories.models import Category

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_income(request):
    user = request.user
    amount = request.data['amount']
    description = request.data.get('description')

    account = Account.objects.filter(id=request.data['account']).first()
    category = Category.objects.filter(id=request.data.get('category')).first()

    if amount and description and category and account and user:
        income = Income(
            amount=amount,
            description=description,
            category=category,
            created_by=user
        )
        income.save()

        trans = Transaction(
            income=income,
            account=account,
            created_by=user
        )
        
        trans.save()

        response = {
            "income":IncomeSerializer(income).data,
            "message":"Income created successful. "
        }

        return Response(response, status=200)

    return Response({"detail": "Bad request."}, status=400)


class IncomeList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    serializer_class = IncomeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Income.objects.all()

        return Income.objects.filter(created_by=user)

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class IncomeDetail(mixins.
                    RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)
        
    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)