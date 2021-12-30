from rest_framework.generics import GenericAPIView 
from rest_framework.permissions import IsAuthenticated


class AuthenticatedAPIView(GenericAPIView):
    permission_classes  = [IsAuthenticated]