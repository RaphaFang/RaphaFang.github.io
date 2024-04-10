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
