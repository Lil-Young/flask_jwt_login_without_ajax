
/*
로그인이 되고나서의 js
*/
window.addEventListener('load', (event) =>{
    alert("새로고침");
    // protected 요청
    // 만약 access_token이 만료되었을 경우
    // refresh_token으로 재요청한다. 
    const response = fetch('/protected', {
        method: 'get',
        credentials: 'same-origin',
        // header에 csrf_access_token이 포함되어야한다.
        headers: {
          'X-CSRF-TOKEN': getCookie('csrf_access_token'),
        },
    });
    const result = response.json();
    console.log(result);
});
// 쿠키 가져오는 함수
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}