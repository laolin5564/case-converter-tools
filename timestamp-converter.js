const toolSection = document.getElementById('toolSection');
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
