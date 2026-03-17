const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text to Repeat:</label>
        <textarea id="inputText" rows="4" placeholder="Enter text here..."></textarea>
        <label style="margin-top:12px;">Repeat Count:</label>
        <input type="number" id="repeatCount" value="3" min="1" max="1000" style="width:100px;padding:8px;">
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Repeat Text</button>
    </div>
    <div class="output-area">
        <label for="outputText">Result:</label>
        <textarea id="outputText" rows="8" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    const text = document.getElementById('inputText').value;
    const count = parseInt(document.getElementById('repeatCount').value) || 1;
    const result = Array(count).fill(text).join('\n');
    document.getElementById('outputText').value = result;
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        document.getElementById('copyBtn').textContent = '✅ Copied!';
        setTimeout(() => { document.getElementById('copyBtn').textContent = '📋 Copy'; }, 2000);
    });
}
