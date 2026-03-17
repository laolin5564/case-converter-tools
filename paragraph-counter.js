// Paragraph Counter
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
    const paragraphs = text.split(/\n\n+/).filter(p => p.trim());
    const sentences = text.split(/[.!?]+/).filter(s => s.trim()).length;
    document.getElementById('paragraphCount').textContent = paragraphs.length;
    document.getElementById('avgSentences').textContent = paragraphs.length ? Math.round(sentences / paragraphs.length) : 0;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
