$(document).ready(function(){
    $('#search-btn').click(function(){
        var category=$('#search-category').val();
        var term=$('#search-term').val();
        $.ajax({
            url:'/search',
            method:'POST',
            data:{
                'search-category':category,
                'search-term':term

            },
            success:function(data){

            },
            error:function(error)
            {
                alert('error');
            }



        });
    });
});