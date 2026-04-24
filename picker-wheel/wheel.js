/* ═══ PICKER WHEEL – Full Featured JS ═══ */

// ── CRYPTO RANDOM (like wheelofnames) ──
function cryptoRand() {
  const arr = new Uint32Array(1);
  crypto.getRandomValues(arr);
  return arr[0] / 0xFFFFFFFF;
}

// ── STATE ──
let entries = []; // [{text, weight, color}]
let spinHistory = [];
let spinning = false;
let currentAngle = 0;
let settings = {
  sound: true, confetti: true, remove: false,
  popup: true, themeIdx: 0, speed: 3, volume: 0.6,
  soundTheme: 'tick', displayMode: 'wheel', showCount: true
};

const THEMES = [
  ['#e74c3c','#e67e22','#f1c40f','#2ecc71','#1abc9c','#3498db','#9b59b6','#e91e63','#ff5722','#607d8b'],
  ['#ff6b6b','#feca57','#48dbfb','#ff9ff3','#54a0ff','#5f27cd','#00d2d3','#ff9f43','#1dd1a1','#c8d6e5'],
  ['#1a1a2e','#16213e','#0f3460','#533483','#e94560','#457b9d','#1d3557','#a8dadc','#2b2d42','#8d99ae'],
  ['#6c5ce7','#a29bfe','#fd79a8','#fdcb6e','#00cec9','#55efc4','#e17055','#74b9ff','#0984e3','#d63031'],
  ['#2ecc71','#27ae60','#1abc9c','#16a085','#3498db','#2980b9','#9b59b6','#8e44ad','#f39c12','#d35400'],
  ['#ff0000','#ff4000','#ff8000','#ffbf00','#ffff00','#80ff00','#00ff00','#00ff80','#00ffff','#0080ff'],
];

// ── CANVAS ──
const canvas = document.getElementById('wheelCanvas');
const ctx = canvas.getContext('2d');
const SIZE = 420;

function getSegColors() {
  return entries.map((e, i) => e.color || THEMES[settings.themeIdx][i % THEMES[settings.themeIdx].length]);
}

function isLight(hex) {
  const r=parseInt(hex.slice(1,3),16), g=parseInt(hex.slice(3,5),16), b=parseInt(hex.slice(5,7),16);
  return (r*299+g*587+b*114)/1000 > 155;
}

// Build weighted segment array
function getSegments() {
  const segs = [];
  entries.forEach((e, i) => {
    const w = Math.max(1, parseInt(e.weight) || 1);
    for (let j = 0; j < w; j++) segs.push(i);
  });
  return segs;
}

function drawWheel() {
  ctx.clearRect(0, 0, SIZE, SIZE);
  const cx = SIZE/2, cy = SIZE/2, r = SIZE/2 - 10;
  const n = entries.length;
  const segs = getSegments();
  const total = segs.length;
  const colors = getSegColors();

  if (n === 0) {
    ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2);
    const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, r);
    grad.addColorStop(0, '#f8f9fa'); grad.addColorStop(1, '#e9ecef');
    ctx.fillStyle = grad; ctx.fill();
    ctx.strokeStyle = '#dee2e6'; ctx.lineWidth = 4; ctx.stroke();
    ctx.fillStyle = '#adb5bd'; ctx.font = 'bold 15px Instrument Sans';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText('Add entries to spin!', cx, cy);
    return;
  }

  // Build arc map: each unique entry gets accumulated arc
  const arcMap = new Array(n).fill(0);
  segs.forEach(i => arcMap[i]++);
  const arcFracs = arcMap.map(c => c / total);

  // Draw segments
  ctx.save(); ctx.translate(cx, cy); ctx.rotate(currentAngle);
  let startAngle = 0;
  for (let i = 0; i < n; i++) {
    if (arcFracs[i] === 0) continue;
    const arc = arcFracs[i] * 2 * Math.PI;
    const col = colors[i];
    const isWinner = entries[i]._highlight;

    ctx.beginPath(); ctx.moveTo(0,0);
    ctx.arc(0, 0, r, startAngle, startAngle + arc);
    ctx.closePath();
    ctx.fillStyle = isWinner ? '#FFD700' : col;
    ctx.fill();
    ctx.strokeStyle = 'rgba(255,255,255,0.9)';
    ctx.lineWidth = isWinner ? 3 : 2;
    ctx.stroke();

    // Text
    ctx.save();
    ctx.rotate(startAngle + arc / 2);
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    const fs = Math.max(9, Math.min(16, r * 0.12, 180 / n));
    ctx.font = `bold ${fs}px Nunito, sans-serif`;
    ctx.fillStyle = isLight(col) ? '#1a1a1a' : '#ffffff';
    ctx.shadowColor = 'rgba(0,0,0,0.2)'; ctx.shadowBlur = 3;
    const label = entries[i].text.length > 20 ? entries[i].text.slice(0, 18) + '…' : entries[i].text;
    // Draw weight badge
    const wt = parseInt(entries[i].weight) || 1;
    const fullLabel = wt > 1 ? `${label} ×${wt}` : label;
    ctx.fillText(fullLabel, r - 14, 0);
    ctx.restore();
    startAngle += arc;
  }

  // Outer ring
  ctx.beginPath(); ctx.arc(0, 0, r, 0, Math.PI*2);
  ctx.strokeStyle = 'rgba(255,255,255,0.5)'; ctx.lineWidth = 8; ctx.stroke();
  ctx.strokeStyle = 'rgba(0,0,0,0.06)'; ctx.lineWidth = 2; ctx.stroke();

  // Center
  const cg = ctx.createRadialGradient(0,0,0,0,0,28);
  cg.addColorStop(0,'#ffffff'); cg.addColorStop(1,'#f0f0f0');
  ctx.beginPath(); ctx.arc(0,0,28,0,Math.PI*2);
  ctx.fillStyle = cg; ctx.fill();
  ctx.strokeStyle = '#ddd'; ctx.lineWidth = 3; ctx.stroke();
  ctx.restore();
}

