from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password
#비밀번호 암호화,(단방향 암호화..)
# Create your views here.


class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg='해당 사용자 없음'))
        
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg='로그인 성공'))
        else:
            return Response(dict(msg='로그인 실패, 비번틀림'))

class RegistUser(APIView):
    def post(self,request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user_pw_encryted = make_password(user_pw)

        user = LoginUser.objects.filter(user_id=user_id).first()
        if user is not None:
            Response(dict(msg='동일한 아이디가 있습니다.'))
        #암호화된 비밀번호로 저장한다.
        LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encryted)

        data = dict(
            user_id=user_id,
            user_pw=user_pw_encryted
        )

        return Response(data)