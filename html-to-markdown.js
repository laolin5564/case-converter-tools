const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">HTML:</label>
        <textarea id="inputText" rows="10" placeholder="Enter HTML here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Convert to Markdown</button>
    </div>
    <div class="output-area">
        <label for="outputText">Markdown:</label>
        <textarea id="outputText" rows="10" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    const input = document.getElementById('inputText').value;
    let md = input
        .replace(/<h1>(.*?)<\/h1>/gim, '# $1\n')
        .replace(/<h2>(.*?)<\/h2>/gim, '## $1\n')
        .replace(/<h3>(.*?)<\/h3>/gim, '### $1\n')
        .replace(/<strong>(.*?)<\/strong>/gim, '**$1**')
        .replace(/<em>(.*?)<\/em>/gim, '*$1*')
        .replace(/<a href=["\'](.*?)["\']>(.*?)<\/a>/gim, '[$2]($1)')
        .replace(/<br\s*\/?>/gim, '\n')
        .replace(/<[^>]+>/g, '');
    document.getElementById('outputText').value = md;
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        document.getElementById('copyBtn').textContent = '✅ Copied!';
        setTimeout(() => { document.getElementById('copyBtn').textContent = '📋 Copy'; }, 2000);
    });
}
