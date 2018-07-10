$('#suggestion').keyup(function(){
var query;
query = $(this).val();
$.get('/suggest/', {suggestion: query}, function(data){
$('#prod').html(data);
});
});