#!/usr/bin/env python3

# 通用转换器模板
def create_converter(input_label, output_label, convert_fn, button_text="Convert"):
    return f'''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">{input_label}:</label>
        <textarea id="inputText" rows="8" placeholder="Enter text here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="convert()" class="btn btn-primary">{button_text}</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <label for="outputText">{output_label}:</label>
        <textarea id="outputText" rows="8" readonly placeholder="Result will appear here..."></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

{convert_fn}

function copyOutput() {{
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {{
        document.getElementById('copyBtn').textContent = '✅ Copied!';
        setTimeout(() => {{ document.getElementById('copyBtn').textContent = '📋 Copy'; }}, 2000);
    }});
}}

function clearAll() {{
    document.getElementById('inputText').value = '';
    document.getElementById('outputText').value = '';
}}
'''

# 转换类工具
converters = {
    "text-repeater": '''const toolSection = document.getElementById('toolSection');
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
    const result = Array(count).fill(text).join('\\n');
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

    "text-reverser": create_converter(
        "Text to Reverse",
        "Reversed Text",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const reversed = input.split('').reverse().join('');
    document.getElementById('outputText').value = reversed;
}''',
        "Reverse Text"
    ),

    "remove-duplicate-lines": create_converter(
        "Text with Duplicate Lines",
        "Unique Lines",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const lines = input.split('\\n');
    const unique = [...new Set(lines)];
    document.getElementById('outputText').value = unique.join('\\n');
}''',
        "Remove Duplicates"
    ),

    "remove-empty-lines": create_converter(
        "Text with Empty Lines",
        "Text without Empty Lines",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const lines = input.split('\\n').filter(line => line.trim());
    document.getElementById('outputText').value = lines.join('\\n');
}''',
        "Remove Empty Lines"
    ),

    "remove-line-breaks": create_converter(
        "Text with Line Breaks",
        "Single Line Text",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const result = input.replace(/\\n/g, ' ').replace(/\\s+/g, ' ').trim();
    document.getElementById('outputText').value = result;
}''',
        "Remove Line Breaks"
    ),

    "add-line-numbers": create_converter(
        "Text",
        "Text with Line Numbers",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const lines = input.split('\\n');
    const numbered = lines.map((line, i) => `${i + 1}. ${line}`);
    document.getElementById('outputText').value = numbered.join('\\n');
}''',
        "Add Line Numbers"
    ),

    "sort-lines": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text to Sort:</label>
        <textarea id="inputText" rows="8" placeholder="Enter text here..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="sortAsc()" class="btn btn-primary">Sort A-Z</button>
        <button onclick="sortDesc()" class="btn btn-secondary">Sort Z-A</button>
        <button onclick="clearAll()" class="btn btn-clear">Clear</button>
    </div>
    <div class="output-area">
        <label for="outputText">Sorted Text:</label>
        <textarea id="outputText" rows="8" readonly></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy</button>
    </div>
`;

function sortAsc() {
    const input = document.getElementById('inputText').value;
    const lines = input.split('\\n').sort();
    document.getElementById('outputText').value = lines.join('\\n');
}

function sortDesc() {
    const input = document.getElementById('inputText').value;
    const lines = input.split('\\n').sort().reverse();
    document.getElementById('outputText').value = lines.join('\\n');
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

    "text-to-binary": create_converter(
        "Text",
        "Binary",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const binary = input.split('').map(char => 
        char.charCodeAt(0).toString(2).padStart(8, '0')
    ).join(' ');
    document.getElementById('outputText').value = binary;
}''',
        "Convert to Binary"
    ),

    "binary-to-text": create_converter(
        "Binary",
        "Text",
        '''function convert() {
    try {
        const input = document.getElementById('inputText').value;
        const binary = input.replace(/\\s/g, '').match(/.{1,8}/g) || [];
        const text = binary.map(bin => String.fromCharCode(parseInt(bin, 2))).join('');
        document.getElementById('outputText').value = text;
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid binary input';
    }
}''',
        "Convert to Text"
    ),

    "text-to-hex": create_converter(
        "Text",
        "Hexadecimal",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const hex = input.split('').map(char => 
        char.charCodeAt(0).toString(16).padStart(2, '0')
    ).join(' ');
    document.getElementById('outputText').value = hex;
}''',
        "Convert to Hex"
    ),

    "hex-to-text": create_converter(
        "Hexadecimal",
        "Text",
        '''function convert() {
    try {
        const input = document.getElementById('inputText').value;
        const hex = input.replace(/\\s/g, '').match(/.{1,2}/g) || [];
        const text = hex.map(h => String.fromCharCode(parseInt(h, 16))).join('');
        document.getElementById('outputText').value = text;
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid hex input';
    }
}''',
        "Convert to Text"
    ),

    "base64-encode": create_converter(
        "Text",
        "Base64",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const encoded = btoa(unescape(encodeURIComponent(input)));
    document.getElementById('outputText').value = encoded;
}''',
        "Encode to Base64"
    ),

    "base64-decode": create_converter(
        "Base64",
        "Decoded Text",
        '''function convert() {
    try {
        const input = document.getElementById('inputText').value;
        const decoded = decodeURIComponent(escape(atob(input)));
        document.getElementById('outputText').value = decoded;
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid Base64 input';
    }
}''',
        "Decode from Base64"
    ),

    "url-encode": create_converter(
        "Text",
        "URL Encoded",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const encoded = encodeURIComponent(input);
    document.getElementById('outputText').value = encoded;
}''',
        "URL Encode"
    ),

    "url-decode": create_converter(
        "URL Encoded Text",
        "Decoded Text",
        '''function convert() {
    try {
        const input = document.getElementById('inputText').value;
        const decoded = decodeURIComponent(input);
        document.getElementById('outputText').value = decoded;
    } catch(e) {
        document.getElementById('outputText').value = 'Error: Invalid URL encoded input';
    }
}''',
        "URL Decode"
    ),

    "html-encode": create_converter(
        "Text",
        "HTML Encoded",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const div = document.createElement('div');
    div.textContent = input;
    document.getElementById('outputText').value = div.innerHTML;
}''',
        "HTML Encode"
    ),

    "html-decode": create_converter(
        "HTML Encoded Text",
        "Decoded Text",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const div = document.createElement('div');
    div.innerHTML = input;
    document.getElementById('outputText').value = div.textContent;
}''',
        "HTML Decode"
    ),
}

# 生成所有转换类工具
for tool_id, js_code in converters.items():
    filename = f"{tool_id}.js"
    with open(filename, 'w') as f:
        f.write(js_code)
    print(f"✅ Generated {filename}")

print(f"\\n🎯 Generated {len(converters)} converter tools!")
