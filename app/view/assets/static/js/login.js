

// 로그인
async function login() {
  // form data 생성
  var formData = new FormData(document.getElementById("login_form"));
  
  // form data를 body에 포함시켜 요청
  await fetch('/login_with_cookies', {
      method: 'post',
      body : formData
  })
  .then((response)=>response.json())
  .then(function(data){
      // success가 되었는지 확인
      if(data["msg"]=="success"){
          // 로그인이 완료되면, "/protected"페이지로 "변경"한다.
          window.location.replace("/protected");
      }
  })
  .catch(()=>{
    alert("로그인에 실패했습니다.");
  });
  
  console.log(getCookie('csrf_access_token'));
}

// 로그아웃
async function logout() {
    await fetch('/logout_with_cookies', {method: 'post'});
    // logout시 logout form을 숨긴다.
    document.getElementById("logout_form").style.display = "none";

    // logout시 login form을 보여준다.
    document.getElementById("login_form").style.display = "";
  console.log(getCookie('csrf_access_token'));
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

// 보호된 페이지로 이동
async function makeRequestWithJWT() {
  const options = {
    method: 'get',
    credentials: 'same-origin',
    // header에 csrf_access_token이 포함되어야한다.
    headers: {
      'X-CSRF-TOKEN': getCookie('csrf_access_token'),
    },
  };
  const response = await fetch('/protected', options);
  const result = await response.json();
  
  
  console.log(result);
  return result;
}

