$(function(){
    var bookTitles=[];
    $('#register').submit(function(event){
        event.preventDefault();
        var bookTitle=$('#book-title').val();
        var authorName=$('#author-name').val();
        var genre=$('#genre').val();
        var bookimage=$('#img')[0].files[0];
        var summary=$('#description').val();
        

        if(bookTitle==''){

            alert('Please enter the book title.');
            return;
        }
        if(authorName=='')
        {
            alert('Please enter an author name.')
            return;
        }
        if(genre=='')
        {
            alert('Please enter a genre');
            return;
        }
        if(bookTitles.includes(bookTitle))
        {
            alert('This book already exists');
            return;
        }
        bookTitles.push(bookTitle);
        var formdata=new FormData();
        formdata.append('booktitle',bookTitle);
        formdata.append('author',authorName);
        formdata.append('genre',genre);
        formdata.append('description',summary);
        formdata.append('file',bookimage);
        


        console.log(bookTitle);
        
        console.log($('#register').serialize());
        $.ajax({
            type:'POST',
            url:'/callbookform',
            data:formdata,
            contentType:false,
            processData:false,

            
           
            
                
            
            success:function(response){
                $("#msg").html(response);
                alert('Book added successfully');
            },
            error:function(){
                
                alert('Failed to add book');
            }

        });

        $('#book-title').val('');
        $('#author-name').val('');
        $('#genre').val('');
        $('#img').val('');
        $('#description').val('');

    });
});