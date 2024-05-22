// document.addEventListener("DOMContentLoaded", function () {
//   document
//     .getElementById("dataForm")
//     .addEventListener("submit", function (event) {
//       event.preventDefault();

//       let password = document.getElementById("password").value;
//       let passwordRegex = /^[A-Za-z0-9@#$%]{4,8}$/;

//       // if error, get feedback for user(optional)
//       let passwordError = document.getElementById("passwordError");
//       passwordError.textContent = "";

//       if (passwordRegex.test(password)) {
//         this.submit();
//       } else {
//         passwordError.textContent =
//           "Password must be 4-8 characters long and include only alphabets, numbers, and @#$%";
//       }
//     });
// });

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("dataForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      let email = document.getElementById("email").value;
      let password = document.getElementById("password").value;
      let tel = document.getElementById("tel").value;

      let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      let passwordRegex = /^[A-Za-z0-9@#$%]{4,8}$/;
      let telRegex = /^[0-9]{4}-[0-9]{3}-[0-9]{3}$/;

      let emailError = document.getElementById("emailError");
      let passwordError = document.getElementById("passwordError");
      let telError = document.getElementById("telError");

      emailError.textContent = "";
      passwordError.textContent = "";
      telError.textContent = "";

      if (!emailRegex.test(email)) {
        emailError.textContent = "Invalid email format";
      }
      if (!passwordRegex.test(password)) {
        passwordError.textContent =
          "Password must be 4-8 characters long and include only alphabets, numbers, and @#$%";
      }
      if (!telRegex.test(tel)) {
        telError.textContent = "Invalid tel format";
      }

      if (
        emailRegex.test(email) &&
        passwordRegex.test(password) &&
        telRegex.test(tel)
      ) {
        this.submit();
      }
    });
});

// const telInput = document.getElementById("tel");
// const telError = document.getElementById("telError");

// telInput.addEventListener("input", function (event) {
//   let value = telInput.value.replace(/\D/g, "");
//   let formattedValue = "";

//   if (value.length > 0) {
//     formattedValue = value.substring(0, 3);
//   }
//   if (value.length > 3) {
//     formattedValue += "-" + value.substring(3, 6);
//   }
//   if (value.length > 6) {
//     formattedValue += "-" + value.substring(6, 12);
//   } // value.substring(6, 12) automatically lock the max length you could input

//   telInput.value = formattedValue;
