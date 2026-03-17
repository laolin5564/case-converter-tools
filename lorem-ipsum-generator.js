const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label>Number of Paragraphs:</label>
        <input type="number" id="numParagraphs" value="3" min="1" max="50" style="width:100px;padding:8px;margin-bottom:16px;">
        <button onclick="generate()" class="btn btn-primary">Generate Lorem Ipsum</button>
    </div>
    <div class="output-area">
        <label for="outputText">Result:</label>
        <textarea id="outputText" rows="10" readonly placeholder="Generated text will appear here..."></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy to Clipboard</button>
    </div>
`;

function generate() {
    const num = parseInt(document.getElementById('numParagraphs').value) || 3;
    const paragraphs = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.",
        "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti."
    ];
    const result = [];
    for (let i = 0; i < num; i++) {
        result.push(paragraphs[i % paragraphs.length]);
    }
    document.getElementById('outputText').value = result.join('\n\n');
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        const btn = document.getElementById('copyBtn');
        btn.textContent = '✅ Copied!';
        setTimeout(() => { btn.textContent = '📋 Copy to Clipboard'; }, 2000);
    });
}

generate();
