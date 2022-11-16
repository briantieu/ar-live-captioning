const text_p = document.getElementById('speech-to-text-output');

console.log(text_p)
console.log(document)
window.SpeechRecognition = window.speechRecognition || window.webkitSpeechRecognition;

const recognition = new window.SpeechRecognition();
recognition.interimResults = true;

// let p = document.createElement('p');

recognition.addEventListener('result', (e) => {
    const text = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('');
    // console.log(e.results);
    // console.log(e)
    console.log(text);
    text_p.innerHTML = text;

});

recognition.addEventListener('end', () => {
    recognition.start();
})

recognition.start();

// var recognition = new webkitSpeechRecognition();
// recognition.lang = "en-GB";

// recognition.onresult = function(event) {
//     console.log(event);
//     document.getElementById('speech-to-text-output').value = event.results[0][0].transcript;
// }
// recognition.start();