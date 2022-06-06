import datetime
from flask import (
    Blueprint, render_template, jsonify, request
)
from flask_jwt_extended import *
from datetime import *
def error(msg):
    return msg

class IndexBp:
    bp = Blueprint('index_bp', __name__)
    
    @bp.route('/')
    def index():
        return render_template('login_index.html')
    
    @bp.route("/signin", methods=["POST"])
    def login_with_cookies():
        form_data = request.form
        user_id = form_data['id']
        user_pw = form_data['pw']

        """
        DB에서 회원정보 확인, 입력값, 유효성 인증 등 작업 생략
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

            # set_access_cookies를 통해 access_token을 저장할 수 있다.
            set_access_cookies(response, access_token)

            # set_refresh_cookies를 통해 refresh_token을 저장할 수 있다.
            set_refresh_cookies(response, refresh_token)
            return response
        else:
            return jsonify({
                "msg":"fail",
                "description":"로그인 실패"
            })


    @bp.route("/logout_with_cookies", methods=["POST"])
    def logout_with_cookies():
        response = jsonify({"msg": "logout successful"})
        # unset_jwt_cookies를 통해 쿠키를 삭제할 수 있다.
        unset_jwt_cookies(response)
        return response
    

    @bp.route("/protected", methods=["GET"])
    @jwt_required() # 엑세스 토큰이 필요하다.
    def protected():
        identity = get_jwt_identity()
        print("curent_user =", identity)
        return render_template('login_complete.html')

    @bp.route("/test", methods=["POST"])
    @jwt_required()
    def test():
        identity = get_jwt_identity()
        return jsonify({
            "msg":"success",
            "identity":identity
            })
    

    @bp.route("/refresh", methods=["POST"])
    @jwt_required(refresh=True)
    def refresh():
        print("refresh")
        """
        refresh토큰을 헤더에 포함시켜 서버에 요청하면, 엑세스 토큰을 새로 만들어 전달한다.
        이때, 엑세스 토큰이 fresh하지 않음을 표시하기 위해 fresh=False를 추가한다.
        
        """

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

    

    @bp.route("/only_headers")
    @jwt_required(locations=["headers"])
    def only_headers():
        return jsonify(foo="baz")