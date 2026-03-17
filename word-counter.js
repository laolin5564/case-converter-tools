// Word Counter
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
    document.getElementById('wordCount').textContent = text.trim() ? text.trim().split(/\s+/).length : 0;
    document.getElementById('charCount').textContent = text.length;
    document.getElementById('charNoSpaceCount').textContent = text.replace(/\s/g, '').length;
    document.getElementById('lineCount').textContent = text ? text.split('\n').length : 0;
    document.getElementById('sentenceCount').textContent = text.split(/[.!?]+/).filter(s => s.trim()).length;
    document.getElementById('paragraphCount').textContent = text.split(/\n\n+/).filter(p => p.trim()).length;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
