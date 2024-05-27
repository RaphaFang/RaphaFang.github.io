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

console.log("========task1 end========");
