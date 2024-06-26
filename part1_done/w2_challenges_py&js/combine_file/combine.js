function findAndPrint(messages, currentStation) {
  // >>> given current_station = "Wanlong"
  const stations = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Xiaobitan",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
  ];

  const messageStaList = [];
  for (const k of Object.values(messages)) {
    for (const i of stations) {
      if (k.includes(i)) {
        messageStaList.push(i);
      }
    }
  }
  const messageStaDict = Object.fromEntries(
    Object.keys(messages).map((key, index) => [key, messageStaList[index]])
  );

  const stationsWithoutXiaobitan = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
  ];
  let messageStaIndexDict = {};
  if (currentStation !== "Xiaobitan") {
    const fix = stationsWithoutXiaobitan.indexOf(currentStation);

    for (const [name, station] of Object.entries(messageStaDict)) {
      if (station === "Xiaobitan") {
        messageStaIndexDict[name] =
          Math.abs(fix - stationsWithoutXiaobitan.indexOf("Qizhang")) + 1;
      } else {
        const absoluteLoc = stationsWithoutXiaobitan.indexOf(station);
        const relativeLoc = Math.abs(fix - absoluteLoc);
        messageStaIndexDict[name] = relativeLoc;
      }
    }
  } else {
    const fix = stationsWithoutXiaobitan.indexOf("Qizhang");

    for (const [name, station] of Object.entries(messageStaDict)) {
      if (station === "Xiaobitan") {
        messageStaIndexDict[name] = 0;
      } else {
        const absoluteLoc = stationsWithoutXiaobitan.indexOf(station);
        const relativeLoc = Math.abs(fix - absoluteLoc) + 1;
        messageStaIndexDict[name] = relativeLoc;
      }
    }
  }

  const person = Object.keys(messageStaIndexDict).reduce((a, b) =>
    messageStaIndexDict[a] < messageStaIndexDict[b] ? a : b
  );
  console.log(person);
}

const messages = {
  Leslie: "I'm at home near Xiaobitan station.",
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Vivian: "I'm at Xindian station waiting for you.",
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

findAndPrint(messages, "Dapinglin"); // print Mary

// Ｏ解決：js dictionary comprehension
//    https://stackoverflow.com/questions/11068247/in-javascript-a-dictionary-comprehension-or-an-object-map

// terminal:--------------------------------------------------------------------
// Mary
// Copper
// Leslie
// Bob
// Vivian
// Mary

console.log("========task1 end========");

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

function func(...data) {
  let nameDict = {};
  for (let n of data) {
    if (n.length >= 4) {
      nameDict[n] = n[2];
    }
    if (n.length <= 3) {
      nameDict[n] = n[1];
    }
  }

  let countingList = Object.values(nameDict);
  let countingDict = {};
  for (let k of countingList) {
    countingDict[k] = countingList.filter((x) => x === k).length;
  }

  let minName = Math.min(...Object.values(countingDict));
  let checkMinList = Object.keys(countingDict).filter(
    (k) => countingDict[k] === minName
  );

  let reverseNameDict = Object.fromEntries(
    Object.entries(nameDict).map(([k, v]) => [v, k])
  );

  if (checkMinList.length === 1) {
    console.log(reverseNameDict[checkMinList[0]]);
  } else {
    console.log("沒有");
  }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

// terminal:--------------------------------------------------------------------
// 彭大牆
// 林花花
// 沒有
// 夏曼藍波安

console.log("========task3 end========");

function getNumber(index) {
  const tuple = [Math.floor(index / 3), index % 3];
  console.log(tuple[0] * 7 + tuple[1] * 4);
}

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70

// Ｏ解決：js的divmod
//      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor

// terminal:--------------------------------------------------------------------
// 4
// 15
// 25
// 70

console.log("========task4 end========");

function find(spaces, stat, n) {
  // >>> given find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) // print 5
  let available = spaces.map((space, i) =>
    stat[i] > 0 && space > 0 ? space : 0
  );
  // console.log(available); // >>> [0, 1, 0, 4, 3, 2]

  let avaMinusPassengerList = available.map((a) => a - n);
  // console.log(avaMinusPassengerList); // >>> [-2, -1, -2, 2, 1, 0]

  let fit = null;
  for (let i = 0; i < avaMinusPassengerList.length; i++) {
    for (let j = 0; j < avaMinusPassengerList.length; j++) {
      if (
        avaMinusPassengerList[i] >= 0 &&
        avaMinusPassengerList[i] < avaMinusPassengerList[j]
      ) {
        fit = i;
      }
    }
  }

  if (typeof fit === "number") {
    console.log(fit);
  } else {
    console.log(-1);
  }
}

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2

// terminal:--------------------------------------------------------------------
// 5
// -1
// 2

console.log("========task5 end========");
