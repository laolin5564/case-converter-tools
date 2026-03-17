// Line Counter
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
    const lines = text.split('\n');
    const nonEmpty = lines.filter(l => l.trim());
    document.getElementById('lineCount').textContent = text ? lines.length : 0;
    document.getElementById('nonEmptyCount').textContent = nonEmpty.length;
    document.getElementById('emptyCount').textContent = lines.length - nonEmpty.length;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
