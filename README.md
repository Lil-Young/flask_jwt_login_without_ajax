# ajax없이 로그인 구현
- flask_jwt_extend를 공부하기 위한 예제 프로젝트입니다.

# flask API
- 로그인 ("/signin")
- 로그아웃 ("/logout_with_cookies") : 사용 X
- 보호된 페이지 접근 ("/protected")
- 토큰 확인 ("/check_token")
- 자동 리프레시 ("/silent-refresh")

# API Description
## 로그인 ("/signin")
- 웹으로부터 폼 데이터(form data)를 받습니다.
- form data로부터 사용자의 id, password를 추출하여 간단한 인증(id==pw=="test")을 수행합니다.
- 인증을 완료하면 다음을 수행합니다.
    - access_token, refresh_token을 발행
    - access_token, refresh_token을 쿠키에 저장 // set_****_cookies()
    - 응답메시지 생성후 응답
- 만약 인증이 되지 않을 경우 로그인 실패 응답메시지를 생성하여 보냅니다.

## 보호된 페이지 접근 ("/protected")
- 유효한 엑세스 토큰을 통해 접근할 수 있는 API입니다.
- 엑세스 토큰이 만료된채로 접근할 경우 에러 메시지를 반환시킵니다.
    - 이때 발생되는 에러메시지는 app.\_\_init\_\_.py의 
    - @jwt_manager.expired_token_loader의 콜백함수에 설정합니다.
- 정상적으로 접근했을 경우 'login_complete.html'을 랜더링하여 응답합니다.


## 토큰 확인 ("/check_token")
- 웹에서 보낸 토큰이 유효한지 확인하는 API입니다.
- 유효할 경우 "msg":"success" 메시지를 반환하며
- 유효하지 않을 경우 @jwt_manager.expired_token_loader에 설정된 메시지를 반환합니다.

## 자동 리프레시 ("/silent-refresh")
- 유효한 리프레시 토큰을 받아 엑세스 토큰과 리프레시 토큰을 재발행합니다.
- 재발행된 토큰들을 쿠키에 저장합니다.

# GET Started (Windows)
```
# Get Repository
> git clone https://github.com/songyw0517/flask_jwt_login_without_ajax.git
> cd flask_jwt_login_without_ajax

# virtual env
> py -3 -m venv venv
> venv\Scripts\activate

# Install dependency
> pip install -r requirements.txt

# set flask application
> set flask_app=manage:application

# App start
> flask run
```
