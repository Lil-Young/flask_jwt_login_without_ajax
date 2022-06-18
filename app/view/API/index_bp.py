import datetime
from flask import (
    Blueprint, render_template, jsonify, request
)
from flask_jwt_extended import *
from datetime import *

class index_bp:
    bp = Blueprint('index_bp', __name__)
    
    # 로그인 페이지
    @bp.route('/')
    def index():
        return render_template('login_index.html')
    
    # 로그인 API
    @bp.post("/signin")
    def login_with_cookies():
        form_data = request.form
        user_id = form_data['id']
        user_pw = form_data['pw']

        """
        DB에서 회원정보 확인, 입력값, 유효성 인증 등 작업 생략했습니다.
        """
        # 간단한 인증
        if user_id==user_pw=='test':
            print('인증 완료(test)')
            access_token = create_access_token(identity=user_id)
            refresh_token = create_refresh_token(identity=user_id)
            
            response = jsonify({
                "msg": "success",
                "user_id": user_id,
                "description":"토큰 발급 완료",
                "access_token": access_token,
                "refresh_token": refresh_token
            })
            return response
        else:
            return jsonify({
                "msg":"fail",
                "description":"로그인 실패"
            })

    # # 로그아웃 API
    # @bp.post("/logout_with_cookies")
    # def logout_with_cookies():
    #     response = jsonify({"msg": "logout successful"})
    #     # unset_jwt_cookies를 통해 쿠키를 삭제할 수 있다.
    #     unset_jwt_cookies(response)
    #     return response
    
    # 엑세스 토큰 확인 API
    @bp.post("/check_access_token")
    @jwt_required()
    def check_access_token():
        identity = get_jwt_identity()
        return jsonify({
            "msg":"success",
            "identity":identity
            })
    
    # 리프레시 토큰 확인 API
    '''
    리프레시 토큰 확인 및 엑세스 토큰 재발행
    '''
    @bp.post("/check_refresh_token")
    @jwt_required(refresh=True)
    def check_refresh_token():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        refresh_token = create_refresh_token(identity=identity)
        response = jsonify({
            "msg":"success",
            "access_token": access_token,
            "refresh_token": refresh_token
        })
        return response
