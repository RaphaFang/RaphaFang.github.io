"use strict";
document.addEventListener("DOMContentLoaded", function () {
  console.log("顯示查詢 username 內容");
  document
    .getElementById("start-fetch-button")
    .addEventListener("click", async function () {
      let username = document.getElementById("input_searching_name").value;
      // 這步驟記得寫在click func 的內部，每次點及後重新建議一個username的變數，而非在點擊前建立好
      console.log(username);
      let response = await fetch(
        `http://127.0.0.1:8000/api/member?username=${username}`
      );
      let data = await response.json();
      console.log(data);
      displayUserInfo(data["data"]);
    });

  console.log("顯示更新 username 成功與否");
  document
    .getElementById("update-button")
    .addEventListener("click", async function () {
      let new_username = document.getElementById("update_name_input").value;
      console.log(new_username);
      console.log(333);

      let response = await fetch(`http://127.0.0.1:8000/api/member`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: new_username }),
      });

      let result = await response.json();
      console.log(result);
      displayUserUpdateInfo(result);
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

function displayUserUpdateInfo(data) {
  let userInfoDiv = document.getElementById("update-SorF");
  if (data["ok"] === true) {
    userInfoDiv.innerHTML = "<p>更新成功</p>";
  } else {
    userInfoDiv.innerHTML = "<p>更新失敗</p>";
  }
}
