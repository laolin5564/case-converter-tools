const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label>Regular Expression:</label>
        <input type="text" id="regexInput" placeholder="Enter regex pattern" style="width:100%;padding:8px;margin-bottom:8px;">
        <label><input type="checkbox" id="flagG" checked> g (global)</label>
        <label><input type="checkbox" id="flagI"> i (case insensitive)</label>
        <label><input type="checkbox" id="flagM"> m (multiline)</label>
    </div>
    <div class="input-area">
        <label>Test String:</label>
        <textarea id="testString" rows="6" placeholder="Enter text to test..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="testRegex()" class="btn btn-primary">Test Regex</button>
    </div>
    <div class="output-area">
        <div id="result"></div>
    </div>
`;

function testRegex() {
    const pattern = document.getElementById('regexInput').value;
    const testStr = document.getElementById('testString').value;
    const result = document.getElementById('result');
    
    if (!pattern) {
        result.innerHTML = '<span style="color:red;">Please enter a regex pattern</span>';
        return;
    }
    
    try {
        let flags = '';
        if (document.getElementById('flagG').checked) flags += 'g';
        if (document.getElementById('flagI').checked) flags += 'i';
        if (document.getElementById('flagM').checked) flags += 'm';
        
        const regex = new RegExp(pattern, flags);
        const matches = [...testStr.matchAll(regex)];
        
        if (matches.length > 0) {
            let html = `<h3 style="color:green;">✅ ${matches.length} match(es) found:</h3><div style="font-family:monospace;">`;
            matches.forEach((match, i) => {
                html += `<div style="background:#e0ffe0;padding:8px;margin:4px 0;border-radius:4px;">Match ${i+1}: "${match[0]}"</div>`;
            });
            html += '</div>';
            result.innerHTML = html;
        } else {
            result.innerHTML = '<h3 style="color:orange;">⚠️ No matches found</h3>';
        }
    } catch(e) {
        result.innerHTML = `<span style="color:red;">❌ Invalid regex: ${e.message}</span>`;
    }
}
