from rest_framework import serializers
from .models import LoginUser
from django.contrib.auth.hashers import make_password
# 관리, 사용, 생산성이 높아져서 serialize를 사용하지만 꼭 좋은것은 아니다.
# 복잡한 로직은 뷰에서 처리하는게 나을 수 있다..

class LoginUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user_pw'] = make_password(validated_data['user_pw'])
        user = LoginUser.objects.create(**validated_data)
        return user

    def validate(self, attrs):
        return attrs

    class Meta:
        model = LoginUser
        fields = ('user_id', 'user_pw', 'birth_day', 'gender', 'email', 'name', 'age')