// ── SPIN (crypto random) ──
let startRot=0, targetRot=0, spinStart=0, spinDur=0, lastTick=-1, animId;

function spinWheel() {
  if (spinning) return;
  if (entries.length < 2) { toast('Add at least 2 entries!', '⚠️'); return; }
  spinning = true;
  document.getElementById('spinBtn').disabled = true;
  document.getElementById('pwResult').classList.remove('show');
  entries.forEach(e => e._highlight = false);

  const spd = parseInt(document.getElementById('spinSpeedRange').value) || 3;
  const minSpins = 5 + spd;
  const add = cryptoRand() * (spd * 2); // crypto random
  const totalRot = (minSpins + add) * 2 * Math.PI;
  const dur = Math.max(2000, (8000 - spd * 900) + cryptoRand() * 1200);

  startRot = currentAngle;
  targetRot = currentAngle + totalRot;
  spinStart = performance.now();
  spinDur = dur;
  lastTick = -1;
  if (settings.sound) playSpinStart();
  animateSpin();
}

function easeOut(t) { return 1 - Math.pow(1 - t, 4); }

function animateSpin() {
  const elapsed = performance.now() - spinStart;
  const prog = Math.min(elapsed / spinDur, 1);
  currentAngle = startRot + (targetRot - startRot) * easeOut(prog);

  // Tick on each segment boundary
  if (settings.sound && entries.length > 0) {
    const segs = getSegments();
    const segArc = 2 * Math.PI / segs.length;
    const norm = ((currentAngle % (2*Math.PI)) + 2*Math.PI) % (2*Math.PI);
    const tick = Math.floor(norm / segArc);
    if (tick !== lastTick) { playTick(); lastTick = tick; }
  }

  drawWheel();
  if (prog < 1) { animId = requestAnimationFrame(animateSpin); }
  else {
    spinning = false;
    document.getElementById('spinBtn').disabled = false;
    announceResult();
  }
}

function announceResult() {
  const segs = getSegments();
  const total = segs.length;
  const arcUnit = 2 * Math.PI / total;
  const norm = ((-currentAngle - Math.PI/2 + 2*Math.PI*100) % (2*Math.PI) + 2*Math.PI) % (2*Math.PI);
  const segIdx = Math.floor(norm / arcUnit) % total;
  const entryIdx = segs[segIdx];
  const winner = entries[entryIdx].text;

  // Highlight winner segment briefly
  entries[entryIdx]._highlight = true;
  drawWheel();

  document.getElementById('pwResultValue').textContent = winner;
  document.getElementById('pwResult').classList.add('show');

  addToHistory(winner, entries[entryIdx].color || getSegColors()[entryIdx]);
  updateCountDisplay();

  if (settings.popup) showWinModal(winner, entries[entryIdx].color || getSegColors()[entryIdx]);
  if (settings.confetti) launchConfetti();
  if (settings.sound) playWin();

  if (settings.remove) {
    setTimeout(() => {
      entries[entryIdx]._highlight = false;
      entries.splice(entryIdx, 1);
      renderEntries(); drawWheel();
    }, 1200);
  } else {
    setTimeout(() => { entries[entryIdx]._highlight = false; drawWheel(); }, 2000);
  }
}

