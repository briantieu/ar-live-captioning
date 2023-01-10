// POST to flask
const postTranslateAndStore = async (content) => {
    const response = await fetch('/translate_and_store', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'content': content
        })
    })
}

// alert if browser is unable to use speech recognition
if (!window.hasOwnProperty("webkitSpeechRecognition")) {
    alert("Unable to use the Speech Recognition API");
}

// window.SpeechRecognition = window.speechRecognition || window.webkitSpeechRecognition;
const recognition = new webkitSpeechRecognition(); // window.SpeechRecognition();
// recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = 'en-US'; // es-MX

// log error if necessary
recognition.addEventListener('onerror', (e) => {
    console.error(e);
});

// upon getting a recognition result
recognition.addEventListener('result', (e) => {
    const text = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('');

    // translate, store, and display it
    postTranslateAndStore(text);
    document.getElementById('speech-to-text-output').innerHTML = text;
    window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
});

// continually start up if speech recognition ends
recognition.addEventListener('end', () => {
    recognition.start();
})

recognition.start();