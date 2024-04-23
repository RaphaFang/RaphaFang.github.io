"use strict";

function checkCheckbox() {
  var checkbox = document.getElementById("accept");
  if (!checkbox.checked) {
    alert("Please check the checkbox first");
    // 要想辦法阻擋進入才對
  }
}
