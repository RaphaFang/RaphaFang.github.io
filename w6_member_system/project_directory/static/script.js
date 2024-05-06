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

// function squareCounter() {
//   var posit_num = document.getElementById("posit_num").value;
//   if (posit_num < 1) {
//     alert("Please enter a positive number");
//   } else {
//     window.location.href = "/square/" + posit_num;
//   }
// }
