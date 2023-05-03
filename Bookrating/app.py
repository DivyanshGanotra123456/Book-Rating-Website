from flask import Flask, render_template, json, request,redirect, url_for, jsonify,session,g
# from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import summarization
import os
from werkzeug.utils import secure_filename
import base64

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
            query="SELECT booktitle, author, genre, imgname FROM books LIMIT 10"

            cursor.execute(query)
            
            result=cursor.fetchall()
            books=[]
            print('Result is here:', result)
            for row in result:
                book={
                    'Title':row[0],
                    'Author':row[1],
                    'Genre':row[2],
                    'Image':row[3]
                }
                print('Book is here:', book)
                books.append(book)
            return render_template('basic_structure.html',var_books1=books)
    return redirect(url_for('login'))





@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

def homepage():
    cursor=con.cursor()
    query="SELECT booktitle, author, genre, imgname FROM books LIMIT 10"
    cursor.execute(query)
    result=cursor.fetchall()
    books=[]
    for row in result:
        book={
            'Title':row[0],
            'Author':row[1],
            'Genre':row[2],
            'Image':row[3]
        }
        books.append(book)
    return books


@app.route('/callhomepage',methods=['POST','GET'])
def callhomepage():
    
    if checkuser() == True:
        books = homepage()
        image_path = session.get('file')
        print('Image path is here:', image_path)
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
        if data>0:
            session['fname']=fname
            session['uid']=uid
            session['file']=image_path
            
            return redirect(url_for('callhomepage'))
        else:
            message='Invalid Username/Password'
            return render_template("login.html",message=message)
    else:
        return render_template('login.html')


@app.route('/changepassword',methods=['POST','GET'])
def changepassword():
    print('11')
    if request.method=='POST':
        print('1')
        if request.form['password_old'] !='' or request.form['password_new'] !='' or request.form['confirm-password'] !='':
            print('2')
            if request.form['password_new'] == request.form['confirm-password']:
                password_old=request.form['password_old']
                password_new=request.form['password_new']
                fname = session.get('fname')
                print('Username:'+fname)
                cursor=con.cursor(dictionary=True)
                query="select * from users where username='"+fname+"' and password='"+password_old+"'"
                try:
                    cursor.execute(query)
                except:
                    message='Invalid Old Password'
                    render_template('change_password.html',message=message)
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
                    print(query)
                    cursor.execute(query)
                    con.commit()
                    cursor.close()
                    message='Password Updated sucessfully'
                    return render_template("change_password.html",message=message)
                else:
                    message='Old Password does Not match with the original password'
                    return render_template("change_password.html",message=message)
            else:
                message='New Password and Confirm Password does not match'
                return render_template('change_password.html',message=message)
        else:
            print('old and new password not match')
            message='Please Enter Old Password, New Password and Confirm Password'
            render_template('change_password.html',message=message)
    else:
        return render_template('change_password.html')
    return render_template('change_password.html')


@app.route('/changepassword1',methods=['POST','GET'])
def changepassword1():
    print('22')
    if request.method=='POST':
        print('1')
        if request.form['password_old'] !='' or request.form['password_new'] !='' or request.form['confirm-password'] !='':
            print('2')
            if request.form['password_new'] == request.form['confirm-password']:
                password_old=request.form['password_old']
                password_new=request.form['password_new']
                fname = session.get('fname')
                print('Username:'+fname)
                cursor=con.cursor(dictionary=True)
                query="select * from users where username='"+fname+"' and password='"+password_old+"'"
                try:
                    cursor.execute(query)
                except:
                    message='Invalid Old Password'
                    render_template('basic_structure.html',message=message)
                records=cursor.fetchall()
                data=cursor.rowcount
                print('data')
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
                    print(query)
                    con.commit()
                    print(1)
                    cursor.close()
                    print(2)
                    message='Password Updated sucessfully'
                    print(message)
                    books = homepage()
                    print(books)
                    return render_template('basic_structure.html',var_books1=books, title='Home Page',fname=session.get('fname'))
                    # return render_template("basic_structure.html",message=message)
                else:
                    message='Old Password does Not match with the original password'
                    return render_template("basic_structure.html",message=message)
            else:
                message='New Password and Confirm Password does not match'
                return render_template('basic_structure.html',message=message)
        else:
            print('old and new password not match')
            message='Please Enter Old Password, New Password and Confirm Password'
            render_template('basic_structure.html',message=message)
    else:
        return render_template('login.html')
    return render_template('login.html')










@app.route('/callregister')
def callregistration():
    return render_template('registration_form.html')

@app.route('/callregisterform',methods=['POST','GET'])
def callregistrationform():
    print('Request form keys:', request.form.keys())
    if request.form['fname'] !='':
        print('Inside if request form:')
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
    

@app.route('/calllogin')
def calllogin():
    return render_template('login.html')

@app.route('/callloginform')
def callloginform():
    username=request.form['fname']
    password=request.form['password']
    remember_me=request.form['hobby']

    print(username)
    print(password)
    print(remember_me)
    return json.dumps({'Status':'OK'});

@app.route('/callgenre')
def callgenre():
    return render_template('add_genre.html')

# @app.route('/ratings')
# def ratings():


@app.route('/callgenreform',methods=['POST'])
def callgenreform():
    if request.form['fname'] !='':
        _name = request.form['fname']
        # validate the received values
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
    


