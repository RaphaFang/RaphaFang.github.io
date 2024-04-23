"use strict";

function checkCheckbox() {
  var checkbox = document.getElementById("accept");
  var form = document.getElementById("signin-form");
  if (!checkbox.checked) {
    form.removeAttribute("action");
    alert("Please check the checkbox first");
  } else {
    form.setAttribute("action", "/signin");
  }
}
