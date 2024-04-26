import smtplib
import traceback
import ssl
from email.message import EmailMessage
from flask import Flask, flash,render_template, json, request,redirect, url_for, jsonify,session,g
from flask_mail import Mail
import pickle
import numpy as np
import pandas as pd
# from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import summarization
import os
from werkzeug.utils import secure_filename
import base64
popular_books= pd.read_pickle('popular_books.pkl')
book_pivot= pd.read_pickle('book_pivot.pkl')
books= pd.read_pickle('books.pkl')
similarity_score= pd.read_pickle('similarity_score.pkl')


app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#For sending mail
app.config.update(
    MAIL_SERVER = 'smtp.rediffmailpro.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'BooksRating@rediffmail.com',
    MAIL_PASSWORD = 'Billu123#'
)
mail = Mail(app)

#Generate Random OTP
import random

def otp():
    c=''
    l=1
    p=4
    while l<=p:
        n=random.randint(48,122)
        if ((n>57 and n<65) or (n>90 and n<97)):
            continue
        else:
            c+=chr(n)
            l=l+1
    return c


app.secret_key = os.urandom(24)

con = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='Ganotra123#', database='bookrating')

@app.route('/checkuser')
def checkuser():
    if session.get('fname'):
        return True
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('fname',None)
    return redirect(url_for('login'))
@app.route('/')
def home():
    if checkuser() == True:
        if request.method=='POST' and  request.form['fname'] !='':
            cursor=con.cursor()
            query="SELECT booktitle, author, genre, imgname,commentcount,ratingcount FROM books LIMIT 10"

            cursor.execute(query)
            
            result=cursor.fetchall()
            books=[]
            for row in result:
                book={
                    'Title':row[0],
                    'Author':row[1],
                    'Genre':row[2],
                    'Image':row[3],
                    'Comments':row[4],
                    'Ratings':row[5]
                }
                books.append(book)
            
            return render_template('basic_structure.html',var_books1=books)
    return redirect(url_for('login'))





@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

def homepage():
    cursor=con.cursor()
   
    
    query=''' SELECT * FROM ( SELECT bookid,booktitle, author, genre,ratingcount,commentcount, imgname FROM BOOKS) B LEFT JOIN 
( SELECT IFNULL(BOOKID,0) AS BOOKID, IFNULL(ROUND(AVG(ratings),1),0) AS AVG_RATING , count(ratings) AS RATINGS 
		FROM COMMENTSRATING WHERE commentstatus='V' group by bookid) C ON B.BOOKID = C.BOOKID'''
    cursor.execute(query)
    result=cursor.fetchall()
    books=[]
    for row in result:
        book={
            'Title':row[1],
            'Author':row[2],
            'Genre':row[3],
            # 'Description':result[0][4],
            'Ratings':row[9],
            'Comments':row[5],
            'Image':row[6],
            'Average':row[8]
        }
        
        books.append(book)
    return books
@app.route('/top_books')
def index():
    return render_template('index.html',
                           book_names= list(popular_books['title'].values),
                           authors=list(popular_books['author'].values),
                           votes=list(popular_books['num_ratings'].values),
                           ratings=list(popular_books['avg_ratings'].values),
                           images=list(popular_books['image'].values))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=["post"])
def recommend():
    user_input= request.form.get("user_input")
    book_index = np.where(book_pivot.index == user_input)[0][0]
    suggested_items = sorted(list(enumerate(similarity_score[book_index])), key=lambda x: x[1], reverse=True)[1:5]
    book_list = list(books["title"].values)

    data = []
    for i in suggested_items:
        item = []
        temp = books[books["title"] == book_pivot.index[i[0]]]
        item.extend(temp.drop_duplicates("title")['title'].values)
        item.extend(temp.drop_duplicates("title")['author'].values)
        item.extend(temp.drop_duplicates("title")['image'].values)

        data.append(item)
    return render_template('recommend.html', data=data)



