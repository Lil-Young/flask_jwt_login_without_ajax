/*
로그인이 되고나서의 js
*/
window.addEventListener('load', (event) =>{
    alert("새로고침");
    

});
// 쿠키 가져오는 함수
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function test(){
    // token 만료 감지
    await fetch("/test",{
        method:"post",
        headers: {
            'X-CSRF-TOKEN': getCookie('csrf_access_token'),
        },
    })
    .then((res)=>res.json())
    .then((res)=>console.log("check"+res['msg']))
}