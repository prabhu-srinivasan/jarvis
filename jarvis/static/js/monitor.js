var recognition = new webkitSpeechRecognition();

recognition.lang = "en-IN";
recognition.continuous = true;
recognition.interimResults = true;
recognition.onresult = function(e){
  process(e.results);
};
recognition.onerror = function(e){
  console.error(e);
  window.location.reload();
};
recognition.onend = function(e){
  recognition.start();
};
recognition.start();

function process(results){
  // console.log(results);
  transcript = $.trim(results[results.length - 1][0].transcript);
  $("#translated-text").html(transcript);
  $.post('/apis/monitor', {'text': transcript}).done(function(data){
    data = JSON.parse(data);
    $("#emotion").html(data.emotion);

    // crack joke if sad
    if(data.emotion == 'Sadness'){
      crackjoke(data.joke);
    }

    // take photo if happy
    if(data.emotion == 'Joy'){
      takephoto();
    }
  });
}


function crackjoke(joke){
  console.log('Joke');
  var msg = new SpeechSynthesisUtterance('Yo man. You seems like sad. Listen this');
  window.speechSynthesis.speak(msg);
  var joke = new SpeechSynthesisUtterance(joke);
  window.speechSynthesis.speak(joke);
}


function takephoto(){
  console.log('Take photo !!!');
}
