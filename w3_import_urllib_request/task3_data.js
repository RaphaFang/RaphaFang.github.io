const src1 =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";

fetch(src1)
  .then((response) => {
    if (response.ok) {
      return response.json();
    }
  })
  .then((data1) => {
    // Assuming data1 is already defined and contains the necessary data
    for (let n of data1.data.results) {
      console.log(data1.data.results[0].stitle);
      let filelist = data1.data.results[0].filelist;
      let jpgIndex;
      if (filelist.indexOf(".jpg") === -1) {
        jpgIndex = filelist.indexOf(".JPG");
      } else {
        jpgIndex = filelist.indexOf(".jpg");
      }
      let ImageURL = filelist.substring(0, jpgIndex + 4);
      console.log(ImageURL);
    }

    // You can now work with the data1 object here
  });
