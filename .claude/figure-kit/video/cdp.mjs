// usage: node cdp.mjs <page-url> <frames-dir> <chrome-profile-dir> <seconds> <fps> [port=9333]
// Opens the page in headless Chrome (1280x720), calls window.render(t) for each frame, saves PNGs f0000.png...
import { spawn } from 'node:child_process';
import fs from 'node:fs';
const [,, url, outdir, prof, dur, fps, port = '9333'] = process.argv;
if (!url || !outdir || !prof || !dur || !fps) { console.error('usage: node cdp.mjs <url> <frames-dir> <profile-dir> <seconds> <fps> [port]'); process.exit(1); }
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const chrome = spawn(CHROME,
 ['--headless=new', `--remote-debugging-port=${port}`, '--hide-scrollbars', '--window-size=1280,720', `--user-data-dir=${prof}`, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let ws;
for (let i = 0; i < 50; i++) {
  try {
    const l = await (await fetch(`http://127.0.0.1:${port}/json`)).json();
    const p = l.find(x => x.type === 'page');
    if (p) { ws = new WebSocket(p.webSocketDebuggerUrl); break; }
  } catch {}
  await sleep(200);
}
await new Promise(r => ws.onopen = r);
let id = 0; const pend = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } };
const call = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
await call('Emulation.setDeviceMetricsOverride', { width: 1280, height: 720, deviceScaleFactor: 1, mobile: false });
await call('Page.enable'); await call('Page.navigate', { url });
await sleep(4000);
await call('Runtime.evaluate', { expression: 'document.fonts.ready.then(()=>1)', awaitPromise: true });
const n = Math.round(dur * fps);
for (let i = 0; i < n; i++) {
  await call('Runtime.evaluate', { expression: `render(${i / fps})` });
  const r = await call('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${outdir}/f${String(i).padStart(4, '0')}.png`, Buffer.from(r.result.data, 'base64'));
}
ws.close(); chrome.kill(); console.log('frames', n);
