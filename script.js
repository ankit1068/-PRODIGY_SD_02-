let attempts = 0;

async function makeGuess() {
    let guessInput = document.getElementById("guessInput");
    let guess = parseInt(guessInput.value);

    if (!guess || guess < 1 || guess > 100) {
        alert("Please enter a number between 1 and 100.");
        return;
    }

    attempts++;

    let response = await fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guess: guess })
    });

    let data = await response.json();
    document.getElementById("message").innerText = data.message;
    document.getElementById("attempts").innerText = `Attempts: ${attempts}`;

    if (data.correct) {
        guessInput.disabled = true;
    }
}