@app.route('/callhomepage',methods=['POST','GET'])
def callhomepage():
    
    if checkuser() == True:
        books = homepage()
        image_path = session.get('file')
        return render_template('basic_structure.html',var_books1=books, title='Home Page',fname=session.get('fname'),image_path=image_path)
    return redirect(url_for('login'))

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST' and request.form['fname'] and request.form['password']:
        fname=request.form['fname']
        password=request.form['password']
        cursor=con.cursor(dictionary=True)
        query="select * from users where username='"+fname+"' and password='"+password+"'"
        try:
            cursor.execute(query)
        except:
            message='Invalid Username/Password'
            render_template('login.html',message=message)
        records=cursor.fetchall()
        data=cursor.rowcount
        cursor.close()
        uid=0
        for row in records:
            uid=row['userid']
            image_path = row['image_path']
            email_id=row['emailid']
        if data>0:
            session['fname']=fname
            session['uid']=uid
            session['file']=image_path
            session['email']= email_id
            
            
            return redirect(url_for('callhomepage'))
        else:
            message='Invalid Username/Password'
            return render_template("login.html",message=message)
    else:
        return render_template('login.html')





@app.route('/changepassword1',methods=['POST','GET'])
def changepassword1():
    if request.method=='POST':
        if request.form['password_old'] !='' or request.form['password_new'] !='' or request.form['confirm-password'] !='':
            if request.form['password_new'] == request.form['confirm-password']:
                password_old=request.form['password_old']
                password_new=request.form['password_new']
                fname = session.get('fname')
                cursor=con.cursor(dictionary=True)
                query="select * from users where username='"+fname+"' and password='"+password_old+"'"
                try:
                    cursor.execute(query)
                except:
                    message='Invalid Old Password'
                    render_template('basic_structure.html',message=message)
                records=cursor.fetchall()
                data=cursor.rowcount
                cursor.close()
                uid=0
                for row in records:
                    uid=row['userid']
                if data>0:
                    session['fname']=fname
                    session['uid']=uid
                    cursor=con.cursor(dictionary=True)
                    query="update users set password = '"+ password_new +"' where username='"+fname+"' and password='"+password_old+"'"
                    cursor.execute(query)
                    con.commit()
                    cursor.close()
                    message='Password Updated sucessfully'
                    books = homepage()
                    print(message)
                    return redirect(url_for('logout'))
                else:
                    message='Old Password does Not match with the original password'
                    return render_template("basic_structure.html",message=message)
            else:
                message='New Password and Confirm Password does not match'
                return render_template('basic_structure.html',message=message)
        else:
            message='Please Enter Old Password, New Password and Confirm Password'
            render_template('basic_structure.html',message=message)
    else:
        return render_template('login.html')
    return render_template('login.html')




@app.route('/call_otp',methods=['POST'])
def send_email():
    email_sender = 'divyanshganotra18@gmail.com'
    email_password = 'tcgphhtffdmltlsi'
    email_receiver = request.form['email']

    if not email_receiver:
        return "Email Address Not Provided"

    sent_otp = otp()
    session['sent_otp']=sent_otp
    session['email']= email_receiver
        
        


    subject = 'OTP for Registration on BooksRating'
    body = "Your OTP for registration is: " + sent_otp

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return sent_otp


@app.route('/callregisterform', methods=['GET', 'POST'])
def callregistrationform():
    
    if request.method == 'POST':
       
        input_otp = request.form.get('otp')
        sent_otp = session.get('sent_otp')
       
        if input_otp != sent_otp or not input_otp:
            error_message = 'Invalid OTP. Please try again later.'
            return render_template('registration_form.html', error_message=error_message)

        session.pop('sent_otp', None)
       

        name = request.form['fname']
        name1 = request.form['email']
        name2 = request.form['password']
        image_path = ""

        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_path = 'static/images/' + filename

        cursor = con.cursor()
        query = "INSERT INTO users (username, emailid, password, image_path) VALUES (%s, %s, %s, %s)"
        val = (name, name1, name2, image_path)
        try:
            cursor.execute(query, val)
        except Exception as e:
            return 'Sorry! The same username has already been registered.'

        con.commit()
        data = cursor.rowcount
        cursor.close()
        if data > 0:

            return render_template('registration_form.html', success_message='Successfully Registered! Please click on the sign-in link.')
        else:
            error_message = 'User not added. Some error occurred.'
            return render_template('registration_form.html', error_message=error_message)

    else:
        return render_template('registration_form.html')

