'''
app/__init__
Application Factory 역할을 담당하는 부분
'''
from flask import Flask, render_template
# JWT 확장 라이브러리 임포트하기
from flask_jwt_extended import *

""" blueprints """
from app.view.API.IndexBP import IndexBp

def create_app():
    # application factory 생성
    app = Flask(
        import_name=__name__, # 패키지의 이름
        instance_relative_config=True, # 상대경로를 사용함
        static_url_path='/', # 정적 폴더 기본 경로 설정
        static_folder='view/assets/static/', # static 폴더 경로 설정 -> 정적 기본 경로/static 폴더 경로에 위치한다.
        template_folder='view/assets/templates/') # templates 폴더 경로 설정 -> 정적 기본 경로/templates 폴더 경로에 위치한다.

    # app config 설정
    app.config.update(
        DEBUG = True,
        
        JWT_TOKEN_LOCATION = ['headers', 'cookies', 'json', 'query_string'],

        JWT_COOKIE_SECURE = False,

        ### JWT 토큰을 생성하는데 필요한 고유의 시크릿 키 값 설정 ###
        JWT_SECRET_KEY = 'secret string',
    )

    # JWT 모듈을 flask 어플리케이션에 등록
    jwt_manager = JWTManager()
    jwt_manager.init_app(app)

    # blueprint 등록
    app.register_blueprint(IndexBp.bp)

    return app