// ── ENTRIES ──
function makeEntry(text, weight = 1, color = '') {
  return { text: text.trim(), weight, color, _highlight: false };
}

function addEntry() {
  const inp = document.getElementById('entryInput');
  const v = inp.value.trim(); if (!v) return;
  entries.push(makeEntry(v));
  inp.value = ''; renderEntries(); drawWheel(); inp.focus();
  saveToLocalStorage();
}

function addBulk() {
  const raw = document.getElementById('bulkInput').value;
  const lines = raw.split('\n').map(l => l.trim()).filter(l => l);
  lines.forEach(l => {
    // Support "Name ×3" or "Name,3" weight syntax
    const match = l.match(/^(.+?)[\s,]×(\d+)$|^(.+?),(\d+)$/);
    if (match) {
      const text = (match[1] || match[3]).trim();
      const w = parseInt(match[2] || match[4]) || 1;
      entries.push(makeEntry(text, w));
    } else {
      entries.push(makeEntry(l));
    }
  });
  document.getElementById('bulkInput').value = '';
  renderEntries(); drawWheel(); saveToLocalStorage();
  toast(`Added ${lines.length} entries!`, '✅');
}

function importFile() {
  const f = document.getElementById('importFile').files[0]; if (!f) return;
  const r = new FileReader();
  r.onload = e => {
    const lines = e.target.result.split(/\r?\n/).map(l => l.split(',')[0].trim()).filter(l => l);
    lines.forEach(l => entries.push(makeEntry(l)));
    renderEntries(); drawWheel(); saveToLocalStorage();
    toast(`Imported ${lines.length} entries!`, '📂');
  };
  r.readAsText(f);
}

function removeEntry(i) { entries.splice(i, 1); renderEntries(); drawWheel(); saveToLocalStorage(); }
function editEntryWeight(i, w) { entries[i].weight = Math.max(1, parseInt(w) || 1); renderEntries(); drawWheel(); saveToLocalStorage(); }
function editEntryColor(i, col) { entries[i].color = col; renderEntries(); drawWheel(); saveToLocalStorage(); }

function clearAll() {
  if (!entries.length) return;
  if (confirm('Clear all entries?')) {
    entries = []; renderEntries(); drawWheel(); saveToLocalStorage();
  }
}
function shuffleEntries() {
  for (let i = entries.length-1; i > 0; i--) {
    const j = Math.floor(cryptoRand() * (i+1));
    [entries[i], entries[j]] = [entries[j], entries[i]];
  }
  renderEntries(); drawWheel(); saveToLocalStorage();
}
function sortEntries() { entries.sort((a,b) => a.text.localeCompare(b.text)); renderEntries(); drawWheel(); }
function removeDuplicates() {
  const before = entries.length;
  const seen = new Set();
  entries = entries.filter(e => { if (seen.has(e.text)) return false; seen.add(e.text); return true; });
  renderEntries(); drawWheel(); saveToLocalStorage();
  toast(`Removed ${before - entries.length} duplicates`, '⚡');
}
function loadExample() {
  entries = ['Alice','Bob','Carol','Dave','Eve','Frank','Grace','Henry'].map(n => makeEntry(n));
  renderEntries(); drawWheel(); saveToLocalStorage();
}

