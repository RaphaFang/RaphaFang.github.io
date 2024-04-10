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
