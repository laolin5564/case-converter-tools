const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label>String Length:</label>
        <input type="number" id="length" value="16" min="1" max="1000" style="width:100px;padding:8px;margin-bottom:8px;"><br>
        <label><input type="checkbox" id="useUpper" checked> Uppercase (A-Z)</label><br>
        <label><input type="checkbox" id="useLower" checked> Lowercase (a-z)</label><br>
        <label><input type="checkbox" id="useNumbers" checked> Numbers (0-9)</label><br>
        <label><input type="checkbox" id="useSpecial"> Special Characters</label><br>
        <button onclick="generate()" class="btn btn-primary" style="margin-top:12px;">Generate Random String</button>
    </div>
    <div class="output-area">
        <label for="outputText">Generated String:</label>
        <textarea id="outputText" rows="4" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function generate() {
    const length = parseInt(document.getElementById('length').value) || 16;
    let chars = '';
    if (document.getElementById('useUpper').checked) chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (document.getElementById('useLower').checked) chars += 'abcdefghijklmnopqrstuvwxyz';
    if (document.getElementById('useNumbers').checked) chars += '0123456789';
    if (document.getElementById('useSpecial').checked) chars += '!@#$%^&*()_+-=[]{}|;:,.<>?';
    if (!chars) chars = 'abcdefghijklmnopqrstuvwxyz';
    let result = '';
    for (let i = 0; i < length; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    document.getElementById('outputText').value = result;
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
