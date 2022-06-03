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
      // TODO: success가 왔는지 확인해야한다.
      if(data["msg"]=="success"){
          var user_id = data["user_id"];
          document.getElementById("user_id").innerHTML = user_id+"님 환영합니다.";
          // login 완료시 login form을 숨긴다
          document.getElementById("login_form").style.display = "none";

          // login 완료시 logout form을 보여준다.
          document.getElementById("logout_form").style.display = "";
      }

  })
  .catch(()=>{
    alert("로그인에 실패했습니다.");
  });
  
  console.log(getCookie('csrf_access_token'));
}

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

async function makeRequestWithJWT() {
  const options = {
    method: 'post',
    credentials: 'same-origin',
    // header에 csrf_access_token이 포함되어야한다.
    headers: {
      'X-CSRF-TOKEN': getCookie('csrf_access_token'),
    },
  };
  const response = await fetch('/protected', options);
  const result = await response.json();
  if(result["msg"]=="Token has expired"){
    console.log("token이 만료되었습니다.");
  }
  console.log(result);
  return result;
}