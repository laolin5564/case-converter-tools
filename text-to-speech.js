const toolSection = document.getElementById('toolSection');
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