function renderEntries() {
  const list = document.getElementById('entriesList');
  document.getElementById('pwCount').textContent = entries.length;
  // Total weight
  const totalW = entries.reduce((s,e) => s + (parseInt(e.weight)||1), 0);
  document.getElementById('pwTotalWeight').textContent = totalW > entries.length ? `Total weight: ${totalW}` : '';

  if (!entries.length) {
    list.innerHTML = '<li style="color:var(--muted);font-size:.82rem;padding:8px;text-align:center">No entries yet. Add some above!</li>'; return;
  }
  const colors = getSegColors();
  list.innerHTML = entries.map((e, i) => `
    <li class="pw-entry" id="pe-${i}">
      <input type="color" class="pw-entry-clr" value="${e.color || colors[i]}"
        title="Segment color" onchange="editEntryColor(${i},this.value)">
      <span class="pw-entry-text" title="${e.text}">${e.text}</span>
      <input type="number" class="pw-entry-wt" value="${e.weight||1}" min="1" max="20" title="Weight (spin frequency)"
        onchange="editEntryWeight(${i},this.value)">
      <button class="pw-entry-up" onclick="moveEntry(${i},-1)" title="Move up">↑</button>
      <button class="pw-entry-dn" onclick="moveEntry(${i},1)" title="Move down">↓</button>
      <button class="pw-entry-del" onclick="removeEntry(${i})" title="Remove">✕</button>
    </li>`).join('');
}

function moveEntry(i, dir) {
  const j = i + dir;
  if (j < 0 || j >= entries.length) return;
  [entries[i], entries[j]] = [entries[j], entries[i]];
  renderEntries(); drawWheel(); saveToLocalStorage();
}

function updateCountDisplay() {
  const picked = spinHistory.length;
  const remaining = entries.length;
  const el = document.getElementById('spinCounter');
  if (el) el.textContent = `Spun: ${picked} • Remaining: ${remaining}`;
}

