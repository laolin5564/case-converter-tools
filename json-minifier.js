const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">JSON to Minify:</label>
        <textarea id="inputText" rows="10" placeholder="Paste your JSON here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="minifyJSON()" class="btn btn-primary">Minify JSON</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <label for="outputText">Minified JSON:</label>
        <textarea id="outputText" rows="6" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function minifyJSON() {
    const input = document.getElementById('inputText').value.trim();
    try {
        const parsed = JSON.parse(input);
        const minified = JSON.stringify(parsed);
        document.getElementById('outputText').value = minified;
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

function clearAll() {
    document.getElementById('inputText').value = '';
    document.getElementById('outputText').value = '';
}
