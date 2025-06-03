
const term = new Terminal();
term.open(document.getElementById('terminal'));
term.write('Welcome to ShellCoach\r\n$ ');

let command = '';

term.onData(data => {
    if (data.charCodeAt(0) === 13) {
        fetch('/explain', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: command })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('ai-output').innerText = data.explanation;
            term.write('\r\n$ ');
        });
        command = '';
    } else {
        command += data;
        term.write(data);
    }
});

function toggleExplanation() {
    const output = document.getElementById('ai-output');
    output.style.display = output.style.display === 'none' ? 'block' : 'none';
}


document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowUp') {
        fetch('/history')
        .then(response => response.json())
        .then(data => {
            if (data.history.length > 0) {
                const lastCommand = data.history[data.history.length - 1];
                term.write(lastCommand);
                command = lastCommand;
            }
        });
    }
});
