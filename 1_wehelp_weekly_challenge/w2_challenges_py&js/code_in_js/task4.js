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
