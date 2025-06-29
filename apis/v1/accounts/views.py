from rest_framework import views, response, status
from rest_framework.authtoken.models import Token

from account_app.models import User
from . import serializers


class LoginView(views.APIView):
    serializer_class = serializers.LoginByTelegramSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get validated data
        data = serializer.validated_data

        # create or update user
        user, created = User.objects.get_or_create(
            telegram_id=data['id'],
            username = data.get('username', f"user_{data['id']}"),
            first_name = data.get('first_name', ''),
            last_name = data.get('last_name', '')
            )

        # create token
        token, _ = Token.objects.get_or_create(user=user)

        # response data
        return response.Response({
            'status': 'success',
            'user_id': user.id,
            'telegram_id': user.telegram_id,
            'token': token.key
        }, status=status.HTTP_200_OK)
