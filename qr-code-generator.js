const toolSection = document.getElementById('toolSection');
toolSection.innerHTML = `
    <div class="input-area">
        <label for="inputText">Text or URL:</label>
        <textarea id="inputText" rows="4" placeholder="Enter text or URL..."></textarea>
    </div>
    <div class="buttons-grid">
        <button onclick="generate()" class="btn btn-primary">Generate QR Code</button>
    </div>
    <div class="output-area" style="text-align:center;">
        <div id="qrcode" style="display:inline-block;margin:20px auto;"></div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"><\/script>
`;

let qrCodeInstance = null;

function generate() {
    const text = document.getElementById('inputText').value.trim();
    if (!text) return;
    const container = document.getElementById('qrcode');
    container.innerHTML = '';
    qrCodeInstance = new QRCode(container, {
        text: text,
        width: 256,
        height: 256,
        colorDark: '#000000',
        colorLight: '#ffffff',
        correctLevel: QRCode.CorrectLevel.H
    });
}
