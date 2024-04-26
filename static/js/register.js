$(document).ready(function() {
  var userstitle = []
  var sentOtp=''
    $('#register').submit(function(event) {
      event.preventDefault();
  
      // Get form data
      var name = $('#name').val();
      var email = $('#email').val();
      var password = $('#password1').val();
      var confirmPassword = $('#confirm_password').val();
      var bookimage=$('#input-file')[0].files[0];;
  
      // Validate form data
      if (name == '' || email == '' || password == '' || confirmPassword == '') {
        alert('Please fill in all fields.');
        return;
      }
      
  
      if (password != confirmPassword) {
        alert('Passwords do not match.');
        return;
      }
  
      if (!isValidEmailAddress(email)) {
        alert('Invalid email address.');
        return;
      }
      if (name.length > 20) {
        alert('Name must be at most 20 characters long.');
        return;
      }
      userstitle.push(name);

      var formdata=new FormData();
      formdata.append('fname',name);
      formdata.append('email',email);
      formdata.append('password',password);
      formdata.append('file', bookimage);
      
      $.ajax({
        type: 'POST',
        url: '/call_otp',
        data:{email:email},
        success: function (response) {
          console.log(response)
          sentOtp = response
          alert('OTP has been sent to your Email!! Please Check the Inbox')

        },
        error: function () {
          alert('Error sending OTP please Try again later!!')
        }

      });

      var inputOTP = $('#otp').val();

      if (inputOTP == sentOtp)
      {
        $.ajax({
          type: 'POST',
          url: '/callregisterform',
          data: $('#register').serialize(),
          data:formdata,
          contentType:false,
          processData:false,
          success: function(response) {
            alert('Registration successful!');
            $('#msg').html(response);
            
            
          },
          error: function() {
          alert('Error processing registration. Please try again later.');
          }
        });
      }
      

  
      // Submit form data to server
      
    });
  });
  
  function isValidEmailAddress(email) {
    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
      