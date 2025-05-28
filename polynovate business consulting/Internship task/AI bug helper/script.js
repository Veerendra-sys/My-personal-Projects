document.getElementById('taskForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const code = document.getElementById('code').value;
    const error = document.getElementById('error').value;

    const response = await fetch('/add_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, error })
    });

    const data = await response.json();
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = `
        <p><strong>Task Saved!</strong></p>
        <p><strong>Explanation:</strong> ${data.explanation || 'AI not yet integrated'}</p>
    `;
});
