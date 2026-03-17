const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text:</label>
        <textarea id="inputText" rows="8" placeholder="Enter text here..."></textarea>
        <label style="margin-top:12px;">Find:</label>
        <input type="text" id="findText" placeholder="Text to find" style="width:100%;padding:8px;margin-bottom:8px;">
        <label>Replace with:</label>
        <input type="text" id="replaceText" placeholder="Replacement text" style="width:100%;padding:8px;margin-bottom:8px;">
        <label><input type="checkbox" id="caseSensitive"> Case sensitive</label>
    </div>
    <div class="buttons-grid">
        <button onclick="replace()" class="btn btn-primary">Find & Replace</button>
    </div>
    <div class="output-area">
        <label for="outputText">Result:</label>
        <textarea id="outputText" rows="8" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function replace() {
    const input = document.getElementById('inputText').value;
    const find = document.getElementById('findText').value;
    const replaceWith = document.getElementById('replaceText').value;
    const caseSensitive = document.getElementById('caseSensitive').checked;
    const flags = caseSensitive ? 'g' : 'gi';
    const regex = new RegExp(find.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), flags);
    const result = input.replace(regex, replaceWith);
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
