const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
        <div>
            <label for="text1">Text 1:</label>
            <textarea id="text1" rows="10" placeholder="Enter first text..."></textarea>
        </div>
        <div>
            <label for="text2">Text 2:</label>
            <textarea id="text2" rows="10" placeholder="Enter second text..."></textarea>
        </div>
    </div>
    <div class="buttons-grid" style="margin-top:16px;">
        <button onclick="compare()" class="btn btn-primary">Compare</button>
    </div>
    <div class="output-area" style="margin-top:16px;">
        <div id="diffResult"></div>
    </div>
`;

function compare() {
    const text1 = document.getElementById('text1').value.split('\n');
    const text2 = document.getElementById('text2').value.split('\n');
    const result = document.getElementById('diffResult');
    let html = '<h3>Differences:</h3><div style="font-family:monospace;font-size:0.9rem;">';
    const maxLen = Math.max(text1.length, text2.length);
    let diffCount = 0;
    for (let i = 0; i < maxLen; i++) {
        if (text1[i] !== text2[i]) {
            diffCount++;
            html += `<div style="background:#ffe0e0;padding:4px;margin:2px 0;">Line ${i+1} differs</div>`;
            if (text1[i]) html += `<div style="color:red;padding-left:20px;">- ${text1[i]}</div>`;
            if (text2[i]) html += `<div style="color:green;padding-left:20px;">+ ${text2[i]}</div>`;
        }
    }
    if (diffCount === 0) {
        html = '<h3 style="color:green;">✅ Texts are identical!</h3>';
    } else {
        html = `<h3>${diffCount} difference(s) found:</h3>` + html;
    }
    html += '</div>';
    result.innerHTML = html;
}
