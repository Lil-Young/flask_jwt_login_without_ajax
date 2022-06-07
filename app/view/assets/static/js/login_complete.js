window.addEventListener('load', (event) =>{
    alert("새로고침 되었습니다.");
    /*
    새로고침시 리프레시 토큰을 API에 전송하여 만료된 토큰을 갱신하고 싶었으나 

    만료된 토큰으로 접근시 window.addEventListener('load', (event) =>{} 함수 접근이 안되었고, 

    데이터를 요청할 수도, 받은 데이터를 처리할 수 도 없었습니다.
    */
});

// 쿠키 가져오는 함수
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// 토큰이 만료되었는지 확인
// 토큰이 만료되었다면, 리프레시 토큰으로 재발행
// 리프레시 토큰도 만료되었으면 로그인화면으로 이동
async function check_token_update_validation(){
    // token이 만료되었는지 체크하는 요청 보내기
    await fetch("/check_token",{
        method:"post",
        headers: {
            'X-CSRF-TOKEN': getCookie('csrf_access_token'),
        },
    })
    .then((res)=>res.json())
    .then((res)=> {
        // 엑세스 토큰이 만료되었다면
        // silent-refresh API로 리프레시 토큰을 포함시켜 요청
        if(res["msg"]=="token has expired"){
            fetch("silent-refresh",{
                method:"post",
                headers:{
                    'X-CSRF-TOKEN': getCookie('csrf_refresh_token'),
                }
            })
            .then((res)=>res.json())
            .then((res)=>{
                // 만약 리프레시 토큰도 만료되면 -> 로그인화면으로 이동
                if(res["msg"]=="token has expired"){
                    window.location.href="/";
                }
            });
        }
    })
}