// ── HISTORY ──
function addToHistory(winner, color) {
  const t = new Date().toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});
  spinHistory.unshift({ winner, color, time: t });
  if (spinHistory.length > 100) spinHistory.pop();
  renderHistory();
}
function renderHistory() {
  const list = document.getElementById('historyList');
  if (!spinHistory.length) {
    list.innerHTML = '<li style="color:var(--muted);font-size:.82rem;padding:6px">No spins yet…</li>'; return;
  }
  list.innerHTML = spinHistory.map((h,i) => `
    <li class="pw-history-item">
      <div class="pw-history-num" style="background:${h.color||'var(--red)'}">${i+1}</div>
      <span class="pw-history-winner">${h.winner}</span>
      <span class="pw-history-time">${h.time}</span>
    </li>`).join('');
}
function clearHistory() { spinHistory = []; renderHistory(); updateCountDisplay(); }
function exportHistory() {
  if (!spinHistory.length) { toast('No history to export', '⚠️'); return; }
  const csv = 'Rank,Winner,Time\n' + spinHistory.map((h,i) => `${i+1},"${h.winner}",${h.time}`).join('\n');
  const blob = new Blob([csv], {type:'text/csv'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob);
  a.download = 'spin-history.csv'; a.click();
  toast('History exported!', '📥');
}

// ── SETTINGS ──
function toggleSetting(k) {
  settings[k] = !settings[k];
  document.getElementById(k+'Toggle').classList.toggle('on', settings[k]);
  saveSettings();
}
function saveSettings() { try { localStorage.setItem('pw_settings', JSON.stringify(settings)); } catch(e){} }
function loadSettings() {
  try {
    const s = JSON.parse(localStorage.getItem('pw_settings') || '{}');
    Object.assign(settings, s);
    ['sound','confetti','remove','popup'].forEach(k => {
      const el = document.getElementById(k+'Toggle');
      if (el) el.classList.toggle('on', settings[k]);
    });
    const sv = document.getElementById('spinSpeedRange'); if (sv) sv.value = settings.speed || 3;
    const vl = document.getElementById('volumeRange'); if (vl) vl.value = settings.volume || 0.6;
    const st = document.getElementById('soundThemeSelect'); if (st) st.value = settings.soundTheme || 'tick';
    setThemeByIdx(settings.themeIdx || 0, false);
  } catch(e) {}
}

// ── SAVE / LOAD WHEELS ──
function saveToLocalStorage() {
  try { localStorage.setItem('pw_entries', JSON.stringify(entries)); } catch(e){}
}
function loadFromLocalStorage() {
  try {
    const e = JSON.parse(localStorage.getItem('pw_entries') || '[]');
    entries = e.map(x => typeof x === 'string' ? makeEntry(x) : {...x, _highlight:false});
    renderEntries(); drawWheel();
  } catch(e) {}
}

function saveNamedWheel() {
  const name = prompt('Save this wheel as:', 'My Wheel'); if (!name) return;
  try {
    const wheels = JSON.parse(localStorage.getItem('pw_saved') || '{}');
    wheels[name] = entries.map(e => ({text:e.text, weight:e.weight||1, color:e.color||''}));
    localStorage.setItem('pw_saved', JSON.stringify(wheels));
    toast(`Saved as "${name}"`, '💾'); updateSavedWheelsList();
  } catch(e) { toast('Could not save', '❌'); }
}
function loadNamedWheel(name) {
  try {
    const wheels = JSON.parse(localStorage.getItem('pw_saved') || '{}');
    if (wheels[name]) {
      entries = wheels[name].map(e => ({...e, _highlight:false}));
      renderEntries(); drawWheel(); saveToLocalStorage();
      toast(`Loaded "${name}"`, '📂');
    }
  } catch(e) {}
}
function deleteNamedWheel(name) {
  try {
    const wheels = JSON.parse(localStorage.getItem('pw_saved') || '{}');
    delete wheels[name]; localStorage.setItem('pw_saved', JSON.stringify(wheels));
    updateSavedWheelsList();
  } catch(e) {}
}
function updateSavedWheelsList() {
  const el = document.getElementById('savedWheelsList'); if (!el) return;
  try {
    const wheels = JSON.parse(localStorage.getItem('pw_saved') || '{}');
    const keys = Object.keys(wheels);
    if (!keys.length) { el.innerHTML = '<div style="color:var(--muted);font-size:.8rem;padding:4px">No saved wheels</div>'; return; }
    el.innerHTML = keys.map(k => `
      <div class="pw-saved-item">
        <button onclick="loadNamedWheel('${k.replace(/'/g,"\\'")}')">📋 ${k}</button>
        <button class="pw-del-saved" onclick="deleteNamedWheel('${k.replace(/'/g,"\\'")}')">✕</button>
      </div>`).join('');
  } catch(e) {}
}

// Export wheel as JSON
function exportWheelJSON() {
  const data = { entries: entries.map(e => ({text:e.text, weight:e.weight||1})), settings };
  const blob = new Blob([JSON.stringify(data, null, 2)], {type:'application/json'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob);
  a.download = 'picker-wheel.json'; a.click();
  toast('Wheel exported!', '💾');
}
function importWheelJSON() { document.getElementById('importJSONFile').click(); }
function onImportJSON(e) {
  const f = e.target.files[0]; if (!f) return;
  const r = new FileReader();
  r.onload = ev => {
    try {
      const data = JSON.parse(ev.target.result);
      if (data.entries) {
        entries = data.entries.map(x => ({...makeEntry(x.text, x.weight||1), color:x.color||''}));
        renderEntries(); drawWheel(); saveToLocalStorage();
        toast(`Loaded ${entries.length} entries!`, '📂');
      }
    } catch(err) { toast('Invalid file', '❌'); }
  };
  r.readAsText(f);
}

// Share via URL
function shareWheel() {
  const data = encodeURIComponent(JSON.stringify(entries.map(e => e.text)));
  const url = `${location.href.split('?')[0]}?entries=${data}`;
  navigator.clipboard.writeText(url)
    .then(() => toast('Link copied!', '🔗'))
    .catch(() => prompt('Copy this link:', url));
}

// URL load
function loadFromURL() {
  const p = new URLSearchParams(location.search);
  if (p.has('entries')) {
    try {
      const d = JSON.parse(decodeURIComponent(p.get('entries')));
      if (Array.isArray(d)) {
        entries = d.map(x => typeof x === 'string' ? makeEntry(x) : makeEntry(x.text || x, x.weight));
        renderEntries(); drawWheel();
      }
    } catch(e) {}
  }
}

// Fullscreen
function fullscreenWheel() {
  const el = document.querySelector('.pw-wheel-card');
  if (!document.fullscreenElement) {
    el.requestFullscreen?.() || el.webkitRequestFullscreen?.();
  } else {
    document.exitFullscreen?.();
  }
}

// ── PALETTE / THEME ──
function buildPalette() {
  const pal = document.getElementById('pwPalette');
  const labels = ['🎨 Vivid','🍬 Pastel','🌑 Dark','💜 Purple','🌿 Green','🌈 Rainbow'];
  const samples = ['#e74c3c','#ff6b6b','#1a1a2e','#6c5ce7','#2ecc71','#ff0000'];
  pal.innerHTML = labels.map((l,i) => `
    <button class="pw-palette-btn ${i===settings.themeIdx?'selected':''}" style="background:${samples[i]}"
      title="${l}" onclick="setThemeByIdx(${i},this)"></button>`).join('');
}
function setThemeByIdx(idx, btn) {
  settings.themeIdx = idx;
  document.querySelectorAll('.pw-palette-btn').forEach((b,i) => b.classList.toggle('selected', i===idx));
  renderEntries(); drawWheel(); saveSettings();
}

// ── TABS ──
function switchTab(name) {
  const names = ['manual','bulk','import'];
  document.querySelectorAll('#pwTabs .pw-tab').forEach((t,i) => t.classList.toggle('active', names[i]===name));
  names.forEach(n => document.getElementById('tab-'+n).classList.toggle('active', n===name));
}

// ── WIN MODAL ──
function showWinModal(winner, color) {
  document.getElementById('winResultText').textContent = winner;
  document.getElementById('winResultText').style.borderLeft = `5px solid ${color||'var(--red)'}`;
  const emojis = ['🏆','🎉','⭐','🥇','🎊','🌟','✨','🎈','🙌','🔥'];
  document.getElementById('winEmoji').textContent = emojis[Math.floor(cryptoRand()*emojis.length)];
  document.getElementById('winModal').classList.add('show');
}
function closeModal() { document.getElementById('winModal').classList.remove('show'); stopConfetti(); }
document.getElementById('winModal').addEventListener('click', e => {
  if (e.target.id === 'winModal') closeModal();
});

// ── SOUND ENGINE ──
let audioCtx;
function getAC() { if (!audioCtx) audioCtx = new (window.AudioContext||window.webkitAudioContext)(); return audioCtx; }

const SOUND_THEMES = {
  tick: () => { const ac=getAC(),o=ac.createOscillator(),g=ac.createGain(); o.connect(g); g.connect(ac.destination); o.frequency.value=900+cryptoRand()*300; o.type='triangle'; const v=parseFloat(document.getElementById('volumeRange').value); g.gain.setValueAtTime(v*.12,ac.currentTime); g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.07); o.start(); o.stop(ac.currentTime+.08); },
  click: () => { const ac=getAC(),b=ac.createOscillator(),g=ac.createGain(); b.connect(g); g.connect(ac.destination); b.frequency.value=1200; b.type='square'; const v=parseFloat(document.getElementById('volumeRange').value); g.gain.setValueAtTime(v*.08,ac.currentTime); g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.05); b.start(); b.stop(ac.currentTime+.06); },
  drum: () => { const ac=getAC(),o=ac.createOscillator(),g=ac.createGain(); o.connect(g); g.connect(ac.destination); o.frequency.setValueAtTime(150,ac.currentTime); o.frequency.exponentialRampToValueAtTime(50,ac.currentTime+.1); o.type='sine'; const v=parseFloat(document.getElementById('volumeRange').value); g.gain.setValueAtTime(v*.3,ac.currentTime); g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.12); o.start(); o.stop(ac.currentTime+.14); },
  silent: () => {},
};

