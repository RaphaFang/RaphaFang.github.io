"use strict";

document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("signup-form");
  var signup_username = document.getElementById("signup_username");
  var signup_user_id = document.getElementById("signup_user_id");
  var signup_password = document.getElementById("signup_password");

  form.addEventListener("submit", function (event) {
    if (
      signup_username.value.trim() === "" ||
      signup_user_id.value.trim() === "" ||
      signup_password.value.trim() === ""
      // trim(), 用來去除space的func，可以避免用戶只輸入空白
    ) {
      event.preventDefault();
      alert("Please make sure all fields are filled out.");
      console.log("submission canceled, found empty field");
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("signin-form");
  var username = document.getElementById("username");
  var password = document.getElementById("password");

  form.addEventListener("submit", function (event) {
    if (
      username.value.trim() === "" ||
      password.value.trim() === ""
      // trim(), 用來去除space的func，可以避免用戶只輸入空白
    ) {
      event.preventDefault();
      alert("Please make sure all fields are filled out.");
      console.log("submission canceled, found empty field");
    }
  });
});

function confirmDelete(event) {
  if (!confirm("確定刪除這筆留言？")) {
    event.preventDefault();
  }
}
