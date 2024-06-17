"use strict";
// hoisting concept

// var
console.log(a); // undefined
var a = 5;
console.log(a); // 5

// let const
console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 10;
console.log(c); // ReferenceError: Cannot access 'c' before initialization
const c = 15;

// func.
// 1. Function Declaration
hoistedFunction(); // "hoisting test: Function Declaration"
function hoistedFunction() {
  console.log("hoisting test: Function Declaration");
}

// 2. Function Expression
expressionFunction(); // TypeError: expressionFunction is not a function
var nonHoistedFunction = function () {
  console.log("Function Expression is not hoisted");
};

// 3. Arrow Function
arrowFunction(); // TypeError: arrowFunction is not a function
var arrowFunction = () => {
  console.log("Arrow function is not hoisted");
};

// 4. Function Constructor （函數構造器，通常在安全性上有問題，不建議使用）
functionConstructor(); // TypeError: functionConstructor is not a function
var functionConstructor = new Function(
  'console.log("Function constructor is not hoisted");'
);
functionConstructor();

// 5. method
var obj = {
  method() {
    console.log("Method is called");
  },
};
obj.method(); // "Method is called"

// 6. Class Methods
class MyClass {
  myMethod() {
    console.log("Class method is called");
  }
}
const myInstance = new MyClass();
myInstance.myMethod(); // "Class method is called"

// --------------------------------------------------------
// 寫入
function fetchAndStoreImage(url, storageKey) {
  fetch(url)
    .then((response) => response.blob()) // 將資料轉換為 Blob （Binary Large Object）
    .then((blob) => {
      const reader = new FileReader();
      reader.onloadend = function () {
        sessionStorage.setItem(storageKey, reader.result); // 將 Base64 字符串存儲到 SessionStorage
        console.log("Image stored in SessionStorage");
      };
      reader.readAsDataURL(blob); // 讀取為 Base64 字符串，更好的成現在hyml
    });
}
fetchAndStoreImage("url", "storageKey");

// --------------------------------------------------------
// 讀取
document.addEventListener("DOMContentLoaded", () => {
  loadImageFromSessionStorage("storageKey", "replacedImgElementId");
});

function loadImageFromSessionStorage(storageKey, replacedImgElementId) {
  const dataURL = sessionStorage.getItem(storageKey);
  if (dataURL) {
    const imgElement = document.getElementById(replacedImgElementId);
    imgElement.src = dataURL;
  }
}

// --------------------------------------------------------
// function fetchAndStoreImages(apiUrl, storageKey) {
//   fetch(apiUrl)
//     .then((response) => response.json()) // 假設 API 返回一個包含多個圖片 URL 的 JSON 數組
//     .then((imageUrls) => {
//       // 創建一個 Promise 列表，每個 Promise 處理一個圖片 URL
//       const fetchPromises = imageUrls.map((url) =>
//         fetch(url)
//           .then((response) => response.blob())
//           .then((blob) => {
//             return new Promise((resolve, reject) => {
//               const reader = new FileReader();
//               reader.onloadend = () => {
//                 resolve(reader.result);
//               };
//               reader.onerror = reject;
//               reader.readAsDataURL(blob);
//             });
//           })
//       );
//       return Promise.all(fetchPromises);
//     })
//     .then((base64Images) => {
//       // 將處理後的 Base64 圖片數組存儲在 SessionStorage 中
//       sessionStorage.setItem(storageKey, JSON.stringify(base64Images));
//       console.log("Images stored in SessionStorage");
//     })
//     .catch((error) => {
//       console.error("Error fetching images:", error);
//     });
// }
