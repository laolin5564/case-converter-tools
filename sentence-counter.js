// Sentence Counter
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
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    document.getElementById('sentenceCount').textContent = sentences.length;
    document.getElementById('avgWords').textContent = sentences.length ? Math.round(words / sentences.length) : 0;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
