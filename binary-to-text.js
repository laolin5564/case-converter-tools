const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Binary:</label>
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
        const binary = input.replace(/\s/g, '').match(/.{1,8}/g) || [];
        const text = binary.map(bin => String.fromCharCode(parseInt(bin, 2))).join('');
        document.getElementById('outputText').value = text;
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid binary input';
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
