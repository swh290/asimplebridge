$(document).ready(function(){
  var socket = io.connect('localhost', {port: 4000});
  
  socket.on('connect', function(){
    console.log("connect");
  });
  
  var entry_el = $('.log');
           
  socket.on('message', function(message) {
    //Append message to the bottom of the list
    $('.log').append('<li>' + message + '</li>').animate({ scrollTop: $('.log > li').length * 20}, 100);
  });
      
  $('#sendBtn').click(function(e){
    e.preventDefault();
    var value = $('#typeIn').val();
    if(value){
      var data = {
        action: 'chat',
        author: e.target.dataset.username,
        message: value,
      };
      $('#typeIn').val('');
      socket.emit('send_message', JSON.stringify(data), function(data){
        console.log(data);
      });
    }
  });           
});