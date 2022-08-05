/* 로그인 
- form_data를 body에 포함시켜 요청
- 받은 데이터가 success일 경우
*/
async function login() {
  // form data 생성
  var formData = new FormData(document.getElementById("login_form"));
  
  // form data를 body에 포함시켜 요청
  await fetch('http://localhost:5000/signin', {
      method: 'post',
      body : formData,
  })
  .then((response)=>response.json())
  .then((data)=>{
    if(data["msg"]=="success"){
      // 로그인이 완료되면, "login_complete.html"로 이동한다.
      console.log("로그인성공");
      window.localStorage.setItem('access_token', data['access_token'])
      window.localStorage.setItem('refresh_token', data['refresh_token'])
      window.location.replace("login_complete.html");
    }
    else{
      console.log("로그인 실패");
    }
  })
  .catch(()=>{
    alert("로그인에 실패했습니다.");
  });
  
}