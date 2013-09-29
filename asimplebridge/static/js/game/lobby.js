var socket = new io.Socket();
socket.connect();
console.log(socket);
socket.on('connect', function() {
    socket.subscribe('room-1');
});
$('#messageTest').click(function(){
  var request = {
    action: 'add',
    option: 1,
    message: 'test for jason'
  };
  socket.send(JSON.stringify(request));
});
$('#sendBtn').click(function(e){
  e.preventDefault();
  var data = {
    action: 'chat',
    author: e.target.dataset.username,
    message: $('#typeIn').val(),
  };
  socket.send(JSON.stringify(data));
});
socket.on('message', function(message){
  var jsonResponse = JSON.parse(message);
  if(jsonResponse.action == 'chat')
    $('.log').append("<li>"+ jsonResponse.author +": "+ jsonResponse.message + "</li>");
});