function playTick() {
  if (!settings.sound) return;
  try { (SOUND_THEMES[settings.soundTheme] || SOUND_THEMES.tick)(); } catch(e) {}
}
function playSpinStart() {
  if (!settings.sound) return;
  try {
    const ac=getAC(), v=parseFloat(document.getElementById('volumeRange').value);
    const o=ac.createOscillator(), g=ac.createGain();
    o.connect(g); g.connect(ac.destination);
    o.frequency.setValueAtTime(300,ac.currentTime); o.frequency.linearRampToValueAtTime(600,ac.currentTime+.15);
    o.type='sine'; g.gain.setValueAtTime(v*.25,ac.currentTime); g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.2);
    o.start(); o.stop(ac.currentTime+.22);
  } catch(e) {}
}
function playWin() {
  if (!settings.sound) return;
  try {
    const ac=getAC(), v=parseFloat(document.getElementById('volumeRange').value);
    const melody = [523,659,784,1047,1319];
    melody.forEach((f,i) => {
      const o=ac.createOscillator(), g=ac.createGain();
      o.connect(g); g.connect(ac.destination);
      o.frequency.value=f; o.type='sine';
      const t=ac.currentTime+i*.11;
      g.gain.setValueAtTime(0,t); g.gain.linearRampToValueAtTime(v*.3,t+.04);
      g.gain.exponentialRampToValueAtTime(.001,t+.38);
      o.start(t); o.stop(t+.42);
    });
  } catch(e) {}
}

