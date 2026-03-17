#!/usr/bin/env python3

# 剩余工具的JS代码
remaining_tools = {
    "json-formatter": '''const toolSection = document.getElementById('toolSection');
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
''',

    "json-minifier": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">JSON to Minify:</label>
        <textarea id="inputText" rows="10" placeholder="Paste your JSON here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="minifyJSON()" class="btn btn-primary">Minify JSON</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <label for="outputText">Minified JSON:</label>
        <textarea id="outputText" rows="6" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function minifyJSON() {
    const input = document.getElementById('inputText').value.trim();
    try {
        const parsed = JSON.parse(input);
        const minified = JSON.stringify(parsed);
        document.getElementById('outputText').value = minified;
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid JSON';
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
}
''',

    "markdown-to-html": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Markdown:</label>
        <textarea id="inputText" rows="10" placeholder="Enter Markdown here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Convert to HTML</button>
    </div>
    <div class="output-area">
        <label for="outputText">HTML:</label>
        <textarea id="outputText" rows="10" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    const input = document.getElementById('inputText').value;
    let html = input
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        .replace(/\\*\\*(.*)\\*\\*/gim, '<strong>$1</strong>')
        .replace(/\\*(.*)\\*/gim, '<em>$1</em>')
        .replace(/\\[(.*?)\\]\\((.*?)\\)/gim, "<a href='$2'>$1</a>")
        .replace(/\\n$/gim, '<br>');
    document.getElementById('outputText').value = html;
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        document.getElementById('copyBtn').textContent = '✅ Copied!';
        setTimeout(() => { document.getElementById('copyBtn').textContent = '📋 Copy'; }, 2000);
    });
}
''',

    "html-to-markdown": '''const toolSection = document.getElementById('toolSection');
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
        .replace(/<h1>(.*?)<\\/h1>/gim, '# $1\\n')
        .replace(/<h2>(.*?)<\\/h2>/gim, '## $1\\n')
        .replace(/<h3>(.*?)<\\/h3>/gim, '### $1\\n')
        .replace(/<strong>(.*?)<\\/strong>/gim, '**$1**')
        .replace(/<em>(.*?)<\\/em>/gim, '*$1*')
        .replace(/<a href=["\\'](.*?)["\\']>(.*?)<\\/a>/gim, '[$2]($1)')
        .replace(/<br\\s*\\/?>/gim, '\\n')
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
''',

    "csv-to-json": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">CSV Data:</label>
        <textarea id="inputText" rows="10" placeholder="Enter CSV here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Convert to JSON</button>
    </div>
    <div class="output-area">
        <label for="outputText">JSON:</label>
        <textarea id="outputText" rows="10" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    const input = document.getElementById('inputText').value.trim();
    const lines = input.split('\\n');
    if (lines.length < 2) {
        document.getElementById('outputText').value = 'Error: Need at least header and one data row';
        return;
    }
    const headers = lines[0].split(',').map(h => h.trim());
    const result = [];
    for (let i = 1; i < lines.length; i++) {
        const values = lines[i].split(',').map(v => v.trim());
        const obj = {};
        headers.forEach((header, index) => {
            obj[header] = values[index] || '';
        });
        result.push(obj);
    }
    document.getElementById('outputText').value = JSON.stringify(result, null, 2);
}

function copyOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {
        document.getElementById('copyBtn').textContent = '✅ Copied!';
        setTimeout(() => { document.getElementById('copyBtn').textContent = '📋 Copy'; }, 2000);
    });
}
''',

    "json-to-csv": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">JSON Array:</label>
        <textarea id="inputText" rows="10" placeholder="Enter JSON array here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">Convert to CSV</button>
    </div>
    <div class="output-area">
        <label for="outputText">CSV:</label>
        <textarea id="outputText" rows="10" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function convert() {
    try {
        const input = document.getElementById('inputText').value.trim();
        const data = JSON.parse(input);
        if (!Array.isArray(data) || data.length === 0) {
            document.getElementById('outputText').value = 'Error: Input must be a non-empty JSON array';
            return;
        }
        const headers = Object.keys(data[0]);
        const csv = [headers.join(',')];
        data.forEach(row => {
            csv.push(headers.map(h => row[h] || '').join(','));
        });
        document.getElementById('outputText').value = csv.join('\\n');
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid JSON';
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
''',

    "diff-checker": '''const toolSection = document.getElementById('toolSection');
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
    const text1 = document.getElementById('text1').value.split('\\n');
    const text2 = document.getElementById('text2').value.split('\\n');
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
''',

    "find-and-replace": '''const toolSection = document.getElementById('toolSection');
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
    const regex = new RegExp(find.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'), flags);
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
''',

    "text-to-speech": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text to Speak:</label>
        <textarea id="inputText" rows="6" placeholder="Enter text here..."></textarea>
        <label style="margin-top:12px;">Voice:</label>
        <select id="voiceSelect" style="width:100%;padding:8px;margin-bottom:8px;"></select>
        <label>Speed: <span id="rateValue">1.0</span>x</label>
        <input type="range" id="rate" min="0.5" max="2" step="0.1" value="1" style="width:100%;" oninput="document.getElementById('rateValue').textContent = this.value">
    </div>
    <div class="buttons-grid">
        <button onclick="speak()" class="btn btn-primary">▶️ Speak</button>
        <button onclick="stop()" class="btn btn-secondary">⏹️ Stop</button>
    </div>
