function getPrice(ele) {
  return ele.price;
}

function getRate(ele) {
  return ele.rate;
}

function bookHourList(hour, duration) {
  return Array.from({ length: duration }, (k, i) => hour + i);
}

console.log(bookHourList(10, 2));