// ── CONFETTI ──
const cCanvas=document.getElementById('confettiCanvas');
const cCtx=cCanvas.getContext('2d');
let cPieces=[], cAnimId;
function launchConfetti() {
  cCanvas.style.display='block';
  cCanvas.width=window.innerWidth; cCanvas.height=window.innerHeight;
  cPieces=[];
  const cols=['#e74c3c','#f39c12','#3498db','#2ecc71','#9b59b6','#e91e63','#1abc9c','#f1c40f','#ff5722','#00bcd4'];
  for (let i=0;i<220;i++) {
    const shape = cryptoRand() > 0.5 ? 'rect' : 'circle';
    cPieces.push({
      x:cryptoRand()*cCanvas.width, y:-20-cryptoRand()*80,
      w:6+cryptoRand()*10, h:4+cryptoRand()*6,
      r:cryptoRand()*Math.PI*2, dr:(cryptoRand()-.5)*.35,
      vx:(cryptoRand()-.5)*4, vy:2+cryptoRand()*5,
      color:cols[Math.floor(cryptoRand()*cols.length)], life:1, shape
    });
  }
  animConf(); setTimeout(stopConfetti, 5000);
}
function animConf() {
  cCtx.clearRect(0,0,cCanvas.width,cCanvas.height);
  let alive=false;
  cPieces.forEach(p => {
    p.x+=p.vx; p.y+=p.vy; p.r+=p.dr; p.vy+=.1; p.life-=.007;
    if (p.life>0 && p.y<cCanvas.height+20) alive=true;
    cCtx.save(); cCtx.globalAlpha=Math.max(0,p.life);
    cCtx.translate(p.x,p.y); cCtx.rotate(p.r);
    cCtx.fillStyle=p.color;
    if (p.shape==='circle') { cCtx.beginPath(); cCtx.arc(0,0,p.w/2,0,Math.PI*2); cCtx.fill(); }
    else { cCtx.fillRect(-p.w/2,-p.h/2,p.w,p.h); }
    cCtx.restore();
  });
  if (alive) cAnimId=requestAnimationFrame(animConf); else stopConfetti();
}
function stopConfetti() { cancelAnimationFrame(cAnimId); cCanvas.style.display='none'; cCtx.clearRect(0,0,cCanvas.width,cCanvas.height); }

// ── TOAST ──
function toast(msg, icon='ℹ️') {
  const t=document.createElement('div');
  t.style.cssText='position:fixed;bottom:30px;left:50%;transform:translateX(-50%);background:var(--text);color:var(--card);padding:11px 22px;border-radius:12px;font-family:Instrument Sans,sans-serif;font-weight:700;font-size:.88rem;z-index:9999;box-shadow:0 8px 28px rgba(0,0,0,.22);animation:popIn .3s;white-space:nowrap;';
  t.textContent=`${icon} ${msg}`;
  document.body.appendChild(t); setTimeout(()=>t.remove(),2800);
}

// ── DARK MODE ──
const _tb = document.getElementById('themeBtn');
if (_tb) {
  if (localStorage.getItem('theme')==='dark') { document.body.classList.add('dark'); _tb.textContent='☀️'; }
  _tb.onclick = () => {
    document.body.classList.toggle('dark');
    const d = document.body.classList.contains('dark');
    localStorage.setItem('theme', d?'dark':'light');
    _tb.textContent = d ? '☀️' : '🌙';
  };
}

// ── KEYBOARD SHORTCUTS ──
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  if (e.code === 'Space') { e.preventDefault(); spinWheel(); }
  if (e.code === 'Escape') closeModal();
  if (e.code === 'KeyF') fullscreenWheel();
  if (e.code === 'KeyS') shuffleEntries();
});

// Settings listeners
document.getElementById('spinSpeedRange')?.addEventListener('input', e => { settings.speed = parseInt(e.target.value); saveSettings(); });
document.getElementById('volumeRange')?.addEventListener('input', e => { settings.volume = parseFloat(e.target.value); saveSettings(); });
document.getElementById('soundThemeSelect')?.addEventListener('change', e => { settings.soundTheme = e.target.value; saveSettings(); });

window.addEventListener('resize', () => { cCanvas.width=window.innerWidth; cCanvas.height=window.innerHeight; });

// ── INIT ──
buildPalette();
loadSettings();
loadFromURL();
if (!entries.length) loadFromLocalStorage();
if (!entries.length) loadExample();
updateSavedWheelsList();
renderHistory();
updateCountDisplay();
