const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label>Number of UUIDs:</label>
        <input type="number" id="numUUIDs" value="1" min="1" max="100" style="width:100px;padding:8px;margin-bottom:16px;">
        <button onclick="generate()" class="btn btn-primary">Generate UUIDs</button>
    </div>
    <div class="output-area">
        <label for="outputText">Generated UUIDs:</label>
        <textarea id="outputText" rows="8" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
        const r = Math.random() * 16 | 0;
        const v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function generate() {
    const num = parseInt(document.getElementById('numUUIDs').value) || 1;
    const uuids = [];
    for (let i = 0; i < num; i++) {
        uuids.push(generateUUID());
    }
    document.getElementById('outputText').value = uuids.join('\n');
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        const btn = document.getElementById('copyBtn');
        btn.textContent = '✅ Copied!';
        setTimeout(() => { btn.textContent = '📋 Copy'; }, 2000);
    });
}

generate();