# @app.route('/callbook')
# def callbook():
    

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
    print('Request Form is here:', request.form.keys())
    # data=request.get_json()
    print('in callbookform', )
    
    if request.form['booktitle'] !='':
        print('booktitle ' + request.form['booktitle'] )
        name = request.form['booktitle']
        name1=request.form['author']
        name2=request.form['genre']
        
        if ('description' in request.form.keys()):
            summary=request.form['description']
        else:
            summary = ''
        print(name)
        print(name1)
        print(name2)
        print(summary)
        
        # return
        #Get The image file
        print(UPLOAD_FOLDER)
        #image = request.files('file')
        image=request.files['file']
                   
           
        filename=secure_filename(image.filename)
        print(filename)
        
        if 'file' in request.files:
            image=request.files['file']
            
            print(request.files)
            filename=secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        #image path in the database
            #image_path = os.path.join(UPLOAD_FOLDER,filename)
        else:
            image_path=''
            print('No image uploaded')

        
        # validate the received values
        cursor = con.cursor()
        query = "insert into books(booktitle,author,genre,description,imgname) values(%s, %s,%s,%s,%s)"
       
        val = (name,name1,name2,summary,filename)  
        print(val)  
        
        try:
            
            cursor.execute(query,val)
            
        except Exception as e:
            print(e)
            return 'Error: Book'
        con.commit()
        data = cursor.rowcount
        cursor.close()
        if data > 0:
            
            return "New Book added sucessfully"
            
        else:
            return "Book not added. Some Error Occured"
    else:
        print ('No Book Title')
        return "Enter the name of new Book"


        
@app.route('/book/<string:getbook>')
def book(getbook):
    cursor=con.cursor()
    # print(getbook)
    query="Select booktitle,author,genre,imgname,description From books where booktitle='"+getbook+"'"
    cursor.execute(query)

    result=cursor.fetchall()
    books=[]
    print("Result is here:",result)
 
    book1={
        'Title':result[0][0],
        'Author':result[0][1],
        'Genre':result[0][2],
        'Image':result[0][3],
        'Description':result[0][4]
    }
    print('Book is here',book1)
    books.append(book1)
    print('All the books are here:', books)
    return render_template('mainpage.html', book1=book1,fname=session.get('fname'))



@app.route('/genre/<string:getgenre>')
def genre(getgenre):
    cursor=con.cursor()
    query="SELECT booktitle, author, genre, imgname FROM books where genre='"+ getgenre +"' LIMIT 10"

    cursor.execute(query)
    
    result=cursor.fetchall()
    books=[]
    print('Result is here:', result)
    for row in result:
        book={
            'Title':row[0],
            'Author':row[1],
            'Genre':row[2],
            'Image':row[3]
        }
        print('Book is here:', book)
        books.append(book)
    return render_template('genre.html',var_books1=books,fname=session.get('fname'))

@app.route('/author/<string:getauthor>')
def author(getauthor):
    cursor=con.cursor()
    query="Select booktitle,author,genre,imgname From books where author='"+getauthor+"'LIMIT 10"
    cursor.execute(query)

    result=cursor.fetchall()
    books=[]
    print("Result is here:",result)
    for row in result:
        book={
            'Title':row[0],
            'Author':row[1],
            'Genre':row[2],
            'Image':row[3]
        }
        print('Book is here',book)
        books.append(book)
    return render_template('author.html',var_books1=books,fname=session.get('fname'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_category = request.form['search-category']
        search_term = request.form['search-term']
        cursor = con.cursor()
        if search_category == 'book-title':
            query = "SELECT booktitle, author, genre, imgname FROM books WHERE booktitle LIKE %s"
            search_term = '%' + search_term + '%'
            cursor.execute(query, (search_term,))
        elif search_category == 'author':
            query = "SELECT booktitle, author, genre, imgname FROM books WHERE author LIKE %s"
            search_term = '%' + search_term + '%'
            cursor.execute(query, (search_term,))
        elif search_category == 'genre':
            query = "SELECT booktitle, author, genre, imgname FROM books WHERE genre LIKE %s"
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
                'Title': row[0],
                'Author': row[1],
                'Genre': row[2],
                'Image': row[3]
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

        
        


@app.route('/callsetting')
def callsetting():
    return render_template('settings.html')
@app.route('/helo')
def callhelp():
    return render_template('help_and_support.html')



@app.route('/addautho1111r',methods=['POST','GET'])
def addauthor():
    print("1")
    try:
        print('2')
        if request.method =='POST':
            if request.form['fname'] !='':
                _name = request.form['fname']

                print (_name )
                # validate the received values
                if _name :
                    conn = mysql.connect()
                    cursor = conn.cursor()
                    cursor.execute('insert into authors values('+ _name +')')
                    data = cursor.fetchall()

                    if len(data) == 0:
                        conn.commit()
                        cursor.close() 
                        conn.close()
                        return json.dumps({'message':'User created successfully !'})
                    else:
                        return json.dumps({'error':str(data[0])})
                else:
                    return json.dumps({'html':'<span>Enter the required fields</span>'})
        
        return render_template("/templates/addauthor.html")

    except Exception as e:
        return json.dumps({'error':str(e)})


if __name__ == "__main__":
    app.run(port=5000)