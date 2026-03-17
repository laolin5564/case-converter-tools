const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">JSON to Format:</label>
        <textarea id="inputText" rows="10" placeholder="Paste your JSON here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="formatJSON()" class="btn btn-primary">Format & Validate</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <div id="validationStatus"></div>
        <label for="outputText">Formatted JSON:</label>
        <textarea id="outputText" rows="10" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function formatJSON() {
    const input = document.getElementById('inputText').value.trim();
    const status = document.getElementById('validationStatus');
    try {
        const parsed = JSON.parse(input);
        const formatted = JSON.stringify(parsed, null, 2);
        document.getElementById('outputText').value = formatted;
        status.innerHTML = '<span style="color:green;">✅ Valid JSON</span>';
    } catch(e) {
        document.getElementById('outputText').value = '';
        status.innerHTML = `<span style="color:red;">❌ Invalid JSON: ${e.message}</span>`;
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
    document.getElementById('validationStatus').innerHTML = '';
}
