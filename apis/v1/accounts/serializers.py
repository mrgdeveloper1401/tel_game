from rest_framework import serializers
from django_telegram_login.authentication import verify_telegram_authentication
from django.conf import settings


class LoginByTelegramSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    photo_url = serializers.CharField(required=False)
    auth_date = serializers.IntegerField()
    hash = serializers.CharField()

    def validate(self, data):
        if not verify_telegram_authentication(
            bot_token=settings.TELEGRAM_BOT_TOKEN,
            request_data=data
        ):
            raise serializers.ValidationError(
                {
                    "message": "Invalid login Telegram Token",
                }
            )
        return data
