document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("dataForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      let password = document.getElementById("password").value;
      let passwordRegex = /^[A-Za-z0-9@#$%]{4,8}$/;

      // if error, get feedback for user(optional)
      let passwordError = document.getElementById("passwordError");
      passwordError.textContent = "";

      if (passwordRegex.test(password)) {
        this.submit();
      } else {
        passwordError.textContent =
          "Password must be 4-8 characters long and include only alphabets, numbers, and @#$%";
      }
    });
});
