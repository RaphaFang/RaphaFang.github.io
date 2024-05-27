document.addEventListener("DOMContentLoaded", function () {
  // Function to get URL parameters
  function getParameterByName(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
  }

  // Function to display a greeting
  function displayGreeting() {
    const name = getParameterByName("name");
    console.log(name);
    // Directly inserting user input into the DOM without sanitization
    document.getElementById("greeting").innerHTML = "Hello, " + name + "!";
  }

  window.onload = displayGreeting;
  // console.log("11111");
});
