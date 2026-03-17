const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text to Reverse:</label>
        <textarea id="inputText" rows="8" placeholder="Enter text here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Reverse Text</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <label for="outputText">Reversed Text:</label>
        <textarea id="outputText" rows="8" readonly placeholder="Result will appear here..."></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    const input = document.getElementById('inputText').value;
    const reversed = input.split('').reverse().join('');
    document.getElementById('outputText').value = reversed;
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
