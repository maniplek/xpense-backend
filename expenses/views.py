from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.decorators import api_view,permission_classes
from .serializers import ExpenseSerializer
from .models import Expense
from accounts.models import Account
from transactions.models import Transaction
from categories.models import Category

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_expense(request):
    user = request.user
    amount = request.data['amount']
    description = request.data.get('description')

    account = Account.objects.filter(id=request.data['account']).first()
    category = Category.objects.filter(id=request.data.get('category')).first()

    if amount and description and category and user and account:
        expense = Expense(
            amount=amount,
            description=description,
            category=category,
            created_by=user
        )
        expense.save()


        trans = Transaction(
            expense=expense,
            account=account,
            created_by=user
        )
        trans.save()

        response = {
            "expense":ExpenseSerializer(expense).data,
            "message":"Expense created successful. "
        }

        return Response(response, status=200)

    return Response({"detail": "Bad request."}, status=400)


class ExpenseList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Expense.objects.all()

        return Expense.objects.filter(created_by=user)


    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class ExpenseDetail(mixins.
                    RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)
        
    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)