@app.route('/calllogin')
def calllogin():
    return render_template('login.html')



@app.route('/callgenre')
def callgenre():
    return render_template('add_genre.html')



@app.route('/callgenreform',methods=['POST'])
def callgenreform():
    if request.form['fname'] !='':
        _name = request.form['fname']
        cursor = con.cursor()
        query = 'insert into genres(genre) values(%s)'
        val = (_name,)
        try:
            cursor.execute(query,val)
        except Exception as e:
            return 'Error: Genre Already Exists'
        con.commit()
        data = cursor.rowcount
        cursor.close()
        if data > 0:
            return "New Genre added sucessfully"
        else:
            return "Genre not added. Some Error Occoured"
    else:
        return "Enter the name of new Genre"
    




    

@app.route('/callbook',methods=['GET','POST'])
def summarize():
    if request.method=='POST':
        url=request.form['bookurl']
        summary=summarization.getdata(url)
        return render_template('new_book.html',summary=summary)
    else:
        return render_template('new_book.html')



@app.route('/callbookform',methods=['POST','GET'])
def callbookform():
    
    
    if request.form['booktitle'] !='':
        name = request.form['booktitle']
        name1=request.form['author']
        name2=request.form['genre']
        
        if ('description' in request.form.keys()):
            summary=request.form['description']
        else:
            summary = ''
        
       
        image=request.files['file']
                   
           
        filename=secure_filename(image.filename)
        
        if 'file' in request.files:
            image=request.files['file']
            
            filename=secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        else:
            image_path=''

        
        # validate the received values
        cursor = con.cursor()
        query = "insert into books(booktitle,author,genre,description,imgname) values(%s, %s,%s,%s,%s)"
       
        val = (name,name1,name2,summary,filename)  
        
        try:
            
            cursor.execute(query,val)
            
        except Exception as e:
            return 'Error: Book'
        con.commit()
        data = cursor.rowcount
        cursor.close()
        if data > 0:
            
            return "New Book added sucessfully"
            
        else:
            return "Book not added. Some Error Occured"
    else:
        return "Enter the name of new Book"


        
@app.route('/book/<string:getbook>',methods=['POST','GET'])
def book(getbook):
    cursor=con.cursor()
    query = " SELECT * FROM ( SELECT * FROM BOOKS WHERE booktitle=\'" + getbook + "\' ) B \
	LEFT JOIN ( SELECT IFNULL(BOOKID,0) AS BOOKID,  IFNULL(ROUND(AVG(ratings),1),0) AS AVG_RATING, count(ratings) as Ratings \
          FROM COMMENTSRATING   	WHERE commentstatus='V' group by bookid) C 	ON B.BOOKID = C.BOOKID"
    cursor.execute(query)
    result=cursor.fetchall()
    books=[]
    if result:
        bookid = result[0][0]
        userid = session.get('uid')
        book1={
            'Title':result[0][1],
            'Author':result[0][2],
            'Genre':result[0][3],
            'Description':result[0][4],
            'Rating':result[0][10],
            'comment':result[0][6],
            'Image':result[0][7],
            'Average':result[0][9]

        }
        books.append(book1)
        cursor.close()

        if request.method=='POST':
            
            comment = request.form['description'].strip()
            rating=request.form['rating']
            cursor=con.cursor()
            query="Select * From commentsrating where bookid='"+str(bookid)+"' and userid='" + str(userid)+"'"
            cursor.execute(query)

            result=cursor.fetchall()
            data = cursor.rowcount
            cursor.close() 
           
            if data>0:
                cursor=con.cursor()
                query = "update commentsrating set comments='"+ comment +"',ratings='"+ str(rating) +"' ,commentstatus='P' where userid='"+ str(userid) +"' and bookid='"+ str(bookid)+"'"
                try:
                    cursor.execute(query)
                except Exception as e:
                    return 'Sorry !!Problem in Registering Rating Or Comments'     
                con.commit()
                
                data = cursor.rowcount
                flash ('Your Comment is Updated Successfully, and pending for approval','success')
                #Reduce the commentscount and ratingcount of book in books table
                cursor=con.cursor()
                query = "update books set commentcount=commentcount,ratingcount=ratingcount where bookid='"+ str(bookid)+"'"
                try:
                    cursor.execute(query)
                except Exception as e:
                    return 'Sorry !!Problem in Registering Rating Or Comments'     
                con.commit()
            # Comment check end
            else:
                cursor=con.cursor()
                query = "insert into commentsrating(userid,bookid,comments,ratings,commentstatus)  values(%s, %s,%s,%s ,%s)"
                val = (userid,bookid,comment,rating,'P')  
                try:
                    cursor.execute(query,val)
                except Exception as e:
                    return 'Sorry !!Problem in Registering Rating Or Comments'     
                con.commit()
                data = cursor.rowcount
                cursor.close() 
                flash ('Your Comment is Added Successfully, and pending for approval','success')
                

        cursor = con.cursor(dictionary=True)
        query = '''SELECT u.username, u.image_path, b.booktitle, c.comments, c.ratings
               FROM ((commentsrating c
               INNER JOIN users u ON c.userid = u.userid)
               INNER JOIN books b ON c.bookid = b.bookid)
               WHERE c.commentstatus = 'V' AND c.bookid = ''' + str(bookid)
        cursor.execute(query)
        data_list = cursor.fetchall()
        cursor.close()
        # Get Comments and Rating of the current user
        cursor = con.cursor(dictionary=True)
        query = 'select ratings,comments from COMMENTSRATING where userid='+ str(userid) +' and bookid = '+ str(bookid)
        cursor.execute(query)
        comment_list = cursor.fetchall()
        # usercomment = comment_list.comments
        cursor.close()
    return render_template('mainpage.html',title="Comments & Ratings",comment_list=comment_list, data_list = data_list, book1=book1,fname=session.get('fname'))

