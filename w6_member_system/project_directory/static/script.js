"use strict";

// 以後要監控畫面中元素狀態，並依照元素狀態作為條件執行，需要不斷去看整個文件，而不是只在按按鈕的當下
// 所以在按鈕設定 func，檢查狀態不夠準確

// Why Code 1 Works
// Consistency: The submit event listener is added only once, and it always checks the state of the checkbox at the time of submission, not before.
// No Redundancy: No redundant listeners are added, so each submit action is processed exactly once, preventing the multiple alert problem.

// the different from "DOMContentLoaded"
//The DOMContentLoaded event is a special type of event that fires once when the HTML document has been completely loaded and parsed. This event does not fire multiple times for a single page load; it's designed to run only once as the page finishes loading the initial HTML before it moves on to load external resources like images and stylesheets.

// document.addEventListener("DOMContentLoaded", function () {
//   // DOMContentLoaded, 檢查網頁完整loaded
//   var form = document.getElementById("signin-form");
//   var checkbox = document.getElementById("accept");

//   form.addEventListener("submit", function (event) {
//     if (!checkbox.checked) {
//       event.preventDefault();
//       alert("Please check the checkbox first");
//       console.log("submission canceled");
//     }
//   });
// });

function squareCounter() {
  var posit_num = document.getElementById("posit_num").value;
  if (posit_num < 1) {
    alert("Please enter a positive number");
  } else {
    window.location.href = "/square/" + posit_num;
  }
}

// 錯誤嘗試2. --------------------------------------------------------------------------------

// 這func的問題是，1. 他無法回到預設狀態（即便勾選accept）
// 2.會不斷跳出alert，隨著提交次數增加

// the answer from chat gpt:
// Analysis of Code 2 Problems
// Persistent Event Listeners:
// In Code 2, each time the button is clicked and the checkbox is not checked, a new submit event listener is added to the form. This results in multiple listeners stacking up on the same form. Each of these listeners will execute when the form attempts to submit, causing repeated alerts and prevention actions.
// The added listeners do not get removed. Therefore, once added, they continue to listen and react to the submit event, irrespective of the checkbox state in future submissions.
// Ineffective Event Handling:
// Since the new submit listeners are added during each button click when the checkbox is unchecked, they remain active and execute their logic every time the form is attempted to be submitted. This includes times when the checkbox might actually be checked after initially being unchecked, because the listeners were added before and were never removed.

// function checkCheckbox() {
//   var checkbox = document.getElementById("accept");
//   var form = document.getElementById("signin-form");
//   if (!checkbox.checked) {
//     form.addEventListener("submit", function (event) {
//       event.preventDefault();
//       console.log("submission canceled");
//       alert("Please check the checkbox first");
//     });
//   }
// }

// 錯誤嘗試1. --------------------------------------------------------------------------------
// form.removeAttribute("action");
// 移除 action 不有效
