var socket = new io.Socket();
socket.connect("http://asimplebridge.herokuapp.com:9000/");
socket.on('connect', function() {
    socket.subscribe('lobby');
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
    socket.send(JSON.stringify(data));
  }
});
socket.on('message', function(message){
  var jsonResponse = JSON.parse(message);
  if(jsonResponse.action == 'chat')
    $('.log').append("<li>"+ jsonResponse.author +": "+ jsonResponse.message + "</li>").animate({ scrollTop: $('.log > li').length * 20}, 100);
});