const text_p = document.getElementById('speech-to-text-output');

if (!window.hasOwnProperty("webkitSpeechRecognition")) {
    alert("Unable to use the Speech Recognition API");
} else {
    console.log("Good to go.")
}

console.log(text_p)
console.log(document)
// window.SpeechRecognition = window.speechRecognition || window.webkitSpeechRecognition;

const recognition = new webkitSpeechRecognition(); // window.SpeechRecognition();
// recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = "en-US";

recognition.addEventListener('onerror', (e) => {
    console.error(e);
});

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
    window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
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