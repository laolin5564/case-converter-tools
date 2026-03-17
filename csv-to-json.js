const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">CSV Data:</label>
        <textarea id="inputText" rows="10" placeholder="Enter CSV here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Convert to JSON</button>
    </div>
    <div class="output-area">
        <label for="outputText">JSON:</label>
        <textarea id="outputText" rows="10" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    const input = document.getElementById('inputText').value.trim();
    const lines = input.split('\n');
    if (lines.length < 2) {
        document.getElementById('outputText').value = 'Error: Need at least header and one data row';
        return;
    }
    const headers = lines[0].split(',').map(h => h.trim());
    const result = [];
    for (let i = 1; i < lines.length; i++) {
        const values = lines[i].split(',').map(v => v.trim());
        const obj = {};
        headers.forEach((header, index) => {
            obj[header] = values[index] || '';
        });
        result.push(obj);
    }
    document.getElementById('outputText').value = JSON.stringify(result, null, 2);
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        document.getElementById('copyBtn').textContent = '✅ Copied!';
        setTimeout(() => { document.getElementById('copyBtn').textContent = '📋 Copy'; }, 2000);
    });
}
