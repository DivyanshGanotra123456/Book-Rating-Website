// function checkForm() {
//   var oldP = document.getElementById("oldP").value;
//   var newP = document.getElementById("newP").value;
//   var confirmP = document.getElementById("confirmP").value;

//   if (oldP != "" && newP != "" && confirmP != "") {
//     if (oldP != newP) {
//       if (newP == confirmP) {
//         return true;
//       } else {
//         alert("Confirm password is not same as you new password.");
//         return false;
//       }
//     } else {
//       alert(" This Is Your Old Password,Please Provide A New Password");
//       return false;
//     }
//   } else {
//     alert("All Fields Are Required");
//     return false;
//   }
// }

const modal = document.querySelector(".modal");
const btnCloseModal = document.querySelector(".close-modal");
const btnsOpenModal = document.querySelector('a[onclick="openModal()"]');

const openModal = function (e) {
  e.preventDefault();
  modal.classList.remove("hidden");
};

const closeModal = function () {
  modal.classList.add("hidden");
};
btnsOpenModal.addEventListener("click", openModal);

btnCloseModal.addEventListener("click", closeModal);
