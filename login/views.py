from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password
from .serialize import LoginUserSerializer
#비밀번호 암호화,(단방향 암호화..)
# Create your views here.


class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id',"")
        user_pw = request.data.get('user_pw',"")
        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg='해당 사용자 없음'))
        
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg='로그인 성공',
            user_id=user.user_id,
            user_pw=user.user_pw, 
            birth_day=user.birth_day,
            gender=user.gender,
            email=user.email,
            name=user.name,
            age=user.age))
        else:
            return Response(dict(msg='로그인 실패, 비번틀림'))

class RegistUser(APIView):
    def post(self,request):
        serializer = LoginUserSerializer(request.data)
        # 한번에 시리얼라이저로 받을거라 주석함.
        # user_id = request.data.get('user_id','')
        # user_pw = request.data.get('user_pw','')
        # birth_day=request.data.get('birth_day',None)
        # gender=request.data.get('gender','male')
        # email=request.data.get('email','')
        # name=request.data.get('name','')
        # age=request.data.get('age',20)

        # user_pw_encryted = make_password(user_pw) # 암호화
        user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first()
        if user is not None:
            return Response(dict(msg='동일한 아이디가 있습니다.'))
            
        #암호화된 비밀번호로 저장한다.
        # LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encryted, birth_day=birth_day,gender=gender,email=email,name=name,age=age)

        user = serializer.create(request.data)

        return Response(data=LoginUserSerializer(user).data)