`;

let voices = [];
function loadVoices() {
    voices = speechSynthesis.getVoices();
    const select = document.getElementById('voiceSelect');
    select.innerHTML = voices.map((v, i) => 
        `<option value="${i}">${v.name} (${v.lang})</option>`
    ).join('');
}

speechSynthesis.onvoiceschanged = loadVoices;
loadVoices();

function speak() {
    const text = document.getElementById('inputText').value;
    if (!text) return;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.voice = voices[document.getElementById('voiceSelect').value];
    utterance.rate = parseFloat(document.getElementById('rate').value);
    speechSynthesis.speak(utterance);
}

function stop() {
    speechSynthesis.cancel();
}
''',

    "qr-code-generator": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text or URL:</label>
        <textarea id="inputText" rows="4" placeholder="Enter text or URL..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="generate()" class="btn btn-primary">Generate QR Code</button>
    </div>
    <div class="output-area" style="text-align:center;">
        <div id="qrcode" style="display:inline-block;margin:20px auto;"></div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"><\\/script>
`;

let qrCodeInstance = null;

function generate() {
    const text = document.getElementById('inputText').value.trim();
    if (!text) return;
    const container = document.getElementById('qrcode');
    container.innerHTML = '';
    qrCodeInstance = new QRCode(container, {
        text: text,
        width: 256,
        height: 256,
        colorDark: '#000000',
        colorLight: '#ffffff',
        correctLevel: QRCode.CorrectLevel.H
    });
}
''',

    "color-picker": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area" style="text-align:center;">
        <label>Pick a Color:</label><br>
        <input type="color" id="colorPicker" value="#3b82f6" style="width:200px;height:100px;border:none;cursor:pointer;">
    </div>
    <div class="output-area" style="margin-top:20px;">
        <div class="stats-grid">
            <div class="stat-card"><span class="stat-label">HEX</span><span class="stat-value" id="hexValue">#3b82f6</span></div>
            <div class="stat-card"><span class="stat-label">RGB</span><span class="stat-value" id="rgbValue">rgb(59, 130, 246)</span></div>
            <div class="stat-card"><span class="stat-label">HSL</span><span class="stat-value" id="hslValue">hsl(217, 91%, 60%)</span></div>
        </div>
    </div>
`;

function hexToRgb(hex) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `rgb(${r}, ${g}, ${b})`;
}

function hexToHsl(hex) {
    let r = parseInt(hex.slice(1, 3), 16) / 255;
    let g = parseInt(hex.slice(3, 5), 16) / 255;
    let b = parseInt(hex.slice(5, 7), 16) / 255;
    const max = Math.max(r, g, b), min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;
    if (max === min) { h = s = 0; }
    else {
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r: h = ((g - b) / d + (g < b ? 6 : 0)) / 6; break;
            case g: h = ((b - r) / d + 2) / 6; break;
            case b: h = ((r - g) / d + 4) / 6; break;
        }
    }
    return `hsl(${Math.round(h*360)}, ${Math.round(s*100)}%, ${Math.round(l*100)}%)`;
}

function updateColors() {
    const hex = document.getElementById('colorPicker').value;
    document.getElementById('hexValue').textContent = hex;
    document.getElementById('rgbValue').textContent = hexToRgb(hex);
    document.getElementById('hslValue').textContent = hexToHsl(hex);
}

document.getElementById('colorPicker').addEventListener('input', updateColors);
updateColors();
''',

    "timestamp-converter": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label>Unix Timestamp:</label>
        <input type="number" id="timestamp" value="${Math.floor(Date.now()/1000)}" style="width:100%;padding:8px;margin-bottom:16px;">
        <button onclick="convertFromTimestamp()" class="btn btn-primary">Convert to Date</button>
    </div>
    <div class="output-area">
        <h3>Human Readable Date:</h3>
        <div id="dateOutput" style="font-size:1.2rem;padding:16px;background:#f8f9fa;border-radius:8px;"></div>
    </div>
    <div class="input-area" style="margin-top:32px;">
        <label>Date String:</label>
        <input type="datetime-local" id="dateInput" style="width:100%;padding:8px;margin-bottom:16px;">
        <button onclick="convertToTimestamp()" class="btn btn-primary">Convert to Timestamp</button>
    </div>
    <div class="output-area">
        <h3>Unix Timestamp:</h3>
        <div id="timestampOutput" style="font-size:1.2rem;padding:16px;background:#f8f9fa;border-radius:8px;"></div>
    </div>
`;

function convertFromTimestamp() {
    const ts = parseInt(document.getElementById('timestamp').value);
    const date = new Date(ts * 1000);
    document.getElementById('dateOutput').textContent = date.toString();
}

function convertToTimestamp() {
    const dateStr = document.getElementById('dateInput').value;
    if (!dateStr) return;
    const ts = Math.floor(new Date(dateStr).getTime() / 1000);
    document.getElementById('timestampOutput').textContent = ts;
}

convertFromTimestamp();
''',

    "regex-tester": '''const toolSection = document.getElementById('toolSection');
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
''',
}

# 生成所有剩余工具
for tool_id, js_code in remaining_tools.items():
    filename = f"{tool_id}.js"
    with open(filename, 'w') as f:
        f.write(js_code)
    print(f"✅ Generated {filename}")

print(f"\\n🎉 Generated {len(remaining_tools)} remaining tools!")
