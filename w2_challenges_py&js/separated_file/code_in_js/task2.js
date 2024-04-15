function getPrice(ele) {
  return ele.price;
}

function getRate(ele) {
  return ele.rate;
}

function bookHourList(hour, duration) {
  let hourList = [];
  for (let b = hour; b < hour + duration; b++) {
    hourList.push(b);
  }
  return hourList;
} // console.log(bookHourList(15, 1));   // [15]

function timeOccupiedOrNotList(n, hourList) {
  let occupiedList = [];
  for (let k of hourList) {
    if (n.time.includes(k)) {
      occupiedList.push(true);
    } else {
      occupiedList.push(false);
    }
  }
  return occupiedList.some(Boolean);
}
// n = { name: "John", rate: 4.5, price: 1000, time: [15] };
// console.log(timeOccupiedOrNotList(n, bookHourList(15, 1)));
// >>> true

function printNameAndBreak(n, hour, duration) {
  for (let t = 0; t < duration; t++) {
    n.time.push(hour + t);
  }
  n.time.sort();
  console.log(n.name);
}

function book(consultants, hour, duration, criteria) {
  //   try {
  //     Boolean(consultants[0].time);
  //     console.log(Boolean(consultants[0].time));
  //   } catch (SyntaxError) {
  //     consultants.forEach((n) => (n["time"] = []));
  //   }
  // this won't work, because "Boolean(consultants[0].time);" return "false"
  // not SyntaxError

  for (let n of consultants) {
    if (!n.hasOwnProperty("time")) {
      n.time = [];
    }
  }

  if (criteria === "price") {
    consultants.sort((a, b) => getPrice(a) - getPrice(b));
    let count = 0;
    for (let n of consultants) {
      if (timeOccupiedOrNotList(n, bookHourList(hour, duration))) {
        count++;
      } else {
        printNameAndBreak(n, hour, duration);
        break;
      }
    }
    if (count === 3) {
      console.log("No Service");
    }
  } else if (criteria === "rate") {
    consultants.sort((a, b) => getRate(b) - getRate(a)); // >>> the [::-1] part at js
    let count = 0;
    for (let n of consultants) {
      if (timeOccupiedOrNotList(n, bookHourList(hour, duration))) {
        count++;
      } else {
        printNameAndBreak(n, hour, duration);
        break;
      }
    }
    if (count === 3) {
      console.log("No Service");
    }
  }
}

const consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

// Jenny 11 12 15
// John 10 11 14 15 16 20 21
// Bob  11
// print(consultants)

// Ｏ解決：py中使用的 try expect, didn't work
//    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch

// terminal:--------------------------------------------------------------------
// Jenny
// Jenny
// John
// John
// Bob
// No Service
// John

console.log("========task2 end========");