@app.route('/callreviewcomments',methods=['POST','GET'])
def callreviewcomments():
    if checkuser()==True:
        cursor = con.cursor(dictionary=True)
        query = ''' select u.username,b.booktitle,c.comments,c.ratings,c.commentid 
                    from (( commentsrating c 
                    inner join users u on c.userid = u.userid)
                    inner join books b on c.bookid = b.bookid)
                    where c.commentstatus = 'P';'''
        cursor.execute(query)
        data_list = cursor.fetchall()
        cursor.close()
        return render_template("review_comments.html", 
                            title="Review Comments", 
                            data_list = data_list, uname=session.get('username'))
    return redirect(url_for('login'))

@app.route('/reject/<string:id>', methods = ['POST','GET'])
def reject_comment(id):
    cursor = con.cursor(dictionary=True)
    cursor.execute("UPDATE commentsrating SET commentstatus = 'R' WHERE commentid = " + id)
    con.commit()
    cursor.close()
    flash('Comment Rejected Successfully')
    return redirect(url_for('callreviewcomments'))
 
@app.route('/show/<string:id>', methods = ['POST','GET'])
def show_comment(id):
    # To make the comment visible after approval
    cursor = con.cursor(dictionary=True)
    cursor.execute("UPDATE commentsrating SET commentstatus = 'V' WHERE commentid = " + id)
    con.commit()
    cursor.close()
    #Get book id from comment id
    cursor = con.cursor(dictionary=True)
    cursor.execute(" select bookid from commentsrating where commentid = " + id)
    result=cursor.fetchall()
    bookid=0
    for row in result:
        bookid=row['bookid']
            
        
    con.commit()
    cursor.close()
    #After approval increase in count of comment and rating of respective book
    cursor = con.cursor(dictionary=True)
    cursor.execute(" update books set commentcount=commentcount+1 , ratingcount=ratingcount+1 where bookid= " + str(bookid))
    con.commit()
    cursor.close()
    flash('Comment Approved Successfully')
    return redirect(url_for('callreviewcomments'))

