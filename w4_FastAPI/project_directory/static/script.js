"use strict";

function checkCheckbox() {
  var checkbox = document.getElementById("accept");
  if (!checkbox.checked) {
    alert("Please check the checkbox first");
    // 要想辦法阻擋進入才對
  } else {
    // You can add more code here to handle the case where the checkbox is checked
    // alert("checked!");
  }
}
