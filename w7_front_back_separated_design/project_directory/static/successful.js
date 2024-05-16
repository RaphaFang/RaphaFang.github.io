"use strict";
document.addEventListener("DOMContentLoaded", function () {
  console.log(111);
  document
    .getElementById("start-fetch-button")
    .addEventListener("click", async function () {
      let username = document.getElementById("input_searching_name").value;
      // 這步驟記得寫在click func 的內部，每次點及後重新建議一個username的變數，而非在點擊前建立好
      console.log(username);
      let response = await fetch(
        `http://127.0.0.1:8000/api/member/${username}`
      );
      let data = await response.json();
      console.log(data);
      displayUserInfo(data);
    });
});

function displayUserInfo(data) {
  let userInfoDiv = document.getElementById("searching_name_text");
  if (data["data"] === null) {
    userInfoDiv.innerHTML = "<p>No Data.</p>";
  } else {
    userInfoDiv.innerHTML = `
          <p>${data["name"]}(${data["username"]})</p>
      `;
  }
}
