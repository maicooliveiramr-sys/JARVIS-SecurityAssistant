* {
  box-sizing: border-box;
}

:root {
  --bg: #040b16;
  --panel: rgba(12, 25, 38, 0.8);
  --panel-strong: rgba(17, 34, 52, 0.95);
  --line: rgba(124, 230, 255, 0.3);
  --cyan: #7ee7ff;
  --blue: #4bb3ff;
  --green: #9ff9c4;
  --text: #eaf9ff;
  --muted: #b7d4e5;
}

html, body, #root {
  margin: 0;
  min-height: 100%;
  height: 100%;
  font-family: 'Segoe UI', sans-serif;
  background: radial-gradient(circle at top, #0a1830 0%, var(--bg) 40%, #02070d 100%);
  color: var(--text);
}

body {
  min-height: 100vh;
}

button, input {
  font: inherit;
}

.app-shell {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  padding: 24px;
}

.background-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(126, 231, 255, 0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(126, 231, 255, 0.08) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: radial-gradient(circle at center, black, transparent 75%);
}

.topbar, .dashboard {
  position: relative;
  z-index: 1;
}

.topbar {
  max-width: 1200px;
  margin: 0 auto 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 18px var(--green);
}

.brand {
  letter-spacing: 0.3rem;
  color: var(--cyan);
  font-weight: 700;
}

.status-pill {
  padding: 8px 14px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(29, 87, 112, 0.2);
  color: var(--green);
  font-size: 0.75rem;
  letter-spacing: 0.1rem;
}

.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 20px;
}

.panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  box-shadow: 0 0 25px rgba(25, 135, 200, 0.15);
  overflow: hidden;
}

.hero-panel {
  display: grid;
  grid-template-columns: 260px 1fr;
  padding: 24px;
  min-height: 280px;
}

.avatar-zone {
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar-core {
  position: relative;
  width: 180px;
  height: 180px;
  display: grid;
  place-items: center;
}

.avatar-ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px solid rgba(126, 231, 255, 0.6);
  box-shadow: 0 0 18px rgba(126, 231, 255, 0.3);
}

.ring-1 {
  transform: scale(1.1);
}

.ring-2 {
  transform: scale(1.25);
  animation: pulse 2.8s infinite ease-in-out;
}

.avatar-face {
  position: relative;
  z-index: 2;
  width: 104px;
  height: 104px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: linear-gradient(180deg, rgba(125, 225, 255, 0.3), rgba(75, 179, 255, 0.12));
  border: 1px solid rgba(126, 231, 255, 0.4);
  box-shadow: inset 0 0 30px rgba(126, 231, 255, 0.15), 0 0 30px rgba(126, 231, 255, 0.15);
  font-size: 2.5rem;
  font-weight: 700;
}

.hero-copy {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.label {
  color: var(--cyan);
  letter-spacing: 0.18rem;
  text-transform: uppercase;
  margin: 0 0 10px;
  font-size: 0.72rem;
}

.hero-copy h1 {
  margin: 0;
  font-size: clamp(2.8rem, 5vw, 5rem);
  letter-spacing: 0.2rem;
}

.subtitle {
  margin-top: 18px;
  max-width: 560px;
  color: var(--muted);
  line-height: 1.6;
}

.control-panel, .response-panel {
  padding: 20px;
}

.control-panel {
  grid-column: 1 / 2;
}

.response-panel {
  grid-column: 2 / 3;
  grid-row: 2;
}

.input-row {
  display: flex;
  gap: 12px;
}

.input-row input {
  flex: 1;
  background: rgba(3, 14, 22, 0.9);
  border: 1px solid var(--line);
  border-radius: 12px;
  color: var(--text);
  padding: 14px 16px;
  outline: none;
}

.input-row button,
.quick-actions button {
  background: linear-gradient(180deg, #53c9ff, #1d78c8);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 12px 18px;
  cursor: pointer;
  transition: transform 0.2s ease, filter 0.2s ease;
}

.input-row button:hover,
.quick-actions button:hover {
  transform: translateY(-1px);
  filter: brightness(1.08);
}

.quick-actions {
  display: flex;
  gap: 10px;
  margin-top: 16px;
  flex-wrap: wrap;
}

.response-panel h3 {
  margin: 0 0 12px;
  color: var(--cyan);
}

.response-panel pre {
  margin: 0;
  padding: 14px;
  border-radius: 12px;
  background: rgba(2, 10, 16, 0.9);
  border: 1px solid var(--line);
  color: var(--muted);
  white-space: pre-wrap;
  word-break: break-word;
  min-height: 180px;
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.6;
    transform: scale(1.2);
  }
  50% {
    opacity: 1;
    transform: scale(1.35);
  }
}

@media (max-width: 900px) {
  .dashboard {
    grid-template-columns: 1fr;
  }

  .response-panel {
    grid-column: auto;
    grid-row: auto;
  }

  .hero-panel {
    grid-template-columns: 1fr;
  }
}
