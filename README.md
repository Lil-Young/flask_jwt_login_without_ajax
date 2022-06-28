# ajax없이 로그인 구현
- flask_jwt_extend를 공부하기 위한 예제 프로젝트입니다.

# flask API
- 로그인 ("/signin")
- 로그아웃 ("/logout_with_cookies") : 사용 X
- 엑세스 토큰 확인 ("/check_access_token")
- 리프레시 토큰 확인 ("/check_refresh_token)
- 보호된 페이지 접근 ("/protected_page")

# API Description
## 로그인 ("/signin")
- 웹으로부터 폼 데이터(form data)를 받습니다.
- form data로부터 사용자의 id, password를 추출하여 간단한 인증(id==pw=="test")을 수행합니다.
- 인증을 완료하면 다음을 수행합니다.
    - access_token, refresh_token을 발행
    - access_token, refresh_token을 응답(response)에 포함시키기
    - 응답메시지 반환
- 만약 인증이 되지 않을 경우 로그인 실패 응답메시지를 생성하여 보냅니다.

## 엑세스 토큰 확인 ("/check_access_token")
- 엑세스 토큰이 포함된 요청을 받아 엑세스 토큰이 유효한지 확인하여 응답합니다.
- 유효한 경우 {
    "msg":"success",
    "identity":identity
    } 메시지를 반환합니다.
- 유효하지 않은 경우 app/\_\_init\_\_.py의
@jwt_manager.expired_token_loader에 정의되어 있는 메시지로 응답합니다.

    {msg':'token has expired','result': 'fail'}

## 리프레시 토큰 확인 ("/check_refresh_token")
- (엑세스 토큰이 만료된 경우,) 리프레시 토큰이 포함된 요청을 받아 리프레시 토큰이 유효한지 확인합니다.
- 리프레시 토큰이 유효할 경우 엑세스 토큰을 재발행하고, 쿠키에 저장합니다.
- 정상적으로 작동할 경우(리프레시 토큰이 유효한 경우)

    {"msg":"success","identity":identity}를 반환합니다.
- 정상적으로 작동하지 않을 경우(리프레시 토큰이 유효하지 않을 경우)
@jwt_manager.expired_token_loader에 정의되어 있는 메시지로 응답합니다.

    {msg':'token has expired','result': 'fail'}

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

# 피드백
- SSR이 아닌 CSR구조로 변경한다면 새로고침 시, js를 통해 refresh토큰을 보낼 수 있을 것이다.