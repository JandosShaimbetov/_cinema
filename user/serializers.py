from rest_framework import serializers

from user.models import CustomUser, Feedback


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "role"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("invalid email")})
        return super().validate(attrs)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "username"]


class FeedbackSerializer(serializers.ModelSerializer):
    client = UserSerializer()

    class Meta:
        model = Feedback
        fields = ["id", "client", "feedback"]
