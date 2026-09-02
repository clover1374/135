import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="Geometry Dash Deluxe Hardcore", layout="centered")
    st.title("Geometry Dash Deluxe Edition")
    st.caption("속도 감소 / 점프력 증가 / 비행기·거미 난이도 패치 / 포탈 우회 완전 차단 적용 완료")
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

            // [패치] 속도를 5.5로 낮추고 점프력을 -18.5로 높임
            const GRAVITY = 1.30;
            const JUMP_STRENGTH = -18.5;
            const SPEED = 5.5; 

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

            // 타입 명세: 1: 블록, 2: 바닥가시, 3: 코인, 4: 점프링, 5: 천장가시, 6: 비행기포탈, 7: 큐브포탈, 8: 거미포탈
            function generateMap() {
                let map = [
                    // ================= 1. 초반 큐브 구간 (높아진 점프력 맞춤 정밀 재배치) =================
                    {x: 20, type: 2, y: 0},
                    
                    // 점프가 높으므로 블록 높이를 올리고 넓게 배치
                    {x: 28, type: 1, y: 1}, 
                    {x: 33, type: 1, y: 2}, 
                    {x: 34, type: 2, y: 3}, // 블록 위 가시
                    {x: 38, type: 2, y: 0}, {x: 39, type: 2, y: 0}, // 연속 가시

                    {x: 46, type: 4, y: 3}, // 고고도 점프링
                    {x: 53, type: 1, y: 3}, {x: 54, type: 1, y: 3},
                    {x: 54, type: 3, y: 5, id: 1}, // 코인 1
                    {x: 62, type: 2, y: 0}, {x: 63, type: 2, y: 0}, {x: 64, type: 2, y: 0}, // 3연 가시

                    {x: 72, type: 1, y: 2},
                    {x: 77, type: 4, y: 3},
                    {x: 84, type: 2, y: 0}, {x: 85, type: 2, y: 0},

                    // ================= 2. 비행기 포탈 벽 및 차단막 (X: 95) =================
                    // 포탈 우회 완전 차단: 포탈 높이(y=2)를 제외한 모든 Y축에 블록 벽 설치
                    {x: 95, type: 1, y: 0},
                    {x: 95, type: 1, y: 1},
                    {x: 95, type: 6, y: 2}, // 포탈
                    {x: 95, type: 1, y: 3},
                    {x: 95, type: 1, y: 4},
                    {x: 95, type: 1, y: 5},
                    {x: 95, type: 1, y: 6},
                    {x: 95, type: 1, y: 7},

                    // ================= 3. 비행기 코스 (손떼기 방지 정밀 난이도 패치) =================
                    // 바닥/천장 가시 및 정교한 고도 조율 필요한 기둥배치
                    {x: 108, type: 1, y: 0}, {x: 108, type: 1, y: 1}, {x: 108, type: 1, y: 2}, {x: 108, type: 1, y: 3}, // 아래 막기
                    {x: 118, type: 1, y: 5}, {x: 118, type: 1, y: 6}, {x: 118, type: 1, y: 7}, {x: 118, type: 1, y: 8}, // 위 막기
                    
                    {x: 128, type: 2, y: 0}, {x: 128, type: 5, y: 8},
                    {x: 132, type: 1, y: 3}, {x: 132, type: 1, y: 4}, // 중앙 장애물 (고도 조절 필수)
                    {x: 132, type: 3, y: 1, id: 2}, // 코인 2

                    {x: 144, type: 1, y: 0}, {x: 144, type: 1, y: 1}, {x: 144, type: 1, y: 2}, {x: 144, type: 1, y: 6}, {x: 144, type: 1, y: 7},
                    {x: 156, type: 1, y: 4}, {x: 156, type: 1, y: 5}, {x: 156, type: 1, y: 6},
                    {x: 168, type: 2, y: 0}, {x: 168, type: 5, y: 8},
                    {x: 178, type: 1, y: 1}, {x: 178, type: 1, y: 2}, {x: 178, type: 1, y: 3},

                    // ================= 4. 큐브 포탈 벽 및 차단막 (X: 190) =================
                    {x: 190, type: 1, y: 0},
                    {x: 190, type: 7, y: 1}, // 큐브 포탈
                    {x: 190, type: 1, y: 2},
                    {x: 190, type: 1, y: 3},
                    {x: 190, type: 1, y: 4},
                    {x: 190, type: 1, y: 5},
                    {x: 190, type: 1, y: 6},
                    {x: 190, type: 1, y: 7},

                    // ================= 5. 중간 큐브 코스 (하드코어) =================
                    {x: 202, type: 2, y: 0}, {x: 203, type: 2, y: 0},
                    {x: 212, type: 1, y: 2}, 
                    {x: 218, type: 4, y: 3},
                    {x: 226, type: 1, y: 3}, {x: 227, type: 2, y: 4},
                    {x: 235, type: 2, y: 0}, {x: 236, type: 2, y: 0}, {x: 237, type: 2, y: 0},
                    {x: 245, type: 3, y: 4, id: 3}, // 코인 3
                    {x: 252, type: 4, y: 2}, 
                    {x: 260, type: 1, y: 2},

                    // ================= 6. 거미 포탈 벽 및 차단막 (X: 275) =================
                    {x: 275, type: 8, y: 0}, // 거미 포탈
                    {x: 275, type: 1, y: 1},
                    {x: 275, type: 1, y: 2},
                    {x: 275, type: 1, y: 3},
                    {x: 275, type: 1, y: 4},
                    {x: 275, type: 1, y: 5},
                    {x: 275, type: 1, y: 6},
                    {x: 275, type: 1, y: 7},

                    // ================= 7. 거미 코스 (칼타이밍 반전 매운맛 난이도) =================
                    {x: 288, type: 2, y: 0}, {x: 289, type: 2, y: 0}, // 바닥 가시 (천장으로 반전 필수)
                    {x: 300, type: 5, y: 8}, {x: 301, type: 5, y: 8}, // 천장 가시 (바닥으로 반전 필수)
                    {x: 312, type: 2, y: 0}, {x: 313, type: 2, y: 0},
                    {x: 322, type: 3, y: 4, id: 4}, // 코인 4
                    {x: 325, type: 5, y: 8}, {x: 326, type: 5, y: 8},
                    {x: 338, type: 2, y: 0}, {x: 339, type: 2, y: 0},
                    {x: 350, type: 5, y: 8}, {x: 351, type: 5, y: 8},
                    {x: 362, type: 2, y: 0},

                    // ================= 8. 최종 큐브 포탈 벽 및 피날레 (X: 375~420) =================
                    {x: 375, type: 7, y: 0},
                    {x: 375, type: 1, y: 1},
                    {x: 375, type: 1, y: 2},
                    {x: 375, type: 1, y: 3},
                    {x: 375, type: 1, y: 4},
                    {x: 375, type: 1, y: 5},
                    {x: 375, type: 1, y: 6},
                    {x: 375, type: 1, y: 7},

                    {x: 388, type: 2, y: 0}, {x: 389, type: 2, y: 0}, {x: 390, type: 2, y: 0},
                    {x: 398, type: 4, y: 3},
                    {x: 408, type: 1, y: 2},
                    {x: 418, type: 2, y: 0}
                ];
                return map;
            }

            const STAGE_MAP = generateMap();
            const FINISH_LINE_X = 430 * BLOCK_SIZE;

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
                                if (dist < BLOCK_SIZE * 2.5) {
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

                // 모드별 물리 로직
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
                        player.angle += 10;
                    } else {
                        player.angle = Math.round(player.angle / 90) * 90;
                    }
                } 
                else if (player.mode === "ship") {
                    if (isHolding) player.vy -= 0.75;
                    else player.vy += 0.65;

                    player.vy = Math.max(-6.5, Math.min(6.5, player.vy));
                    player.y += player.vy;
                    player.angle = player.vy * 4.0;

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

                // 충돌 판정
                let pBox = {
                    x: player.x + 6,
                    y: player.y + 6,
                    w: BLOCK_SIZE - 12,
                    h: BLOCK_SIZE - 12
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
                            if (prevY + BLOCK_SIZE <= oBox.y + 18 && player.vy >= 0 && !player.spiderUpsideDown) {
                                player.y = oBox.y - BLOCK_SIZE;
                                player.vy = 0;
                                onBlock = true;
                            } else {
                                killPlayer();
                            }
                        }
                        else if (obj.type === 3 && !collectedCoinIds.has(obj.id)) {
                            collectedCoinIds.add(obj.id);
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

                // 배경
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

                // Grid Line
                ctx.strokeStyle = "rgba(0, 240, 255, 0.08)";
                ctx.lineWidth = 1;
                let gridOffset = (cameraX * 0.3) % 40;
                for (let x = -gridOffset; x < SCREEN_WIDTH; x += 40) {
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, SCREEN_HEIGHT); ctx.stroke();
                }

                // Ground & Ceiling
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

                // Spider Trail
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

                // Jump Ring Wave
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

                // STAGE MAP Rendering
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
                            ctx.moveTo(screenX + BLOCK_SIZE/2, screenY + 2);
                            ctx.lineTo(screenX + 2, screenY + BLOCK_SIZE);
                            ctx.lineTo(screenX + BLOCK_SIZE - 2, screenY + BLOCK_SIZE);
                            ctx.closePath(); ctx.fill(); ctx.stroke();
                            ctx.restore();
                        }
                        else if (obj.type === 5) {
                            ctx.save();
                            ctx.fillStyle = "#1a000a"; ctx.strokeStyle = "#ff0055";
                            ctx.shadowColor = "#ff0055"; ctx.shadowBlur = 10; ctx.lineWidth = 2;
                            ctx.beginPath();
                            ctx.moveTo(screenX + 2, screenY);
                            ctx.lineTo(screenX + BLOCK_SIZE - 2, screenY);
                            ctx.lineTo(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE - 2);
                            ctx.closePath(); ctx.fill(); ctx.stroke();
                            ctx.restore();
                        }
                        else if (obj.type === 3 && !collectedCoinIds.has(obj.id)) {
                            let pulse = Math.sin(animFrame * 0.1) * 2;
                            ctx.save();
                            ctx.shadowColor = "#ffd700"; ctx.shadowBlur = 15;
                            ctx.fillStyle = "#ffd700";
                            ctx.beginPath();
                            ctx.arc(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 11 + pulse, 0, Math.PI * 2);
                            ctx.fill(); ctx.restore();
                        }
                        else if (obj.type === 4) {
                            ctx.save();
                            ctx.shadowColor = "#ffe600"; ctx.shadowBlur = 12;
                            ctx.strokeStyle = "#ffe600"; ctx.lineWidth = 3;
                            ctx.beginPath();
                            ctx.arc(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 14, 0, Math.PI * 2);
                            ctx.stroke();
                            ctx.fillStyle = "#ffffff"; ctx.beginPath();
                            ctx.arc(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 6, 0, Math.PI * 2);
                            ctx.fill(); ctx.restore();
                        }
                        else if (obj.type === 6 || obj.type === 7 || obj.type === 8) {
                            let portalColor = obj.type === 6 ? "#ff007f" : (obj.type === 7 ? "#00f0ff" : "#aa00ff");
                            ctx.save();
                            ctx.shadowColor = portalColor; ctx.shadowBlur = 18;
                            ctx.strokeStyle = portalColor; ctx.lineWidth = 4;
                            ctx.beginPath();
                            ctx.ellipse(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 14, 40, 0, 0, Math.PI * 2);
                            ctx.stroke(); ctx.restore();
                        }
                    }
                });

                // Finish Line
                let finishX = FINISH_LINE_X - cameraX;
                if (finishX >= -BLOCK_SIZE && finishX <= SCREEN_WIDTH) {
                    ctx.save();
                    ctx.fillStyle = "#00f0ff"; ctx.shadowColor = "#00f0ff"; ctx.shadowBlur = 20;
                    ctx.fillRect(finishX, 0, 12, GROUND_Y);
                    ctx.restore();
                }

                // Particles
                particles.forEach(p => {
                    let pX = p.x - cameraX;
                    ctx.save();
                    ctx.fillStyle = p.color; ctx.globalAlpha = p.life;
                    ctx.fillRect(pX, p.y, 4, 4);
                    ctx.restore();
                });

                // Player
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
