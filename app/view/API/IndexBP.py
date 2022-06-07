import datetime
from flask import (
    Blueprint, render_template, jsonify, request
)
from flask_jwt_extended import *
from datetime import *

class IndexBp:
    bp = Blueprint('index_bp', __name__)
    
    # 로그인 페이지
    @bp.route('/')
    def index():
        return render_template('login_index.html')
    
    # 로그인 API
    @bp.route("/signin", methods=["POST"])
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
                "description":"토큰 발급 완료"
            })

            # set_access_cookies를 통해 access_token을 저장
            set_access_cookies(response, access_token)

            # set_refresh_cookies를 통해 refresh_token을 저장
            set_refresh_cookies(response, refresh_token)
            return response
        else:
            return jsonify({
                "msg":"fail",
                "description":"로그인 실패"
            })

    # 로그아웃 API
    @bp.route("/logout_with_cookies", methods=["POST"])
    def logout_with_cookies():
        response = jsonify({"msg": "logout successful"})
        # unset_jwt_cookies를 통해 쿠키를 삭제할 수 있다.
        unset_jwt_cookies(response)
        return response
    
    # 보호된 페이지 API
    @bp.route("/protected", methods=["GET"])
    @jwt_required() # 엑세스 토큰이 필요하다.
    def protected():
        identity = get_jwt_identity()
        print("curent_user =", identity)
        return render_template('login_complete.html')

    # 토큰 확인 API
    @bp.route("/check_token", methods=["POST"])
    @jwt_required()
    def test():
        identity = get_jwt_identity()
        return jsonify({
            "msg":"success",
            "identity":identity
            })
    
    # 자동 리프레시 API
    @bp.route("/silent-refresh", methods=["POST"])
    @jwt_required(refresh=True) # refresh token을 받음을 명시
    def refresh():
        user_id = get_jwt_identity()
        print('identity = ', user_id)
        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)

        response = jsonify({
            "msg": "success",
            "user_id": user_id
            })

        # set_access_cookies를 통해 access_token을 저장할 수 있다.
        set_access_cookies(response, access_token)

        # set_refresh_cookies를 통해 refresh_token을 저장할 수 있다.
        set_refresh_cookies(response, refresh_token)        
        return response
