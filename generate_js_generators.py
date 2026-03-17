#!/usr/bin/env python3

# 通用工具模板生成器
def create_basic_converter(input_label, output_label, convert_fn, button_text="Convert"):
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
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy to Clipboard</button>
    </div>
`;

{convert_fn}

function copyOutput() {{
    const output = document.getElementById('outputText');
    if (!output.value) return;
    navigator.clipboard.writeText(output.value).then(() => {{
        const btn = document.getElementById('copyBtn');
        btn.textContent = '✅ Copied!';
        setTimeout(() => {{ btn.textContent = '📋 Copy to Clipboard'; }}, 2000);
    }});
}}

function clearAll() {{
    document.getElementById('inputText').value = '';
    document.getElementById('outputText').value = '';
}}
'''

# 生成器类工具
generators = {
    "lorem-ipsum-generator": '''const toolSection = document.getElementById('toolSection');
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
    document.getElementById('outputText').value = result.join('\\n\\n');
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
''',

    "random-string-generator": '''const toolSection = document.getElementById('toolSection');
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
''',

    "uuid-generator": '''const toolSection = document.getElementById('toolSection');
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
    document.getElementById('outputText').value = uuids.join('\\n');
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
''',

    "password-generator": '''const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label>Password Length:</label>
        <input type="number" id="length" value="16" min="4" max="128" style="width:100px;padding:8px;margin-bottom:8px;"><br>
        <label><input type="checkbox" id="useUpper" checked> Uppercase Letters</label><br>
        <label><input type="checkbox" id="useLower" checked> Lowercase Letters</label><br>
        <label><input type="checkbox" id="useNumbers" checked> Numbers</label><br>
        <label><input type="checkbox" id="useSpecial" checked> Special Characters</label><br>
        <button onclick="generate()" class="btn btn-primary" style="margin-top:12px;">Generate Password</button>
    </div>
    <div class="output-area">
        <label for="outputText">Generated Password:</label>
        <textarea id="outputText" rows="3" readonly style="font-family:monospace;font-size:1.2rem;"></textarea>
        <button onclick="copyOutput()" class="btn btn-copy" id="copyBtn">📋 Copy Password</button>
    </div>
`;

function generate() {
    const length = parseInt(document.getElementById('length').value) || 16;
    let chars = '';
    if (document.getElementById('useUpper').checked) chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (document.getElementById('useLower').checked) chars += 'abcdefghijklmnopqrstuvwxyz';
    if (document.getElementById('useNumbers').checked) chars += '0123456789';
    if (document.getElementById('useSpecial').checked) chars += '!@#$%^&*()_+-=[]{}|;:,.<>?';
    if (!chars) chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
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
        setTimeout(() => { btn.textContent = '📋 Copy Password'; }, 2000);
    });
}

generate();
''',

    "slug-generator": create_basic_converter(
        "Text",
        "URL Slug",
        '''function convert() {
    const input = document.getElementById('inputText').value;
    const slug = input.toLowerCase()
        .trim()
        .replace(/[^a-z0-9\\s-]/g, '')
        .replace(/\\s+/g, '-')
        .replace(/-+/g, '-');
    document.getElementById('outputText').value = slug;
}''',
        "Generate Slug"
    ),
}

# 生成generators
for tool_id, js_code in generators.items():
    filename = f"{tool_id}.js"
    with open(filename, 'w') as f:
        f.write(js_code)
    print(f"✅ Generated {filename}")

print("\\n🎯 Generated generator tools!")
