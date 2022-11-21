const sendPost = async (content) => {
    const response = await fetch("/post", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'content': content
        })
    })

    if (response.ok) {
        return response
    }
}

const text_p = document.getElementById('speech-to-text-output');

if (!window.hasOwnProperty("webkitSpeechRecognition")) {
    alert("Unable to use the Speech Recognition API");
} else {
    console.log("Good to go.")
}

// window.SpeechRecognition = window.speechRecognition || window.webkitSpeechRecognition;

const recognition = new webkitSpeechRecognition(); // window.SpeechRecognition();
// recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = "en-US";

recognition.addEventListener('onerror', (e) => {
    console.error(e);
});

recognition.addEventListener('result', (e) => {
    const text = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('');
    console.log(text);
    sendPost(text)
    text_p.innerHTML = text
    ;
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