import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="지오메트리 대쉬 디럭스", layout="wide")

game_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Geometry Dash Deluxe</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #0d0e15;
      color: #fff;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      overflow: hidden;
      user-select: none;
    }
    #game-container {
      position: relative;
      width: 800px;
      height: 400px;
      box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);
      border-radius: 10px;
      overflow: hidden;
      margin: 20px auto;
    }
    canvas {
      display: block;
      background: #111;
      cursor: pointer;
    }
    /* 로비 UI Overlay */
    #lobby-overlay {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(10, 10, 20, 0.88);
      backdrop-filter: blur(8px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 10;
    }
    #lobby-overlay h1 {
      font-size: 2.8rem;
      margin-bottom: 25px;
      color: #fff;
      text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 40px #00ffff;
      letter-spacing: 2px;
    }
    .stage-container {
      display: flex;
      gap: 20px;
    }
    .stage-card {
      background: rgba(255, 255, 255, 0.05);
      border: 2px solid #00ffff;
      border-radius: 12px;
      padding: 20px;
      width: 180px;
      text-align: center;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    .stage-card:hover {
      transform: translateY(-8px) scale(1.05);
      background: rgba(0, 255, 255, 0.2);
      box-shadow: 0 0 20px #00ffff;
    }
    .stage-title { font-size: 1.4rem; font-weight: bold; margin-bottom: 10px; }
    .stage-desc { font-size: 0.85rem; color: #ccc; line-height: 1.3; }
    .info { font-size: 13px; color: #8a8ab0; margin-top: 10px; text-align: center; }
  </style>
</head>
<body>

<div id="game-container">
  <canvas id="canvas" width="800" height="400"></canvas>
  
  <!-- 로비 화면 -->
  <div id="lobby-overlay">
    <h1>GEOMETRY DASH</h1>
    <div class="stage-container">
      <div class="stage-card" onclick="startStage(1)">
        <div class="stage-title" style="color: #00ffff;">STAGE 1</div>
        <div class="stage-desc">기본 큐브 &<br>비행기 모드</div>
      </div>
      <div class="stage-card" onclick="startStage(2)" style="border-color: #ff00ff;">
        <div class="stage-title" style="color: #ff00ff;">STAGE 2</div>
        <div class="stage-desc">중력 반전<br>볼(Ball) 모드</div>
      </div>
      <div class="stage-card" onclick="startStage(3)" style="border-color: #ffff00;">
        <div class="stage-title" style="color: #ffff00;">STAGE 3</div>
        <div class="stage-desc">초고속 지그재그<br>웨이브(Wave) 모드</div>
      </div>
    </div>
    <div class="info" style="margin-top:25px;">💡 원하시는 단계를 클릭하여 게임을 시작하세요!</div>
  </div>
</div>

<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const lobbyOverlay = document.getElementById('lobby-overlay');

let gameState = 'LOBBY';
let currentStage = 1;
let isHolding = false;
let cameraShake = 0;

const player = {
  x: 100, y: 300, size: 30, vy: 0, vx: 5, rotation: 0,
  mode: 'CUBE', gravityDir: 1, isGrounded: false, trail: []
};

let particles = [];
let obstacles = [];
let portals = [];

function createExplosion(x, y, color) {
  for (let i = 0; i < 30; i++) {
    particles.push({
      x: x, y: y,
      vx: (Math.random() - 0.5) * 12,
      vy: (Math.random() - 0.5) * 12,
      size: Math.random() * 6 + 2, color: color, life: 1.0
    });
  }
}

function loadLevel(stage) {
  obstacles = []; portals = [];
  if (stage === 1) {
    obstacles = [
      { x: 500, y: 340, w: 30, h: 30, type: 'SPIKE' },
      { x: 800, y: 340, w: 30, h: 30, type: 'SPIKE' },
      { x: 1100, y: 310, w: 60, h: 60, type: 'BLOCK' },
      { x: 1600, y: 340, w: 30, h: 30, type: 'SPIKE' }
    ];
    portals = [
      { x: 1300, y: 250, targetMode: 'SHIP' },
      { x: 2200, y: 250, targetMode: 'CUBE' }
    ];
  } else if (stage === 2) {
    portals = [
      { x: 400, y: 250, targetMode: 'BALL' },
      { x: 1500, y: 250, targetMode: 'SHIP' }
    ];
    obstacles = [
      { x: 700, y: 340, w: 30, h: 30, type: 'SPIKE' },
      { x: 1000, y: 30, w: 30, h: 30, type: 'SPIKE_CEIL' },
      { x: 1200, y: 340, w: 30, h: 30, type: 'SPIKE' }
    ];
  } else if (stage === 3) {
    portals = [ { x: 300, y: 250, targetMode: 'WAVE' } ];
    obstacles = [
      { x: 600, y: 300, w: 40, h: 100, type: 'BLOCK' },
      { x: 900, y: 0, w: 40, h: 150, type: 'BLOCK' },
      { x: 1200, y: 250, w: 40, h: 150, type: 'BLOCK' }
    ];
  }
}

function startStage(stageNum) {
  currentStage = stageNum;
  resetGame();
  loadLevel(stageNum);
  lobbyOverlay.style.display = 'none';
  gameState = 'PLAYING';
  requestAnimationFrame(gameLoop);
}

function resetGame() {
  player.x = 100; player.y = 300; player.vy = 0; player.rotation = 0;
  player.mode = 'CUBE'; player.gravityDir = 1; player.trail = [];
  particles = [];
}

window.addEventListener('keydown', (e) => {
  if (e.code === 'Space' || e.code === 'ArrowUp') handlePress();
});
window.addEventListener('keyup', (e) => {
  if (e.code === 'Space' || e.code === 'ArrowUp') handleRelease();
});
canvas.addEventListener('mousedown', handlePress);
canvas.addEventListener('mouseup', handleRelease);

function handlePress() {
  if (gameState !== 'PLAYING') return;
  isHolding = true;
  if (player.mode === 'CUBE' && player.isGrounded) {
    player.vy = -12; player.isGrounded = false;
  } else if (player.mode === 'BALL' && player.isGrounded) {
    player.gravityDir *= -1; player.vy = player.gravityDir * 5; player.isGrounded = false;
  }
}

function handleRelease() { isHolding = false; }

function update() {
  if (gameState !== 'PLAYING') return;

  player.trail.push({ x: player.x, y: player.y, rotation: player.rotation, mode: player.mode });
  if (player.trail.length > 8) player.trail.shift();

  if (player.mode === 'CUBE') {
    player.vy += 0.7; player.y += player.vy;
    if (!player.isGrounded) player.rotation += 8;
    else player.rotation = Math.round(player.rotation / 90) * 90;

    if (player.y >= 340) { player.y = 340; player.vy = 0; player.isGrounded = true; }
  } else if (player.mode === 'SHIP') {
    player.vy += isHolding ? -0.6 : 0.6; player.y += player.vy;
    player.rotation = player.vy * 3;
    if (player.y > 340) { player.y = 340; player.vy = 0; }
    if (player.y < 30) { player.y = 30; player.vy = 0; }
  } else if (player.mode === 'BALL') {
    player.vy += 0.7 * player.gravityDir; player.y += player.vy;
    player.rotation += 5 * player.gravityDir;
    if (player.y >= 340) { player.y = 340; player.vy = 0; player.isGrounded = true; }
    if (player.y <= 30) { player.y = 30; player.vy = 0; player.isGrounded = true; }
  } else if (player.mode === 'WAVE') {
    player.vy = isHolding ? -8 : 8; player.y += player.vy;
    player.rotation = isHolding ? -45 : 45;
    if (player.y > 340 || player.y < 30) triggerGameOver();
  }

  obstacles.forEach(obs => obs.x -= player.vx);
  portals.forEach(p => p.x -= player.vx);

  portals.forEach(p => {
    if (Math.abs(p.x - player.x) < 20) {
      if (player.mode !== p.targetMode) {
        player.mode = p.targetMode;
        createExplosion(player.x, player.y, '#00ffff');
      }
    }
  });

  obstacles.forEach(obs => {
    if (
      player.x + player.size/2 > obs.x &&
      player.x - player.size/2 < obs.x + obs.w &&
      player.y + player.size/2 > obs.y &&
      player.y - player.size/2 < obs.y + obs.h
    ) {
      triggerGameOver();
    }
  });

  particles.forEach((p, index) => {
    p.x += p.vx; p.y += p.vy; p.life -= 0.03;
    if (p.life <= 0) particles.splice(index, 1);
  });

  if (cameraShake > 0) cameraShake *= 0.9;
}

function triggerGameOver() {
  cameraShake = 15;
  createExplosion(player.x, player.y, '#ff0055');
  gameState = 'GAMEOVER';
  setTimeout(() => { lobbyOverlay.style.display = 'flex'; }, 1000);
}

function draw() {
  ctx.save();
  if (cameraShake > 0.5) {
    ctx.translate((Math.random() - 0.5) * cameraShake, (Math.random() - 0.5) * cameraShake);
  }

  let bgGrad = ctx.createLinearGradient(0, 0, 0, canvas.height);
  bgGrad.addColorStop(0, '#0f0c20'); bgGrad.addColorStop(1, '#06040a');
  ctx.fillStyle = bgGrad; ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = '#00ffff'; ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(0, 370); ctx.lineTo(canvas.width, 370);
  ctx.moveTo(0, 30); ctx.lineTo(canvas.width, 30);
  ctx.stroke();

  player.trail.forEach((t, i) => {
    ctx.save(); ctx.translate(t.x, t.y);
    ctx.rotate((t.rotation * Math.PI) / 180);
    ctx.fillStyle = `rgba(0, 255, 255, ${i * 0.05})`;
    ctx.fillRect(-player.size/2, -player.size/2, player.size, player.size);
    ctx.restore();
  });

  if (gameState === 'PLAYING') {
    ctx.save(); ctx.translate(player.x, player.y);
    ctx.rotate((player.rotation * Math.PI) / 180);
    ctx.fillStyle = player.mode === 'WAVE' ? '#ffff00' : '#00ffff';
    ctx.shadowBlur = 15; ctx.shadowColor = ctx.fillStyle;

    if (player.mode === 'CUBE' || player.mode === 'BALL') {
      ctx.fillRect(-player.size/2, -player.size/2, player.size, player.size);
      ctx.strokeStyle = '#fff';
      ctx.strokeRect(-player.size/4, -player.size/4, player.size/2, player.size/2);
    } else if (player.mode === 'SHIP' || player.mode === 'WAVE') {
      ctx.beginPath(); ctx.moveTo(player.size/2, 0);
      ctx.lineTo(-player.size/2, -player.size/2);
      ctx.lineTo(-player.size/2, player.size/2);
      ctx.closePath(); ctx.fill();
    }
    ctx.restore();
  }

  obstacles.forEach(obs => {
    ctx.fillStyle = '#ff0055'; ctx.shadowBlur = 10; ctx.shadowColor = '#ff0055';
    if (obs.type === 'SPIKE') {
      ctx.beginPath(); ctx.moveTo(obs.x, obs.y + obs.h);
      ctx.lineTo(obs.x + obs.w / 2, obs.y); ctx.lineTo(obs.x + obs.w, obs.y + obs.h);
      ctx.fill();
    } else {
      ctx.fillRect(obs.x, obs.y, obs.w, obs.h);
    }
  });

  portals.forEach(p => {
    ctx.fillStyle = '#a000ff'; ctx.shadowBlur = 15; ctx.shadowColor = '#a000ff';
    ctx.fillRect(p.x, 30, 10, 340);
  });

  particles.forEach(p => {
    ctx.fillStyle = p.color; ctx.globalAlpha = p.life;
    ctx.fillRect(p.x, p.y, p.size, p.size);
  });
  ctx.globalAlpha = 1.0;

  ctx.restore();
}

function gameLoop() {
  update(); draw();
  if (gameState === 'PLAYING' || particles.length > 0) {
    requestAnimationFrame(gameLoop);
  }
}
</script>
</body>
</html>
"""

components.html(game_html, height=500)
