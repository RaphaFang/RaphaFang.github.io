document.addEventListener("DOMContentLoaded", function () {
  const output = document.getElementById("output");

  // Function to display output
  function displayOutput(data) {
    output.textContent = JSON.stringify(data, null, 2);
  }

  // Fetch from Google (should fail due to CORS policy)
  document.getElementById("fetchGoogle").addEventListener("click", () => {
    fetch("https://www.google.com")
      .then((response) => response.json())
      .then((data) => displayOutput({ state: true, data }))
      .catch((error) => displayOutput({ state: false, error: error.message }));
  });

  // ! the bypass method!!
  // document.getElementById("fetchGoogle").addEventListener("click", () => {
  //   fetch("http://localhost:8000/proxy/google")
  //     .then((response) => response.text())
  //     .then((data) => displayOutput(data))
  //     .catch((error) =>
  //       displayOutput({ success: false, error: error.message })
  //     );
  // });

  // Fetch from Taipei Attractions (should work if CORS headers are set)
  document.getElementById("fetchTaipei").addEventListener("click", () => {
    fetch(
      "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    )
      .then((response) => response.json())
      .then((data) => displayOutput({ success: true, data }))
      .catch((error) =>
        displayOutput({ success: false, error: error.message })
      );
  });

  // Fetch from Local API (needs to be set up with CORS)
  document.getElementById("fetchLocal").addEventListener("click", () => {
    fetch("http://localhost:3000/api/data")
      .then((response) => response.json())
      .then((data) => displayOutput({ success: true, data }))
      .catch((error) =>
        displayOutput({ success: false, error: error.message })
      );
  });

  // Log Origin, Simple Requests, Preflight Requests, and CORS Headers
  console.log("Origin:", window.location.origin);

  const simpleRequestHeaders = new Headers();
  simpleRequestHeaders.append(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );

  // Simple Request Example
  fetch("http://localhost:3000/api/simple", {
    method: "POST",
    headers: simpleRequestHeaders,
    body: "key1=value1&key2=value2",
  })
    .then((response) => response.json())
    .then((data) => console.log("Simple Request Data:", data))
    .catch((error) => console.error("Simple Request Error:", error));

  // Preflight Request Example
  const preflightRequestHeaders = new Headers();
  preflightRequestHeaders.append("X-Custom-Header", "value");

  fetch("http://localhost:3000/api/preflight", {
    method: "POST",
    headers: preflightRequestHeaders,
    body: JSON.stringify({ key1: "value1", key2: "value2" }),
  })
    .then((response) => response.json())
    .then((data) => console.log("Preflight Request Data:", data))
    .catch((error) => console.error("Preflight Request Error:", error));
});
