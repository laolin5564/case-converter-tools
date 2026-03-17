const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area" style="text-align:center;">
        <label>Pick a Color:</label><br>
        <input type="color" id="colorPicker" value="#3b82f6" style="width:200px;height:100px;border:none;cursor:pointer;">
    </div>
    <div class="output-area" style="margin-top:20px;">
        <div class="stats-grid">
            <div class="stat-card"><span class="stat-label">HEX</span><span class="stat-value" id="hexValue">#3b82f6</span></div>
            <div class="stat-card"><span class="stat-label">RGB</span><span class="stat-value" id="rgbValue">rgb(59, 130, 246)</span></div>
            <div class="stat-card"><span class="stat-label">HSL</span><span class="stat-value" id="hslValue">hsl(217, 91%, 60%)</span></div>
        </div>
    </div>
`;

function hexToRgb(hex) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `rgb(${r}, ${g}, ${b})`;
}

function hexToHsl(hex) {
    let r = parseInt(hex.slice(1, 3), 16) / 255;
    let g = parseInt(hex.slice(3, 5), 16) / 255;
    let b = parseInt(hex.slice(5, 7), 16) / 255;
    const max = Math.max(r, g, b), min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;
    if (max === min) { h = s = 0; }
    else {
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r: h = ((g - b) / d + (g < b ? 6 : 0)) / 6; break;
            case g: h = ((b - r) / d + 2) / 6; break;
            case b: h = ((r - g) / d + 4) / 6; break;
        }
    }
    return `hsl(${Math.round(h*360)}, ${Math.round(s*100)}%, ${Math.round(l*100)}%)`;
}

function updateColors() {
    const hex = document.getElementById('colorPicker').value;
    document.getElementById('hexValue').textContent = hex;
    document.getElementById('rgbValue').textContent = hexToRgb(hex);
    document.getElementById('hslValue').textContent = hexToHsl(hex);
}

document.getElementById('colorPicker').addEventListener('input', updateColors);
updateColors();
