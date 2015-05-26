$(document).ready(function(){
    $('#tips_visible').click(function(){
        var text_visibly;
        text_visibly=document.getElementById('tips_visible').innerHTML;
        if (text_visibly=='Hide tips'){
            document.getElementById('tips_visible').innerHTML='Show tips';
            $('#tips').slideUp('slow');}
        else {
            document.getElementById('tips_visible').innerHTML='Hide tips';
            $('#tips').slideDown('slow');}
    });
                 
    
});

