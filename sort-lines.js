const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text to Sort:</label>
        <textarea id="inputText" rows="8" placeholder="Enter text here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="sortAsc()" class="btn btn-primary">Sort A-Z</button>
        <button onclick="sortDesc()" class="btn btn-secondary">Sort Z-A</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <label for="outputText">Sorted Text:</label>
        <textarea id="outputText" rows="8" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function sortAsc() {
    const input = document.getElementById('inputText').value;
    const lines = input.split('\n').sort();
    document.getElementById('outputText').value = lines.join('\n');
}

function sortDesc() {
    const input = document.getElementById('inputText').value;
    const lines = input.split('\n').sort().reverse();
    document.getElementById('outputText').value = lines.join('\n');
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
