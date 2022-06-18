window.addEventListener('load', (event) =>{
    alert("새로고침 되었습니다.");
    if (window.localStorage.getItem('access_token') == undefined) {
        window.location.href="login_index.html";
    }
    // access token이 유효한지 확인
    fetch("http://localhost:5000/check_access_token",{
        method:"post",
        headers:{
            "Authorization": "Bearer " + window.localStorage.getItem('access_token'),
            'Content-Type': 'application/json'
        }
    })
    .then((res) => res.json())
    .then((res) =>{
        if(res["msg"]=="token has expired"){
            // 엑세스 토큰이 만료된 블록
            // 2. 리프레시 토큰으로 다시 요청한다.
            fetch("http://localhost:5000/check_refresh_token",{
                method:"post",
                headers:{
                    'Authorization': "Bearer " + window.localStorage.getItem('refresh_token'),
                    'Content-Type': 'application/json'
                }
            })
            .then((res)=>res.json())
            .then((res)=>{
                if(res["msg"]=="token has expired"){
                    // 리프레시 토큰도 만료된 블록
                    console.log("리프레시 토큰 만료");
                    window.location.href="login_index.html"; // 로그인 화면으로 이동
                }
                else{
                    console.log("리프레시 토큰으로 접근 완료");
                    window.localStorage.setItem('access_token', res['access_token'])
                    window.localStorage.setItem('refresh_token', res['refresh_token'])
                    window.location.reload();
                }
            });
        }else{
            console.log("엑세스 토큰으로 접근 완료");
        }
    })
});


// 쿠키 가져오는 함수
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
