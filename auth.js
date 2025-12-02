const BASE_URL = "http://127.0.0.1:8000";

console.log("auth.js loaded"); 

const getValue = (id) => {
  const value = document.getElementById(id).value;
  return value;
};

const handleRegistration = (event) => {
  event.preventDefault();
  const username = getValue("username");
  const first_name = getValue("first_name");
  const last_name = getValue("last_name");
  const email = getValue("email");
  const password = getValue("password");
  const confirm_password = getValue("confirm_password");
  const info = {
    username,
    first_name,
    last_name,
    email,
    password,
    confirm_password,
  };

  if (password === confirm_password) {
    document.getElementById("error").innerText = "";
    if (
      /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(
        password
      )
    ) {
      console.log("Registration payload:", info);

      fetch(`${BASE_URL}/patient/register/`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(info),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("Registration response:", data);
        })
        .catch((err) => {
          console.error("Registration error:", err);
        });
    } else {
      document.getElementById("error").innerText =
        "pass must contain eight characters, at least one letter, one number and one special character:";
    }
  } else {
    document.getElementById("error").innerText =
      "password and confirm password do not match";
    alert("password and confirm password do not match");
  }
};

const handleLogin = (event) => {
  event.preventDefault();
  console.log("handleLogin called");  // debug

  const username = getValue("login-username");
  const password = getValue("login-password");
  console.log("Login input:", username, password);

  if (username && password) {
    fetch(`${BASE_URL}/patient/login/`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ username, password }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("Login response:", data);

        if (data.token && data.user_id) {
          localStorage.setItem("token", data.token);
          localStorage.setItem("user_id", data.user_id);
          window.location.href = "index.html";
        } else {
          alert("Login failed. Check username/password.");
        }
      })
      .catch((err) => {
        console.error("Login error:", err);
        alert("Something went wrong while logging in.");
      });
  } else {
    alert("Please enter username and password.");
  }
};
