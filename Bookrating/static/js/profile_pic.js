const image_input = document.querySelector("#input-file");
var uploaded_image = "";
image_input.addEventListener("change", function () {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    uploaded_image = reader.result;
    console.log("Reader result is here:", reader.result);
    // document.querySelector("#imagee").style='url(${uploaded_image})';
    document.querySelector("#profile-pic").src = uploaded_image;
  });
  console.log("File information:", this.files[0]);
  reader.readAsDataURL(this.files[0]);
  console.log("Preview string:", uploaded_image);
});
