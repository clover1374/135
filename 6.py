import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="Geometry Dash - Human Playable", layout="centered")
    st.title("Geometry Dash Deluxe Edition")
    st.caption("🎮 [사람 조작 최적화] 히트박스 완화 & 반응 시간 확보 완전 패치")
    st.info("💡 **조작법**: [스페이스바 / 마우스 클릭] 점프, 비행기 상승, 거미 천장/바닥 반전")

    game_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                margin: 0;
                padding: 0;
                background-color: #030308;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                user-select: none;
            }
            #gameCanvas {
                border: 3px solid #00f0ff;
                background: #050510;
                box-shadow: 0 0 35px rgba(0, 240, 255, 0.3);
                cursor: pointer;
            }
            .ui-panel {
                color: #fff;
                margin-top: 12px;
                font-size: 18px;
                font-weight: bold;
                display: flex;
                gap: 20px;
            }
            .ui-badge {
                background: rgba(15, 15, 30, 0.85);
                padding: 6px 18px;
                border-radius: 8px;
                border: 1px solid #00f0ff;
                box-shadow: 0 0 12px rgba(0, 240, 255, 0.2);
            }
        </style>
    </head>
    <body>
        <canvas id="gameCanvas" width="800" height="450"></canvas>
        <div class="ui-panel">
            <div class="ui-badge">시도 횟수: <span id="attemptCnt" style="color:#00f0ff;">1</span></div>
            <div class="ui-badge">현재 모드: <span id="modeDisplay" style="color:#00f0ff;">CUBE</span></div>
            <div class="ui-badge">진행도: <span id="progressDisplay" style="color:#ff007f;">0%</span></div>
            <div class="ui-badge">획득 코인: <span id="coinDisplay" style="color:#ffd700;">0 / 4</span></div>
        </div>

        <audio id="bgm" loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        </audio>

        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            const bgm = document.getElementById("bgm");

            const SCREEN_WIDTH = 800;
            const SCREEN_HEIGHT = 450;
            const BLOCK_SIZE = 40;
            const GROUND_Y = SCREEN_HEIGHT - BLOCK_SIZE;
            const CEILING_Y = 40;

            // [사람 반응속도에 맞춘 속도와 중력 매개변수]
            const GRAVITY = 1.15;
            const JUMP_STRENGTH = -15.2;
            const SPEED = 5.8; // 사람의 반응속도에 맞춰 플레이 속도 약간 완화

            let attempts = 1;
            let isHolding = false;
            let animFrame = 0;
            let screenFlash = { alpha: 0, color: "#ffffff" };
            let deathTimer = 0;

            let shockwaves = [];
            let particles = [];
            let spiderTrails = [];

            let player = {
                x: 100,
                y: GROUND_Y - BLOCK_SIZE,
                vy: 0,
                angle: 0,
                isGrounded: false,
                isDead: false,
                isCleared: false,
                mode: "cube",
                spiderUpsideDown: false
            };

            let collectedCoinIds = new Set();

            function generateMap() {
                let map = [
                    // ===== 1. 초반 큐브 (여유로운 가시와 점프링) =====
                    {x: 25, type: 2, y: 0},
                    {x: 35, type: 1, y: 1}, 
                    {x: 40, type: 1, y: 2}, 
                    {x: 47, type: 2, y: 0},
                    {x: 58, type: 4, y: 2}, // 점프링 (여유로운 배치)
                    {x: 66, type: 1, y: 2}, {x: 67, type: 1, y: 2},
                    {x: 67, type: 3, y: 4, id: 1}, // 코인 1
                    {x: 78, type: 2, y: 0},
                    {x: 88, type: 1, y: 1},
                    {x: 96, type: 4, y: 2},

                    // ===== 2. 비행기 포탈 (X: 110) =====
                    {x: 110, type: 6, y: 0},

                    // ===== 3. 비행기 코스 (넓은 통로 배치) =====
                    {x: 128, type: 1, y: 0},
                    {x: 142, type: 1, y: 7},
                    {x: 156, type: 2, y: 0},
                    {x: 164, type: 3, y: 4, id: 2}, // 코인 2
                    {x: 175, type: 1, y: 1}, {x: 175, type: 1, y: 6},
                    {x: 190, type: 5, y: 8},

                    // ===== 4. 큐브 포탈 (X: 205) =====
                    {x: 205, type: 7, y: 0},

                    // ===== 5. 중간 큐브 코스 =====
                    {x: 220, type: 2, y: 0},
                    {x: 232, type: 1, y: 1}, 
                    {x: 242, type: 4, y: 2},
                    {x: 254, type: 1, y: 2},
                    {x: 264, type: 3, y: 4, id: 3}, // 코인 3
                    {x: 274, type: 2, y: 0}, 

                    // ===== 6. 거미 포탈 (X: 290) =====
                    {x: 290, type: 8, y: 0},

                    // ===== 7. 거미 코스 (충분한 반응 시간 부여) =====
                    {x: 308, type: 2, y: 0}, // 1차 반전 지점
                    {x: 326, type: 5, y: 8}, // 2차 반전 지점 (간격 대폭 확대)
                    {x: 338, type: 3, y: 8, id: 4}, // 코인 4
                    {x: 344, type: 2, y: 0}, // 3차 반전 지점
                    {x: 362, type: 5, y: 8},

                    // ===== 8. 최종 피날레 (X: 380) =====
                    {x: 380, type: 7, y: 0},
                    {x: 395, type: 2, y: 0},
                    {x: 408, type: 4, y: 2},
                    {x: 420, type: 1, y: 1}
                ];
                return map;
            }

            const STAGE_MAP = generateMap();
            const FINISH_LINE_X = 435 * BLOCK_SIZE;

            window.addEventListener("keydown", (e) => {
                if (e.code === "Space") {
                    e.preventDefault();
                    if (!isHolding) {
                        isHolding = true;
                        startBGM();
                        triggerSingleClick();
                    }
                }
            });

            window.addEventListener("keyup", (e) => {
                if (e.code === "Space") isHolding = false;
            });

            canvas.addEventListener("mousedown", () => {
                if (!isHolding) {
                    isHolding = true;
                    startBGM();
                    triggerSingleClick();
                }
            });

            window.addEventListener("mouseup", () => { isHolding = false; });

            function startBGM() {
                if (bgm.paused) {
                    bgm.volume = 0.3;
                    bgm.play().catch(() => {});
                }
            }

            function triggerSingleClick() {
                if (player.isDead || player.isCleared) return;

                if (player.mode === "spider" && player.isGrounded) {
                    let oldY = player.y;
                    player.spiderUpsideDown = !player.spiderUpsideDown;
                    player.y = player.spiderUpsideDown ? CEILING_Y : GROUND_Y - BLOCK_SIZE;
                    player.vy = 0;

                    spiderTrails.push({
                        x: player.x + BLOCK_SIZE/2,
                        startY: oldY + BLOCK_SIZE/2,
                        endY: player.y + BLOCK_SIZE/2,
                        alpha: 1.0
                    });

                    for(let i=0; i<16; i++) {
                        particles.push({
                            x: player.x + BLOCK_SIZE/2,
                            y: player.y + BLOCK_SIZE/2,
                            vx: (Math.random()-0.5)*16,
                            vy: (Math.random()-0.5)*16,
                            life: 1.0,
                            color: "#aa00ff"
                        });
                    }
                }
            }

            function processContinuousInput() {
                if (!isHolding || player.isDead || player.isCleared) return;

                if (player.mode === "cube") {
                    if (player.isGrounded) {
                        player.vy = JUMP_STRENGTH;
                        player.isGrounded = false;
                    } else {
                        STAGE_MAP.forEach(obj => {
                            if (obj.type === 4) {
                                let ringX = obj.x * BLOCK_SIZE;
                                let ringY = GROUND_Y - BLOCK_SIZE - (obj.y * BLOCK_SIZE);
                                let dist = Math.hypot((player.x + BLOCK_SIZE/2) - (ringX + BLOCK_SIZE/2), (player.y + BLOCK_SIZE/2) - (ringY + BLOCK_SIZE/2));
                                if (dist < BLOCK_SIZE * 3.0) { // 점프링 판정 대폭 확대
                                    player.vy = JUMP_STRENGTH;
                                    shockwaves.push({
                                        x: ringX + BLOCK_SIZE/2,
                                        y: ringY + BLOCK_SIZE/2,
                                        radius: 10,
                                        maxRadius: 45,
                                        alpha: 1.0
                                    });
                                }
                            }
                        });
                    }
                }
            }

            function killPlayer() {
                if (player.isDead) return;
                player.isDead = true;
                deathTimer = 25;

                for(let i=0; i<40; i++) {
                    let angle = Math.random() * Math.PI * 2;
                    let speed = Math.random() * 14 + 2;
                    particles.push({
                        x: player.x + BLOCK_SIZE/2,
                        y: player.y + BLOCK_SIZE/2,
                        vx: Math.cos(angle) * speed,
                        vy: Math.sin(angle) * speed,
                        life: 1.0,
                        color: Math.random() > 0.5 ? "#ff0055" : "#00f0ff"
                    });
                }
                screenFlash = { alpha: 0.8, color: "#ff0055" };
            }

            function resetGame() {
                player.x = 100;
                player.y = GROUND_Y - BLOCK_SIZE;
                player.vy = 0;
                player.angle = 0;
                player.isGrounded = false;
                player.isDead = false;
                player.isCleared = false;
                player.mode = "cube";
                player.spiderUpsideDown = false;
                collectedCoinIds.clear();
                document.getElementById("coinDisplay").innerText = "0 / 4";
                shockwaves = [];
                particles = [];
                spiderTrails = [];
                updateModeUI();
            }

            function updateModeUI() {
                const modeEl = document.getElementById("modeDisplay");
                if (player.mode === "cube") {
                    modeEl.innerText = "CUBE"; modeEl.style.color = "#00f0ff";
                } else if (player.mode === "ship") {
                    modeEl.innerText = "SHIP"; modeEl.style.color = "#ff007f";
                } else if (player.mode === "spider") {
                    modeEl.innerText = "SPIDER"; modeEl.style.color = "#aa00ff";
                }
            }

            function update() {
                animFrame++;

                if (screenFlash.alpha > 0) screenFlash.alpha -= 0.05;

                let prog = Math.min(100, Math.floor((player.x / FINISH_LINE_X) * 100));
                document.getElementById("progressDisplay").innerText = prog + "%";

                particles.forEach((p, idx) => {
                    p.x += p.vx;
                    p.y += p.vy;
                    p.life -= 0.04;
                    if (p.life <= 0) particles.splice(idx, 1);
                });

                if (player.isCleared) return;

                if (player.isDead) {
                    deathTimer--;
                    if (deathTimer <= 0) {
                        attempts++;
                        document.getElementById("attemptCnt").innerText = attempts;
                        resetGame();
                    }
                    return;
                }

                processContinuousInput();

                player.x += SPEED;
                if (player.x >= FINISH_LINE_X) {
                    player.x = FINISH_LINE_X;
                    player.isCleared = true;
                    return;
                }

                if (player.mode === "cube") {
                    player.vy += GRAVITY;
                    player.y += player.vy;

                    if (player.y >= GROUND_Y - BLOCK_SIZE) {
                        player.y = GROUND_Y - BLOCK_SIZE;
                        player.vy = 0;
                        player.isGrounded = true;
                    } else {
                        player.isGrounded = false;
                    }

                    if (!player.isGrounded) {
                        player.angle += 9;
                    } else {
                        player.angle = Math.round(player.angle / 90) * 90;
                    }
                } 
                else if (player.mode === "ship") {
                    if (isHolding) player.vy -= 0.65;
                    else player.vy += 0.55;

                    player.vy = Math.max(-5.5, Math.min(5.5, player.vy));
                    player.y += player.vy;
                    player.angle = player.vy * 3.0;

                    if (player.y <= CEILING_Y) {
                        player.y = CEILING_Y;
                        player.vy = 0;
                    }
                    
                    if (player.y >= GROUND_Y - BLOCK_SIZE) {
                        player.y = GROUND_Y - BLOCK_SIZE;
                        player.vy = 0;
                    }

                    if (animFrame % 2 === 0) {
                        particles.push({
                            x: player.x - 12,
                            y: player.y + BLOCK_SIZE/2,
                            vx: -SPEED * 0.5,
                            vy: (Math.random()-0.5)*3,
                            life: 0.8,
                            color: isHolding ? "#00f0ff" : "#ff007f"
                        });
                    }
                }
                else if (player.mode === "spider") {
                    player.angle = 0;
                    let targetY = player.spiderUpsideDown ? CEILING_Y : GROUND_Y - BLOCK_SIZE;
                    player.y = targetY;
                    player.isGrounded = true;
                }

                shockwaves.forEach((sw, idx) => {
                    sw.radius += 3.5;
                    sw.alpha -= 0.05;
                    if (sw.alpha <= 0 || sw.radius >= sw.maxRadius) shockwaves.splice(idx, 1);
                });

                spiderTrails.forEach((st, idx) => {
                    st.alpha -= 0.1;
                    if (st.alpha <= 0) spiderTrails.splice(idx, 1);
                });

                // ★ 사람 조작용 판정 박스 (내부 60% 영역만 인정하여 억울한 죽음 완전 제거) ★
                let pBox = {
                    x: player.x + 12,
                    y: player.y + 12,
                    w: BLOCK_SIZE - 24,
                    h: BLOCK_SIZE - 24
                };

                let onBlock = false;

                STAGE_MAP.forEach(obj => {
                    let objX = obj.x * BLOCK_SIZE;
                    let objY = GROUND_Y - BLOCK_SIZE - (obj.y * BLOCK_SIZE);
                    let oBox = {x: objX, y: objY, w: BLOCK_SIZE, h: BLOCK_SIZE};

                    if (pBox.x < oBox.x + oBox.w && pBox.x + pBox.w > oBox.x &&
                        pBox.y < oBox.y + oBox.h && pBox.y + pBox.h > oBox.y) {

                        if (obj.type === 2 || obj.type === 5) {
                            killPlayer();
                        }
                        else if (obj.type === 1) {
                            let prevY = player.y - player.vy;
                            if (prevY + BLOCK_SIZE <= oBox.y + 22 && player.vy >= 0 && !player.spiderUpsideDown) {
                                player.y = oBox.y - BLOCK_SIZE;
                                player.vy = 0;
                                onBlock = true;
                            } else {
                                killPlayer();
                            }
                        }
                        else if (obj.type === 3 && !collectedCoinIds.has(obj.id)) {
                            collectedCoinIds.add(obj.id);
                            document.getElementById("coinDisplay").innerText = collectedCoinIds.size + " / 4";
                            for(let i=0; i<15; i++) {
                                particles.push({
                                    x: objX + BLOCK_SIZE/2, y: objY + BLOCK_SIZE/2,
                                    vx: (Math.random()-0.5)*12, vy: (Math.random()-0.5)*12,
                                    life: 1.0, color: "#ffd700"
                                });
                            }
                        }
                        else if (obj.type === 6 && player.mode !== "ship") {
                            player.mode = "ship"; player.vy = 0;
                            screenFlash = { alpha: 0.6, color: "#ff007f" };
                            createPortalBurst(objX, objY, "#ff007f");
                            updateModeUI();
                        }
                        else if (obj.type === 7 && player.mode !== "cube") {
                            player.mode = "cube"; player.vy = 0;
                            screenFlash = { alpha: 0.6, color: "#00f0ff" };
                            createPortalBurst(objX, objY, "#00f0ff");
                            updateModeUI();
                        }
                        else if (obj.type === 8 && player.mode !== "spider") {
                            player.mode = "spider"; player.spiderUpsideDown = false;
                            player.y = GROUND_Y - BLOCK_SIZE; player.vy = 0;
                            screenFlash = { alpha: 0.6, color: "#aa00ff" };
                            createPortalBurst(objX, objY, "#aa00ff");
                            updateModeUI();
                        }
                    }
                });

                if (onBlock && player.mode === "cube") player.isGrounded = true;
            }

            function createPortalBurst(x, y, color) {
                for(let i=0; i<20; i++) {
                    let angle = Math.random() * Math.PI * 2;
                    let speed = Math.random() * 10 + 3;
                    particles.push({
                        x: x + BLOCK_SIZE/2, y: y + BLOCK_SIZE/2,
                        vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed,
                        life: 1.0, color: color
                    });
                }
            }

            function draw() {
                ctx.clearRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
                let cameraX = player.x - 120;

                let grad = ctx.createLinearGradient(0, 0, 0, SCREEN_HEIGHT);
                if (player.mode === "ship") {
                    grad.addColorStop(0, '#0a0017'); grad.addColorStop(1, '#2a0036');
                } else if (player.mode === "spider") {
                    grad.addColorStop(0, '#12001f'); grad.addColorStop(1, '#3b0054');
                } else {
                    grad.addColorStop(0, '#020b14'); grad.addColorStop(1, '#082136');
                }
                ctx.fillStyle = grad;
                ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);

                ctx.strokeStyle = "rgba(0, 240, 255, 0.08)";
                ctx.lineWidth = 1;
                let gridOffset = (cameraX * 0.3) % 40;
                for (let x = -gridOffset; x < SCREEN_WIDTH; x += 40) {
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, SCREEN_HEIGHT); ctx.stroke();
                }

                ctx.fillStyle = "#010408";
                ctx.fillRect(0, GROUND_Y, SCREEN_WIDTH, BLOCK_SIZE);
                ctx.fillRect(0, 0, SCREEN_WIDTH, CEILING_Y);
                
                ctx.strokeStyle = player.mode === "ship" ? "#ff007f" : (player.mode === "spider" ? "#aa00ff" : "#00f0ff");
                ctx.shadowColor = ctx.strokeStyle;
                ctx.shadowBlur = 12;
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(0, GROUND_Y); ctx.lineTo(SCREEN_WIDTH, GROUND_Y);
                ctx.moveTo(0, CEILING_Y); ctx.lineTo(SCREEN_WIDTH, CEILING_Y);
                ctx.stroke();
                ctx.shadowBlur = 0;

                spiderTrails.forEach(st => {
                    let stX = st.x - cameraX;
                    ctx.save();
                    ctx.strokeStyle = `rgba(170, 0, 255, ${st.alpha})`;
                    ctx.shadowColor = "#aa00ff"; ctx.shadowBlur = 15;
                    ctx.lineWidth = 6;
                    ctx.beginPath();
                    ctx.moveTo(stX, st.startY); ctx.lineTo(stX, st.endY);
                    ctx.stroke(); ctx.restore();
                });

                shockwaves.forEach(sw => {
                    let swX = sw.x - cameraX;
                    ctx.save();
                    ctx.strokeStyle = `rgba(255, 230, 0, ${sw.alpha})`;
                    ctx.shadowColor = "#ffe600"; ctx.shadowBlur = 10;
                    ctx.lineWidth = 3;
                    ctx.beginPath();
                    ctx.arc(swX, sw.y, sw.radius, 0, Math.PI * 2);
                    ctx.stroke(); ctx.restore();
                });

                STAGE_MAP.forEach(obj => {
                    let screenX = obj.x * BLOCK_SIZE - cameraX;
                    let screenY = GROUND_Y - BLOCK_SIZE - (obj.y * BLOCK_SIZE);

                    if (screenX >= -BLOCK_SIZE * 2 && screenX <= SCREEN_WIDTH + BLOCK_SIZE) {
                        if (obj.type === 1) {
                            ctx.save();
                            ctx.fillStyle = "#090d16";
                            ctx.fillRect(screenX, screenY, BLOCK_SIZE, BLOCK_SIZE);
                            ctx.strokeStyle = "#00f0ff";
                            ctx.shadowColor = "#00f0ff"; ctx.shadowBlur = 8;
                            ctx.lineWidth = 2;
                            ctx.strokeRect(screenX, screenY, BLOCK_SIZE, BLOCK_SIZE);
                            ctx.strokeStyle = "rgba(0, 240, 255, 0.3)";
                            ctx.beginPath();
                            ctx.moveTo(screenX, screenY); ctx.lineTo(screenX + BLOCK_SIZE, screenY + BLOCK_SIZE);
                            ctx.moveTo(screenX + BLOCK_SIZE, screenY); ctx.lineTo(screenX, screenY + BLOCK_SIZE);
                            ctx.stroke();
                            ctx.restore();
                        }
                        else if (obj.type === 2) {
                            ctx.save();
                            ctx.fillStyle = "#1a000a"; ctx.strokeStyle = "#ff0055";
                            ctx.shadowColor = "#ff0055"; ctx.shadowBlur = 10; ctx.lineWidth = 2;
                            ctx.beginPath();
                            ctx.moveTo(screenX + BLOCK_SIZE/2, screenY + 6);
                            ctx.lineTo(screenX + 6, screenY + BLOCK_SIZE);
                            ctx.lineTo(screenX + BLOCK_SIZE - 6, screenY + BLOCK_SIZE);
                            ctx.closePath(); ctx.fill(); ctx.stroke();
                            ctx.restore();
                        }
                        else if (obj.type === 5) {
                            ctx.save();
                            ctx.fillStyle = "#1a000a"; ctx.strokeStyle = "#ff0055";
                            ctx.shadowColor = "#ff0055"; ctx.shadowBlur = 10; ctx.lineWidth = 2;
                            ctx.beginPath();
                            ctx.moveTo(screenX + 6, screenY);
                            ctx.lineTo(screenX + BLOCK_SIZE - 6, screenY);
                            ctx.lineTo(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE - 6);
                            ctx.closePath(); ctx.fill(); ctx.stroke();
                            ctx.restore();
                        }
                        else if (obj.type === 3 && !collectedCoinIds.has(obj.id)) {
                            let pulse = Math.sin(animFrame * 0.1) * 2;
                            ctx.save();
                            ctx.shadowColor = "#ffd700"; ctx.shadowBlur = 15;
                            ctx.fillStyle = "#ffd700";
                            ctx.beginPath();
                            ctx.arc(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 13 + pulse, 0, Math.PI * 2);
                            ctx.fill(); ctx.restore();
                        }
                        else if (obj.type === 4) {
                            ctx.save();
                            ctx.shadowColor = "#ffe600"; ctx.shadowBlur = 12;
                            ctx.strokeStyle = "#ffe600"; ctx.lineWidth = 3;
                            ctx.beginPath();
                            ctx.arc(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 16, 0, Math.PI * 2);
                            ctx.stroke();
                            ctx.fillStyle = "#ffffff"; ctx.beginPath();
                            ctx.arc(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 7, 0, Math.PI * 2);
                            ctx.fill(); ctx.restore();
                        }
                        else if (obj.type === 6 || obj.type === 7 || obj.type === 8) {
                            let portalColor = obj.type === 6 ? "#ff007f" : (obj.type === 7 ? "#00f0ff" : "#aa00ff");
                            ctx.save();
                            ctx.shadowColor = portalColor; ctx.shadowBlur = 20;
                            ctx.strokeStyle = portalColor; ctx.lineWidth = 5;
                            ctx.beginPath();
                            ctx.ellipse(screenX + BLOCK_SIZE/2, GROUND_Y - (SCREEN_HEIGHT - CEILING_Y - BLOCK_SIZE)/2, 20, (SCREEN_HEIGHT - CEILING_Y - BLOCK_SIZE)/2 - 5, 0, 0, Math.PI * 2);
                            ctx.stroke(); ctx.restore();
                        }
                    }
                });

                let finishX = FINISH_LINE_X - cameraX;
                if (finishX >= -BLOCK_SIZE && finishX <= SCREEN_WIDTH) {
                    ctx.save();
                    ctx.fillStyle = "#00f0ff"; ctx.shadowColor = "#00f0ff"; ctx.shadowBlur = 20;
                    ctx.fillRect(finishX, 0, 12, GROUND_Y);
                    ctx.restore();
                }

                particles.forEach(p => {
                    let pX = p.x - cameraX;
                    ctx.save();
                    ctx.fillStyle = p.color; ctx.globalAlpha = p.life;
                    ctx.fillRect(pX, p.y, 4, 4);
                    ctx.restore();
                });

                if (!player.isDead) {
                    ctx.save();
                    ctx.translate(120 + BLOCK_SIZE/2, player.y + BLOCK_SIZE/2);
                    ctx.rotate((player.angle * Math.PI) / 180);

                    if (player.mode === "cube") {
                        let cGrad = ctx.createLinearGradient(-20, -20, 20, 20);
                        cGrad.addColorStop(0, "#00f0ff"); cGrad.addColorStop(1, "#0077ff");
                        ctx.fillStyle = cGrad;
                        ctx.fillRect(-BLOCK_SIZE/2, -BLOCK_SIZE/2, BLOCK_SIZE, BLOCK_SIZE);
                        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2.5;
                        ctx.strokeRect(-BLOCK_SIZE/2, -BLOCK_SIZE/2, BLOCK_SIZE, BLOCK_SIZE);
                        
                        ctx.fillStyle = "#000000";
                        ctx.fillRect(-12, -8, 24, 10);
                        ctx.fillStyle = "#00f0ff";
                        ctx.fillRect(-9, -6, 8, 6); ctx.fillRect(1, -6, 8, 6);
                    } 
                    else if (player.mode === "ship") {
                        ctx.fillStyle = "#ff007f";
                        ctx.beginPath();
                        ctx.moveTo(20, 0); ctx.lineTo(-15, -12); ctx.lineTo(-15, 12);
                        ctx.closePath(); ctx.fill();
                        
                        ctx.fillStyle = "#00f0ff";
                        ctx.beginPath();
                        ctx.ellipse(2, -3, 8, 5, 0, 0, Math.PI*2);
                        ctx.fill();

                        ctx.fillStyle = "#b5005b";
                        ctx.beginPath();
                        ctx.moveTo(-2, 0); ctx.lineTo(-14, -18); ctx.lineTo(-6, 0);
                        ctx.closePath(); ctx.fill();

                        ctx.fillStyle = "#ffcc00";
                        ctx.fillRect(-20, -5, 5, 10);
                    } 
                    else if (player.mode === "spider") {
                        let legOffset = Math.sin(animFrame * 0.5) * 5;
                        ctx.fillStyle = "#aa00ff";
                        ctx.beginPath(); ctx.arc(0, 0, 14, 0, Math.PI * 2); ctx.fill();
                        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2; ctx.stroke();
                        
                        ctx.strokeStyle = "#aa00ff"; ctx.lineWidth = 3;
                        for (let i = -1; i <= 1; i += 2) {
                            ctx.beginPath();
                            ctx.moveTo(i * 6, 0); ctx.lineTo(i * 16, 14 + legOffset);
                            ctx.moveTo(i * 6, -4); ctx.lineTo(i * 14, -14 - legOffset);
                            ctx.stroke();
                        }
                    }
                    ctx.restore();
                }

                if (screenFlash.alpha > 0) {
                    ctx.fillStyle = screenFlash.color;
                    ctx.globalAlpha = screenFlash.alpha;
                    ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
                    ctx.globalAlpha = 1.0;
                }

                if (player.isCleared) {
                    ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
                    ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
                    ctx.fillStyle = "#00f0ff"; ctx.font = "bold 42px Arial"; ctx.textAlign = "center";
                    ctx.shadowColor = "#00f0ff"; ctx.shadowBlur = 15;
                    ctx.fillText("STAGE CLEARED!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 10);
                    ctx.fillStyle = "#ffd700"; ctx.font = "bold 24px Arial";
                    ctx.fillText("ALL COINS COLLECTED: " + collectedCoinIds.size + " / 4", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 35);
                }
            }

            function gameLoop() {
                update();
                draw();
                requestAnimationFrame(gameLoop);
            }

            gameLoop();
        </script>
    </body>
    </html>
    """

    components.html(game_html, height=550)

if __name__ == "__main__":
    main()
