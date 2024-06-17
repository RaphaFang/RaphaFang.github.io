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