@app.route('/genre/<string:getgenre>')
def genre(getgenre):
    cursor=con.cursor()
    cursor=con.cursor()
    query = '''
    SELECT *
    FROM (
        SELECT bookid, booktitle, author, genre, ratingcount, commentcount, imgname
        FROM BOOKS
        WHERE genre = %s
    ) B
    LEFT JOIN (
        SELECT IFNULL(BOOKID,0) AS BOOKID, IFNULL(ROUND(AVG(ratings),1),0) AS AVG_RATING, count(ratings) as Ratings
        FROM COMMENTSRATING
        WHERE commentstatus='V'
        GROUP BY BOOKID
    ) C
    ON B.BOOKID = C.BOOKID
'''
    
    cursor.execute(query,(getgenre,))
    result=cursor.fetchall()
    books=[]
    for row in result:
        book={
            'Title':row[1],
            'Author':row[2],
            'Genre':row[3],
            # 'Description':result[0][4],
            'Ratings':row[9],
            'Comments':row[5],
            'Image':row[6],
            'Average':row[8]
        }
        
        books.append(book)
    return render_template('genre.html',var_books1=books,fname=session.get('fname'))






        
@app.route('/author/<string:getauthor>')
def author(getauthor):
    cursor=con.cursor()
    query = '''
    SELECT *
    FROM (
        SELECT bookid, booktitle, author, genre, ratingcount, commentcount, imgname
        FROM BOOKS
        WHERE author = %s
    ) B
    LEFT JOIN (
        SELECT IFNULL(BOOKID,0) AS BOOKID, IFNULL(ROUND(AVG(ratings),1),0) AS AVG_RATING, count(ratings) as Ratings
        FROM COMMENTSRATING
        WHERE commentstatus='V'
        GROUP BY BOOKID
    ) C
    ON B.BOOKID = C.BOOKID
'''
    cursor.execute(query,(getauthor,))
    result=cursor.fetchall()
    books=[]
    for row in result:
        book={
            'Title':row[1],
            'Author':row[2],
            'Genre':row[3],
            # 'Description':result[0][4],
            'Ratings':row[9],
            'Comments':row[5],
            'Image':row[6],
            'Average':row[8]
        }
        
        books.append(book)
    return render_template('genre.html',var_books1=books,fname=session.get('fname'))

@app.route('/delete_account',methods=['GET','POST'])
def delete_account():
    
    userid=session.get('uid')
  
   
    if checkuser() == True:
        books = homepage()
        image_path = session.get('file')
        cursor=con.cursor()
        query="delete from commentsrating where userid='"+str(userid)+"'"
        cursor.execute(query)
        query="delete from users where userid='"+str(userid)+"'"
        cursor.execute(query)
        con.commit()
        cursor.close()
        flash('User deleted sucessfully','success')
        
        return render_template('registration_form.html',message=flash)
    return redirect(url_for('login'))
    

    




@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_category = request.form['search-category']
        search_term = request.form['search-term']
        cursor = con.cursor()
        if search_category == 'book-title':
            query = '''SELECT *
    FROM (
        SELECT bookid, booktitle, author, genre, imgname
        FROM BOOKS
        where booktitle LIKE %s
    ) B
    LEFT JOIN (
        SELECT IFNULL(BOOKID,0) AS BOOKID, IFNULL(ROUND(AVG(ratings),1),0) AS AVG_RATING, count(ratings) as Ratings
        FROM COMMENTSRATING
        WHERE commentstatus='V'
        GROUP BY BOOKID
    ) C
    ON B.BOOKID = C.BOOKID'''
            search_term = '%' + search_term + '%'
            cursor.execute(query, (search_term,))
        elif search_category == 'author':
            query = '''SELECT *
    FROM (
        SELECT bookid, booktitle, author, genre, imgname
        FROM BOOKS
        where author LIKE %s
    ) B
    LEFT JOIN (
        SELECT IFNULL(BOOKID,0) AS BOOKID, IFNULL(ROUND(AVG(ratings),1),0) AS AVG_RATING, count(ratings) as Ratings
        FROM COMMENTSRATING
        WHERE commentstatus='V'
        GROUP BY BOOKID
    ) C
    ON B.BOOKID = C.BOOKID'''
            search_term = '%' + search_term + '%'
            cursor.execute(query, (search_term,))
        elif search_category == 'genre':
            query = '''SELECT *
    FROM (
        SELECT bookid, booktitle, author, genre, imgname
        FROM BOOKS
        where genre LIKE %s
    ) B
    LEFT JOIN (
        SELECT IFNULL(BOOKID,0) AS BOOKID, IFNULL(ROUND(AVG(ratings),1),0) AS AVG_RATING, count(ratings) as Ratings
        FROM COMMENTSRATING
        WHERE commentstatus='V'
        GROUP BY BOOKID
    ) C
    ON B.BOOKID = C.BOOKID'''
            search_term = '%' + search_term + '%'
            cursor.execute(query, (search_term,))
        else:
            return render_template('empty.html')
        result = cursor.fetchall()
        if not result:
            return render_template('empty.html')
        books = []
        for row in result:
            book = {
                'Title': row[1],
                'Author': row[2],
                'Genre': row[3],
                'Image': row[4],
                'Average':row[6],
                'Ratings':row[7]
            }
            books.append(book)
        return render_template('basic_structure.html', var_books1=books,fname=session.get('fname'),image_path=session.get('file'))
    else:
        return render_template('basic_structure.html')

