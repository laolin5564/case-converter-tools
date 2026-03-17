const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">JSON Array:</label>
        <textarea id="inputText" rows="10" placeholder="Enter JSON array here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Convert to CSV</button>
    </div>
    <div class="output-area">
        <label for="outputText">CSV:</label>
        <textarea id="outputText" rows="10" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    try {
        const input = document.getElementById('inputText').value.trim();
        const data = JSON.parse(input);
        if (!Array.isArray(data) || data.length === 0) {
            document.getElementById('outputText').value = 'Error: Input must be a non-empty JSON array';
            return;
        }
        const headers = Object.keys(data[0]);
        const csv = [headers.join(',')];
        data.forEach(row => {
            csv.push(headers.map(h => row[h] || '').join(','));
        });
        document.getElementById('outputText').value = csv.join('\n');
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid JSON';
    }
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        document.getElementById('copyBtn').textContent = '✅ Copied!';
        setTimeout(() => { document.getElementById('copyBtn').textContent = '📋 Copy'; }, 2000);
    });
}
