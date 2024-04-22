"use strict";

function checkCheckbox() {
  var checkbox = document.getElementById("myCheckbox");
  if (!checkbox.checked) {
    alert("Please check the checkbox first");
  } else {
    // You can add more code here to handle the case where the checkbox is checked
    alert("Checkbox is checked!");
  }
}
