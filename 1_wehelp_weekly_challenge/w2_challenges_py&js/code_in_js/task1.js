function findAndPrint(messages, current_station) {
  // >>> given current_station = "Wanlong"
  const rebuildMessagesDict = {};
  const messageLocList = [];
  for (const k in messages) {
    for (const i in stations) {
      if (messages[k].includes(i)) {
        messageLocList.push(stations[i]);
      }
    }
  }
  for (const [key, value] of Object.entries(messages)) {
    rebuildMessagesDict[key] = messageLocList.shift();
  }
  // console.log(rebuildMessagesDict); // >>> { Leslie: 3.1, Bob: 12, Mary: 5, Copper: 17, Vivian: 1 }

  const relativePositionDict = {};
  const positionList = [];
  // this 2 part can't be displace by the Object.keys func below
  // even use announce "const relativePositionDict = ..." won't work

  const currentStationNum = stations[current_station]; // >>> 6

  Object.keys(rebuildMessagesDict).forEach((key) => {
    positionList.push(Math.abs(currentStationNum - rebuildMessagesDict[key]));
  });

  Object.keys(messages).forEach((key, index) => {
    relativePositionDict[positionList[index]] = key;
  });

  let min = positionList[0];
  positionList.forEach((item) => {
    if (item < min) {
      min = item;
    }
  });
  console.log(relativePositionDict[min]);
}

const messages = {
  Leslie: "I'm at home near Xiaobitan station.",
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Vivian: "I'm at Xindian station waiting for you.",
};

const stations = {
  Songshan: 19,
  "Nanjing Sanmin": 18,
  "Taipei Arena": 17,
  "Nanjing Fuxing": 16,
  "Songjiang Nanjing": 15,
  Zhongshan: 14,
  Beimen: 13,
  Ximen: 12,
  Xiaonanmen: 11,
  "Chiang Kai-Shek Memorial Hall": 10,
  Guting: 9,
  "Taipower Building": 8,
  Gongguan: 7,
  Wanlong: 6,
  Jingmei: 5,
  Dapinglin: 4,
  Xiaobitan: 3.1,
  Qizhang: 3,
  "Xindian City Hall": 2,
  Xindian: 1,
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

// Ｏ解決：js dictionary comprehension
//    https://stackoverflow.com/questions/11068247/in-javascript-a-dictionary-comprehension-or-an-object-map

// terminal:--------------------------------------------------------------------
// Mary
// Copper
// Leslie
// Bob
// Vivian
