async function checkAnswer() {
    const answer = document.getElementById('answer').value;
    const response = await fetch('/check_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answer: parseInt(answer), user_id: 1 }),
    });
    const result = await response.json();
    document.getElementById('message').innerText = result.message;
    if (result.status === 'correct') {
        updateTucoins();
    }
}

async function updateTucoins() {
    const response = await fetch('/get_tucoins', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: 1 }),
    });
    const result = await response.json();
    document.getElementById('tucoins').innerText = `Tucoins: ${result.tucoins}`;
}

async function buyHouse(house_id) {
    const response = await fetch('/buy_house', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ house_id: house_id, user_id: 1 }),
    });
    const result = await response.json();
    alert(result.message);
    if (result.status === 'success') {
        updateTucoins();
    }
}

window.onload = updateTucoins;
