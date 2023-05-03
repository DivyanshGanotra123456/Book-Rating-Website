# DivyanshGanotra123456.github.io
# images and videos are at the end .In case if my webhosting does not work i request you to see all the youtube video links i shared at the end to see its working
Book Rating Website
# Formatting using HTML 
First I design webpages using HTML which sets the basic format of the file 
These pages includes are Registration page,login page,Help and Support ,AddBook page,Login Page,Home Page and Mainpage(Please Note all of them is still not working properly)

# Designing Webpages using CSS 
I use Cascading Style sheets for better interactive environment for the user .CSS is used to provide links,buttons for the submission and Storing the data.

#  Using Database 
![image](https://user-images.githubusercontent.com/110733562/235868574-afc7748d-9e20-4f37-b790-edf283ce4eef.png)
above link is the schema i thought . By connecting form with register we can store the users in the databases and while using login page only those users are allowed 
who are already stored in the database with their username,Password and email. Such that those with unique username and password will get connected with the homepage.
Similarly I can add new book by storing it in the database.


con = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='Ganotra123#', database='bookrating')
Above line is used to connect Mysql Database 

# Registration Page
@app.route('/callregister')
def callregistration():
    return render_template('registration_form.html')
    
    Using This code  to render HTML templates and return them as responses to HTTP requests.
    
    $(document).ready(function() {
    var userstitle=[]
    $('#register').submit(function(event) {
      event.preventDefault();
  
      // Get form data
      var name = $('#name').val();
      var email = $('#email').val();
      var password = $('#password1').val();
      var confirmPassword = $('#confirm_password').val();
      var bookimage=$('#input-file')[0].files[0];
      
      This javascript code is triggered by clicking on submit button present in HTML file
      where it collects the value from the form and first check whether the name,password and email you are submitting are applicable or not by using this code:
      
      
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
      if (name.length > 10) {
        alert('Name must be at most 10 characters long.');
        return;
      }
      
      If any of the above situation is not satisfied it will not submit the form
      
      
      function isValidEmailAddress(email) {
    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
  This code above is used to check whether the email id i used is valid or not
  
  formdata.append('fname',name);
      formdata.append('email',email);
      formdata.append('password',password);
      formdata.append('file',bookimage);
      
      This is used to append the value in the form These values will be sent as part of a HTTP request to a server-side script to be processed and stored in a database
      
  AJAX call is made for the '/callregistrationform' for the POST request 
  cursor = con.cursor()
           
        
        
        query = "insert into users(username,emailid,password,image_path) values(%s, %s,%s,%s)"
       
        val = (name,name1,name2,image_path)        
        
        try:
            
            cursor.execute(query,val)
            
        except Exception as e:
            print("Exception caught:", e)
            return 'Sorry !!Same Username has already registered'
        except:
            print('Unknown error occurred')
            return 'Sorry !!Some Error Occured'
        con.commit()
        data = cursor.rowcount
        print("Number of rows affected:", data)
        cursor.close()
        if data > 0:
            return "Sucessfully Registered!! Please Click on the sign in link"
        
        else:
            return "User does not added. Some Error Occured"
    else:
        return "Enter the name of new User"
    
This above code query is used to implement the data stored in the form . con.commit store username,emailid,password and confirm password in the database.If there 
is some exception it will return an error and do not store values in the database.


# Login page
Initially request.method is not 'POST' so it will return render_template('login.html') 

![image](https://user-images.githubusercontent.com/110733562/235906206-9ceff55e-b1d6-4448-b817-4f2f84e521e5.png)

    It will use javascript code in JS where it will check whether the form is empty or not if empty it will show alert and do not proceed further.
    formdata is used to send the request to the server.which will compare fname and password with database query= query="select * from users where username='"+fname+"' and password='"+password+"'"
    If username password does not match it will  message='Invalid Username/Password'
            return render_template("login.html",message=message)
    if both username and passwords match it will return render_template('basic_structure.html') which is the homepage of the website
    
    
    
  # Extractive summarization for addition of the book
    i used to add new books in the basic_structure.html first i will explain you about extractive summarization method i used method is 
    stored in summarization.py and then i import this function in python flask file by applying url link in the webpage it will trigger the 
![image](https://user-images.githubusercontent.com/110733562/235907700-a4abe370-09a0-44f1-937f-43d2435a56a1.png)

If there is summary it will render summary as well otherwise empty column.


![image](https://user-images.githubusercontent.com/110733562/235879663-4075d0df-f079-4279-8595-c935e4d7b07c.png)
Above image is the example how the code generete the summary from the wikipedia page.


Extractive Summarization: Sequence for extractive summarization:

1. Input text: original text we want to summarize
2. Text preprocessing: Cleaning and transforming of raw text data
that can be processed by the machine learning model. Function is
to remove voice and irrelevant text from the data. This may involve
tasks such as sentence segmentation, tokenization, removing stop
words, and stemming
3. Feature extraction: To extract meaningful features from the raw
data. To convert into the structural set for the valid information.
Important feature include frequency of the text ,,number of times it
appears and position of the sentence.
4. Sentence scoring: This method gives score to each sentence in a
document based on the importance of the overall meaning of the
Generation of an Idea
text. The sentences with high scores are selected to form the
summary. It allows important information to be extracted from the
data. By carefully selecting the sentence based on the high score.
5. Ranking sentences: Rank the sentence on the basis of the
relevance.The top ranked sentences will be the one that will
included in the summary.
6. Summary generation: Involves selecting a subset of the most
important sentences or phrases from the original text and
concatenating them to form a summary. This approach is often
simpler and more accurate than abstractive summarization, but it
may not be able to generate summaries that capture the full
meaning and nuances of the original text.


# Change Password
using hover property a form for change password appears which is used to change the password when i click on the link present in basic_structures.html()
<li><a onclick=openModal() href="{{url_for('changepassword1')}}">Change Password2</a></li>
it will trigger ('/change_password')
fname = session.get('fname')//It is used to set the username of the user who is using the website.
![image](https://user-images.githubusercontent.com/110733562/235907104-0c9f3b71-26be-4e60-85c5-463e5b7f682e.png)


 
 The whole code above will update the new password and store the new password in the database.
 var_books1=books is used to call all the books stored in the database using jinja template.
 
 # Profile-photo
 
 By trigerring the submit button on the registration_form.html it will trigger ('/callregister) which will render_template('registration_form.html') 
 in registration form it will trigger the register.js in which the code is first check whether the passeword and username are valid or not then it will store the 
 value in the formdata if fname!='' it will store values using 
 name = request.form['fname']
        name1=request.form['email']
        name2=request.form['password']
        image_path = ""
        
        
        
 print('Request files are here:-->', request.files)
        if 'file' in request.files:
            file=request.files['file']
           
            print('File is here:--->', file)
            if file.filename!='':
                filename=secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                image_path = image_path = 'static/images/' + filename
                print('Image path in registration', image_path)
                session['file'] = image_path
        cursor = con.cursor()
           
 The request.files object contains any files that were uploaded as part of the HTTP request. In this code, the if 'file' in request.files statement checks if a file was uploaded with the name file. If a file was uploaded, it is retrieved from the request.files object using the request.files['file'] syntax and stored in the file variable.

The secure_filename function from the werkzeug.utils module is then used to ensure that the filename is safe and does not contain any malicious characters. The os.path.join function is used to construct a path to the directory where the file should be saved. In this case, it is the UPLOAD_FOLDER specified in the Flask app configuration.

The file is then saved to the specified directory using the file.save method. Finally, the image_path variable is set to the path of the saved image, and stored in the user's session for later use. The cursor object is then created to interact with the database.
Then using jinja template it will further store profile picture on other pages.
To store the profile photo with username we need to attach the string 

        
 return render_template('basic_structure.html', var_books1=books,fname=session.get('fname'),image_path=session.get('file')) to call username and profile photo
 
 
 # searchbar
![image](https://user-images.githubusercontent.com/110733562/235908351-22e3291b-88b3-4b7f-86d3-56ea10167a36.png)

       

Flask handles POST request sent to the server when the user searches for a book. Then use the cursor.cor() to execute the sql query. which retrieves the search category and search term 
if search_category == 'book-title':
it will execute  query = "SELECT booktitle, author, genre, imgname FROM books WHERE booktitle LIKE %s"
            search_term = '%' + search_term + '%'
            cursor.execute(query, (search_term,))
            
 similarly for 'author' and 'genre' it varies if it do not fetch any values it will render_template('empty.html')
 
  books = []
        for row in result:
            book = {
                'Title': row[0],
                'Author': row[1],
                'Genre': row[2],
                'Image': row[3]
            }
            books.append(book)
        return render_template('basic_structure.html', var_books1=books,fname=session.get('fname'),image_path=session.get('file'))
    else:
        return render_template('basic_structure.html')
The function first retrieves the values of the search category and search term fields from the request form. It then initializes a database cursor and constructs a SQL query based on the selected search category and search term. 
The query is then executed and the results are fetched as a list of tuples. The function iterates through the list of tuples and creates a dictionary for each book  mapped to the corresponding values from the tuple. Each dictionary is then appended to a list of books.

# Images
 # Registration Page:![image](https://user-images.githubusercontent.com/110733562/235893022-c8aaca04-a869-49bd-b441-9d94b9a5f9a9.png)
 # loginpage:![image](https://user-images.githubusercontent.com/110733562/235893242-7f31d805-e629-42d8-b4cc-f05ea7d43702.png)
 # Homepage:![image](https://user-images.githubusercontent.com/110733562/235893456-3cb1d799-13d1-4b69-9826-6942d9cd04b0.png)
 # Add Book:![image](https://user-images.githubusercontent.com/110733562/235893663-398d810c-3cc6-459a-9017-82db684a8a78.png)

# Videos
# Video Link1: https://www.youtube.com/watch?v=rnjrU-_jaF8
# Video Link2: https://www.youtube.com/watch?v=brrR4JLj3Pw
# Video Link3: https://www.youtube.com/watch?v=-RXTlvE1zFw
# Video Link4: https://youtu.be/zxD1uxEbvLI
# Video Link5: https://youtu.be/kYvHc51I-CE
# Video Link6: https://www.youtube.com/watch?v=8qsW3a0uijM
# Video Link7: https://www.youtube.com/watch?v=QQzBhwNqms0
# Video Link8:https://www.youtube.com/watch?v=4xJLz9l6BoY
# Video Link9:https://www.youtube.com/watch?v=PP7WavWCvGY


