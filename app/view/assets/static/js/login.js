async function login() {
  alert("login button click");
  // form data 생성
  var formData = new FormData(document.getElementById("login_form"));
  
  // form data를 body에 포함시켜 요청
  await fetch('/login_with_cookies', {
      method: 'post',
      body : formData
  }).then(function(){
      // login 완료시 login form을 숨긴다
      document.getElementById("login_form").style.display = "none";
  });
  console.log(getCookie('csrf_access_token'));
}

async function logout() {
  await fetch('/logout_with_cookies', {method: 'post'});
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
  console.log(result);
  return result;
}