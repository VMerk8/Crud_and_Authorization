from pytz import unicode
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PortfolioSerializer
from .models import Portfolio
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import SessionAuthentication


class Portfolioiew(ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PortfolioSerializer
        if self.action == 'retrieve':
            return PortfolioSerializer
        return self.serializer_class


class ExampleAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return user, None


class MyView(APIView):
    authentication_classes = (SessionAuthentication, ExampleAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)
