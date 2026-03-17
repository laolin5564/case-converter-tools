#!/usr/bin/env python3
import json

# 读取工具配置
with open('tools-config.json', 'r') as f:
    config = json.load(f)

tools = config['tools']

# JS代码模板定义
js_templates = {
    # 文本计数类工具
    "word-counter": '''// Word Counter
const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Paste or type your text here:</label>
        <textarea id="inputText" rows="8" placeholder="Type or paste your text here..."></textarea>
    </div>
    <div class="output-area">
        <div class="stats-grid">
            <div class="stat-card"><span class="stat-value" id="wordCount">0</span><span class="stat-label">Words</span></div>
            <div class="stat-card"><span class="stat-value" id="charCount">0</span><span class="stat-label">Characters</span></div>
            <div class="stat-card"><span class="stat-value" id="charNoSpaceCount">0</span><span class="stat-label">Characters (no spaces)</span></div>
            <div class="stat-card"><span class="stat-value" id="lineCount">0</span><span class="stat-label">Lines</span></div>
            <div class="stat-card"><span class="stat-value" id="sentenceCount">0</span><span class="stat-label">Sentences</span></div>
            <div class="stat-card"><span class="stat-value" id="paragraphCount">0</span><span class="stat-label">Paragraphs</span></div>
        </div>
    </div>
`;

function updateCounts() {
    const text = document.getElementById('inputText').value;
    document.getElementById('wordCount').textContent = text.trim() ? text.trim().split(/\\s+/).length : 0;
    document.getElementById('charCount').textContent = text.length;
    document.getElementById('charNoSpaceCount').textContent = text.replace(/\\s/g, '').length;
    document.getElementById('lineCount').textContent = text ? text.split('\\n').length : 0;
    document.getElementById('sentenceCount').textContent = text.split(/[.!?]+/).filter(s => s.trim()).length;
    document.getElementById('paragraphCount').textContent = text.split(/\\n\\n+/).filter(p => p.trim()).length;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
''',

    "character-counter": '''// Character Counter
const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Paste or type your text here:</label>
        <textarea id="inputText" rows="8" placeholder="Type or paste your text here..."></textarea>
    </div>
    <div class="output-area">
        <div class="stats-grid">
            <div class="stat-card"><span class="stat-value" id="charCount">0</span><span class="stat-label">Total Characters</span></div>
            <div class="stat-card"><span class="stat-value" id="charNoSpaceCount">0</span><span class="stat-label">Characters (no spaces)</span></div>
            <div class="stat-card"><span class="stat-value" id="letterCount">0</span><span class="stat-label">Letters</span></div>
            <div class="stat-card"><span class="stat-value" id="digitCount">0</span><span class="stat-label">Digits</span></div>
            <div class="stat-card"><span class="stat-value" id="spaceCount">0</span><span class="stat-label">Spaces</span></div>
            <div class="stat-card"><span class="stat-value" id="specialCount">0</span><span class="stat-label">Special Characters</span></div>
        </div>
    </div>
`;

function updateCounts() {
    const text = document.getElementById('inputText').value;
    document.getElementById('charCount').textContent = text.length;
    document.getElementById('charNoSpaceCount').textContent = text.replace(/\\s/g, '').length;
    document.getElementById('letterCount').textContent = (text.match(/[a-zA-Z]/g) || []).length;
    document.getElementById('digitCount').textContent = (text.match(/\\d/g) || []).length;
    document.getElementById('spaceCount').textContent = (text.match(/\\s/g) || []).length;
    document.getElementById('specialCount').textContent = (text.match(/[^a-zA-Z0-9\\s]/g) || []).length;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
''',

    "line-counter": '''// Line Counter
const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Paste or type your text here:</label>
        <textarea id="inputText" rows="10" placeholder="Type or paste your text here..."></textarea>
    </div>
    <div class="output-area">
        <div class="stats-grid">
            <div class="stat-card"><span class="stat-value" id="lineCount">0</span><span class="stat-label">Total Lines</span></div>
            <div class="stat-card"><span class="stat-value" id="nonEmptyCount">0</span><span class="stat-label">Non-Empty Lines</span></div>
            <div class="stat-card"><span class="stat-value" id="emptyCount">0</span><span class="stat-label">Empty Lines</span></div>
        </div>
    </div>
`;

function updateCounts() {
    const text = document.getElementById('inputText').value;
    const lines = text.split('\\n');
    const nonEmpty = lines.filter(l => l.trim());
    document.getElementById('lineCount').textContent = text ? lines.length : 0;
    document.getElementById('nonEmptyCount').textContent = nonEmpty.length;
    document.getElementById('emptyCount').textContent = lines.length - nonEmpty.length;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
''',

    "sentence-counter": '''// Sentence Counter
const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Paste or type your text here:</label>
        <textarea id="inputText" rows="8" placeholder="Type or paste your text here..."></textarea>
    </div>
    <div class="output-area">
        <div class="stats-grid">
            <div class="stat-card"><span class="stat-value" id="sentenceCount">0</span><span class="stat-label">Sentences</span></div>
            <div class="stat-card"><span class="stat-value" id="avgWords">0</span><span class="stat-label">Avg Words/Sentence</span></div>
        </div>
    </div>
`;

function updateCounts() {
    const text = document.getElementById('inputText').value;
    const sentences = text.split(/[.!?]+/).filter(s => s.trim());
    const words = text.trim() ? text.trim().split(/\\s+/).length : 0;
    document.getElementById('sentenceCount').textContent = sentences.length;
    document.getElementById('avgWords').textContent = sentences.length ? Math.round(words / sentences.length) : 0;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
''',

    "paragraph-counter": '''// Paragraph Counter
const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Paste or type your text here:</label>
        <textarea id="inputText" rows="10" placeholder="Type or paste your text here..."></textarea>
    </div>
    <div class="output-area">
        <div class="stats-grid">
            <div class="stat-card"><span class="stat-value" id="paragraphCount">0</span><span class="stat-label">Paragraphs</span></div>
            <div class="stat-card"><span class="stat-value" id="avgSentences">0</span><span class="stat-label">Avg Sentences/Paragraph</span></div>
        </div>
    </div>
`;

function updateCounts() {
    const text = document.getElementById('inputText').value;
    const paragraphs = text.split(/\\n\\n+/).filter(p => p.trim());
    const sentences = text.split(/[.!?]+/).filter(s => s.trim()).length;
    document.getElementById('paragraphCount').textContent = paragraphs.length;
    document.getElementById('avgSentences').textContent = paragraphs.length ? Math.round(sentences / paragraphs.length) : 0;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
''',
}

# 由于代码太长，我将分多个文件生成。先生成基础工具
for tool in tools[:6]:
    tool_id = tool['id']
    if tool_id in js_templates:
        js_content = js_templates[tool_id]
        filename = f"{tool_id}.js"
        with open(filename, 'w') as f:
            f.write(js_content)
        print(f"✅ Generated {filename}")

print("\\n🎯 Step 1: Generated first 6 JS files. Continuing with more...")