@app.route('/empty')
def empty():
    return render_template('empty.html')

@app.route('/changePassword')
def changePassword():
    render_template('change_password.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success_message = None
    error_message = None
    email_id=session.get('email')

    if request.method == 'POST':
        default_email='divyanshganotra18@gmail.com'
        email_sender = email_id
        email_password = 'tcgphhtffdmltlsi'
        email_receiver = 'dganotra_be19@thapar.edu'
      

        if not email_receiver:
            error_message = "Email Address Not Provided"
        else:
            subject = request.form['fname1']
            message='sender: '+email_sender+'\n Message: '+request.form['email1']
            username1 = session.get('fname')
            
            try:
                
                cursor = con.cursor()

                cursor.execute('INSERT INTO messages (username, subject, message) VALUES (%s, %s, %s)', (username1, subject, message))
                con.commit()
                
                cursor.close()


                em = EmailMessage()
                em['From'] ='divyanshganotra18@gmail.com'
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(message)

                context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login('divyanshganotra18@gmail.com', email_password)
                    smtp.send_message(em)

                success_message = "Email sent successfully"
                
                
                cursor = con.cursor()
                cursor.execute('SELECT username,subject,message FROM messages')
                messages = cursor.fetchall()
                cursor.close()
                

                return render_template('contact.html', fname=session.get('fname'), image_path=session.get('file'), success_message=success_message, error_message=error_message, messages=messages)

            except Exception as e:
                error_message = "An error occurred while sending the email."

    return render_template('contact.html', fname=session.get('fname'), image_path=session.get('file'), success_message=success_message, error_message=error_message)


@app.route('/admin_dashboard',methods=['GET','POST'])
def admin_dashboard():
    if request.method=='POST':
        subject=request.form['fname1']
        message=request.form['email1']
        username=session.get('fname')

        cursor=con.cursor()
        cursor.execute('insert into messages (username,subject,message) VALUES (%s, %s, %s)', (username, subject, message))
        con.commit()
        
        return redirect(url_for('admin_dashboard'))
    cursor = con.cursor()
    cursor.execute('SELECT username, subject, message FROM messages')
    messages = cursor.fetchall()
    con.commit()
    

    return render_template('admin_dashboard.html',messages=messages)
@app.route('/your_route', methods=['POST', 'GET'])
def your_route():
    if request.method == 'POST':
        search_query = request.form.get('search1')

        if not search_query:
            # Handle the case when the search query is empty
            return "Invalid search query"

        cursor = con.cursor()
        query = "SELECT bookid, booktitle, author, genre, imgname FROM books WHERE booktitle LIKE %s"
        cursor.execute(query, ('%' + search_query + '%' if search_query else '',))
        book_data = cursor.fetchall()
        con.commit()
        cursor.close()

        books = []
        for book_data in book_data:
            book = {
                'bookid': book_data[0],
                'booktitle': book_data[1],
                'author': book_data[2],
                'genre': book_data[3],
                'imgname': book_data[4],
                'imgpath': url_for('static', filename='images/' + book_data[4])
            }
            books.append(book)

        return render_template('tier_list.html', books=books)

    return render_template('tier_list.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)


    




