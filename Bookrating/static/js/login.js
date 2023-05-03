$(document).ready(function () {
  $("form").submit(function (event) {
    if ($("#username").val() == "") {
      alert("Please Enter User Name");
      return false;
    }
    if ($("#password").val() == "") {
      alert("Please Enter Password");
      return false;
    }
    var formData = {
      fname: $("#username").val(),
      password: $("#password").val(),
    };
    // $.ajax({
    //   //  async: false,
    //   url: "/home",
    //   data: $("form").serialize(),
    //   type: "POST",
    //   success: function (response) {
    //     $("#msg").html(response);
    //     alert(response);
    //   },
    //   error: function (error) {
    //     alert("Error");
    //     console.log(error);
    //   },
    // });
    // event.preventDefault();
  });
});
