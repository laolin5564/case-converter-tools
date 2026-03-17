const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Hexadecimal:</label>
        <textarea id="inputText" rows="8" placeholder="Enter text here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Convert to Text</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <label for="outputText">Text:</label>
        <textarea id="outputText" rows="8" readonly placeholder="Result will appear here..."></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    try {
        const input = document.getElementById('inputText').value;
        const hex = input.replace(/\s/g, '').match(/.{1,2}/g) || [];
        const text = hex.map(h => String.fromCharCode(parseInt(h, 16))).join('');
        document.getElementById('outputText').value = text;
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid hex input';
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
