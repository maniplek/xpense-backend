from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.decorators import api_view,permission_classes
from .serializers import TransactionSerializer
from .models import Transaction
from accounts.models import Account

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_transactions_by_account(request):
    user = request.user

    account = Account.objects.filter(id=request.data['account']).first()
    trans = []

    if user and account:
        transactions = Transaction.objects.filter(account=account)
        if transactions and len(transactions) > 0:
            for trans_i in transactions:
                trans.append(TransactionSerializer(trans_i).data)

            response = {
                "transactions":trans,
                "message":"data fetched successful. "
            }

            return Response(response, status=200)

        return Response({"detail": "No data."}, status=404)

    return Response({"detail": "Bad request."}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_transactions_range(request):
    user = request.user
    start_date = request.data.get('start_date')
    end_date = request.data.get('end_date')

    if user and start_date and end_date:
        transactions = Transaction.objects.filter(created_at__range=[start_date, end_date], created_by=user)
        if transactions and len(transactions) > 0:
            response = []
            for trans_i in transactions:
                response.append(TransactionSerializer(trans_i).data)
            return Response(response,status=200)

        return Response({"detail":"Transaction Not found"},status=404)

    return Response({"detail":"bad request"},status=400)


class TransactionList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Transaction.objects.all()

        return Transaction.objects.filter(created_by=user)

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

