// Character Counter
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
    document.getElementById('charNoSpaceCount').textContent = text.replace(/\s/g, '').length;
    document.getElementById('letterCount').textContent = (text.match(/[a-zA-Z]/g) || []).length;
    document.getElementById('digitCount').textContent = (text.match(/\d/g) || []).length;
    document.getElementById('spaceCount').textContent = (text.match(/\s/g) || []).length;
    document.getElementById('specialCount').textContent = (text.match(/[^a-zA-Z0-9\s]/g) || []).length;
}

document.getElementById('inputText').addEventListener('input', updateCounts);
updateCounts();
