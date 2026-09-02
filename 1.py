import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="Geometry Dash Deluxe Ultimate", layout="centered")
    st.title("Geometry Dash Deluxe Edition")
    st.caption("맵 길이 3배 확장, 네온 그래픽 리뉴얼, 모드 전환 코스 재배치 완료!")
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

            // 물리 매개변수 (상향된 난이도에 맞춘 기동성)
            const GRAVITY = 1.35;
            const JUMP_STRENGTH = -16.0;
            const SPEED = 8.0; 

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
                    // ================= 1. 큐브 구간 (X: 18~90) : 정밀 연타 및 타이밍 =================
                    {x: 20, type: 2, y: 0},
                    {x: 27, type: 2, y: 0}, {x: 28, type: 2, y: 0},
                    {x: 35, type: 1, y: 0}, {x: 36, type: 1, y: 1}, {x: 37, type: 1, y: 2},
                    {x: 37, type: 2, y: 3},
                    {x: 44, type: 4, y: 2}, 
                    {x: 50, type: 1, y: 2}, {x: 51, type: 2, y: 3},
                    {x: 56, type: 3, y: 4, id: 1}, // 코인 1
                    {x: 62, type: 2, y: 0}, {x: 63, type: 2, y: 0}, {x: 64, type: 2, y: 0},
                    {x: 72, type: 1, y: 1}, {x: 75, type: 4, y: 2.5},
                    {x: 82, type: 2, y: 0}, {x: 83, type: 2, y: 0},

                    // ================= 2. 비행기 포탈 (X: 95) =================
                    {x: 95, type: 6, y: 2},

                    // ================= 3. 비행기 코스 (X: 100~190) : 땅 착지 가능, 바느질 통과 =================
                    {x: 110, type: 1, y: 4}, {x: 110, type: 1, y: 5}, {x: 110, type: 1, y: 6}, {x: 110, type: 1, y: 7}, // 위 장해물
                    {x: 110, type: 2, y: 0}, // 바닥 가시
                    {x: 125, type: 5, y: 8}, {x: 125, type: 1, y: 1}, {x: 125, type: 1, y: 2}, // 정밀 통과
                    {x: 140, type: 3, y: 5, id: 2}, // 코인 2
                    {x: 155, type: 1, y: 3}, {x: 155, type: 1, y: 4}, {x: 155, type: 1, y: 5},
                    {x: 170, type: 5, y: 8}, {x: 170, type: 2, y: 0},
                    {x: 185, type: 1, y: 2}, {x: 185, type: 1, y: 7},

                    // ================= 4. 다시 큐브 모드로 전환 (X: 200) =================
                    {x: 200, type: 7, y: 1},

                    // ================= 5. 중간 큐브 코스 (X: 205~280) =================
                    {x: 212, type: 2, y: 0}, {x: 213, type: 2, y: 0},
                    {x: 222, type: 1, y: 1}, {x: 223, type: 1, y: 2}, {x: 224, type: 2, y: 3},
                    {x: 232, type: 4, y: 2},
                    {x: 240, type: 1, y: 3}, {x: 241, type: 2, y: 4},
                    {x: 250, type: 3, y: 5, id: 3}, // 코인 3
                    {x: 260, type: 2, y: 0}, {x: 261, type: 2, y: 0}, {x: 262, type: 2, y: 0},
                    {x: 272, type: 4, y: 2}, {x: 277, type: 4, y: 4},

                    // ================= 6. 거미 포탈 (X: 290) =================
                    {x: 290, type: 8, y: 0},

                    // ================= 7. 거미 코스 (X: 295~390) : 상하 빠른 스위칭 =================
                    {x: 305, type: 2, y: 0}, {x: 306, type: 2, y: 0},
                    {x: 318, type: 5, y: 8}, {x: 319, type: 5, y: 8},
                    {x: 330, type: 2, y: 0}, {x: 331, type: 2, y: 0},
                    {x: 342, type: 3, y: 4, id: 4}, // 코인 4
                    {x: 355, type: 5, y: 8}, {x: 356, type: 5, y: 8},
                    {x: 370, type: 2, y: 0}, {x: 371, type: 2, y: 0},
                    {x: 385, type: 5, y: 8},

                    // ================= 8. 최종 큐브 복귀 및 피날레 (X: 400~440) =================
                    {x: 400, type: 7, y: 0},
                    {x: 410, type: 2, y: 0}, {x: 411, type: 2, y: 0},
                    {x: 420, type: 1, y: 1}, {x: 421, type: 2, y: 2},
                    {x: 430, type: 4, y: 2},
                    {x: 440, type: 1, y: 0}
                ];
                return map;
            }

            const STAGE_MAP = generateMap();
            const FINISH_LINE_X = 450 * BLOCK_SIZE;

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
                        player.angle += 12;
                    } else {
                        player.angle = Math.round(player.angle / 90) * 90;
                    }
                } 
                else if (player.mode === "ship") {
                    if (isHolding) player.vy -= 0.85;
                    else player.vy += 0.75;

                    player.vy = Math.max(-7.5, Math.min(7.5, player.vy));
                    player.y += player.vy;
                    player.angle = player.vy * 3.5;

                    // 천장 제한
                    if (player.y <= CEILING_Y) {
                        player.y = CEILING_Y;
                        player.vy = 0;
                    }
                    
                    // [요청 1 반영] 비행기 모드일 때 바닥에 닿아도 죽지 않고 안전하게 비행
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

                // 충돌 처리 (정밀 히트박스 적용)
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

            // [요청 8 반영] 디테일하고 멋진 그래픽 랜더링
            function draw() {
                ctx.clearRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
                let cameraX = player.x - 120;

                // 1. 네온 사이버펑크 배경 그리드
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

                // 원근감 원경 배경 격자 선
                ctx.strokeStyle = "rgba(0, 240, 255, 0.08)";
                ctx.lineWidth = 1;
                let gridOffset = (cameraX * 0.3) % 40;
                for (let x = -gridOffset; x < SCREEN_WIDTH; x += 40) {
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, SCREEN_HEIGHT); ctx.stroke();
                }

                // 천장 및 바닥 레일
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
                ctx.shadowBlur = 0; // 초기화

                // 거미 이동 궤적
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

                // 점프 충격파
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

                // 2. STAGE MAP 오브젝트 그리기
                STAGE_MAP.forEach(obj => {
                    let screenX = obj.x * BLOCK_SIZE - cameraX;
                    let screenY = GROUND_Y - BLOCK_SIZE - (obj.y * BLOCK_SIZE);

                    if (screenX >= -BLOCK_SIZE * 2 && screenX <= SCREEN_WIDTH + BLOCK_SIZE) {
                        // 블록
                        if (obj.type === 1) {
                            ctx.save();
                            ctx.fillStyle = "#090d16";
                            ctx.fillRect(screenX, screenY, BLOCK_SIZE, BLOCK_SIZE);
                            ctx.strokeStyle = "#00f0ff";
                            ctx.shadowColor = "#00f0ff"; ctx.shadowBlur = 8;
                            ctx.lineWidth = 2;
                            ctx.strokeRect(screenX, screenY, BLOCK_SIZE, BLOCK_SIZE);
                            // 내부에 입체 X 패턴 추가
                            ctx.strokeStyle = "rgba(0, 240, 255, 0.3)";
                            ctx.beginPath();
                            ctx.moveTo(screenX, screenY); ctx.lineTo(screenX + BLOCK_SIZE, screenY + BLOCK_SIZE);
                            ctx.moveTo(screenX + BLOCK_SIZE, screenY); ctx.lineTo(screenX, screenY + BLOCK_SIZE);
                            ctx.stroke();
                            ctx.restore();
                        }
                        // 바닥 가시
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
                        // 천장 가시
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
                        // 코인
                        else if (obj.type === 3 && !collectedCoinIds.has(obj.id)) {
                            let pulse = Math.sin(animFrame * 0.1) * 2;
                            ctx.save();
                            ctx.shadowColor = "#ffd700"; ctx.shadowBlur = 15;
                            ctx.fillStyle = "#ffd700";
                            ctx.beginPath();
                            ctx.arc(screenX + BLOCK_SIZE/2, screenY + BLOCK_SIZE/2, 11 + pulse, 0, Math.PI * 2);
                            ctx.fill(); ctx.restore();
                        }
                        // 점프링
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
                        // 포탈류
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

                // 결승선 랜더링
                let finishX = FINISH_LINE_X - cameraX;
                if (finishX >= -BLOCK_SIZE && finishX <= SCREEN_WIDTH) {
                    ctx.save();
                    ctx.fillStyle = "#00f0ff"; ctx.shadowColor = "#00f0ff"; ctx.shadowBlur = 20;
                    ctx.fillRect(finishX, 0, 12, GROUND_Y);
                    ctx.restore();
                }

                // 파티클
                particles.forEach(p => {
                    let pX = p.x - cameraX;
                    ctx.save();
                    ctx.fillStyle = p.color; ctx.globalAlpha = p.life;
                    ctx.fillRect(pX, p.y, 4, 4);
                    ctx.restore();
                });

                // 3. 플레이어 랜더링 (디테일 상향)
                if (!player.isDead) {
                    ctx.save();
                    ctx.translate(120 + BLOCK_SIZE/2, player.y + BLOCK_SIZE/2);
                    ctx.rotate((player.angle * Math.PI) / 180);

                    // [요청 7 반영] 디테일해진 큐브 (네온 테두리, 내부 그라데이션, 고글 눈)
                    if (player.mode === "cube") {
                        let cGrad = ctx.createLinearGradient(-20, -20, 20, 20);
                        cGrad.addColorStop(0, "#00f0ff"); cGrad.addColorStop(1, "#0077ff");
                        ctx.fillStyle = cGrad;
                        ctx.fillRect(-BLOCK_SIZE/2, -BLOCK_SIZE/2, BLOCK_SIZE, BLOCK_SIZE);
                        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2.5;
                        ctx.strokeRect(-BLOCK_SIZE/2, -BLOCK_SIZE/2, BLOCK_SIZE, BLOCK_SIZE);
                        
                        // 고글 안경 디자인
                        ctx.fillStyle = "#000000";
                        ctx.fillRect(-12, -8, 24, 10);
                        ctx.fillStyle = "#00f0ff";
                        ctx.fillRect(-9, -6, 8, 6); ctx.fillRect(1, -6, 8, 6);
                    } 
                    // [요청 2 반영] 디테일해진 비행기 (유선형 캐노피, 날개, 제트 노즐)
                    else if (player.mode === "ship") {
                        // 몸체
                        ctx.fillStyle = "#ff007f";
                        ctx.beginPath();
                        ctx.moveTo(20, 0); ctx.lineTo(-15, -12); ctx.lineTo(-15, 12);
                        ctx.closePath(); ctx.fill();
                        
                        // 캐노피 (조종석)
                        ctx.fillStyle = "#00f0ff";
                        ctx.beginPath();
                        ctx.ellipse(2, -3, 8, 5, 0, 0, Math.PI*2);
                        ctx.fill();

                        // 날개
                        ctx.fillStyle = "#b5005b";
                        ctx.beginPath();
                        ctx.moveTo(-2, 0); ctx.lineTo(-14, -18); ctx.lineTo(-6, 0);
                        ctx.closePath(); ctx.fill();

                        // 제트 엔진 노즐
                        ctx.fillStyle = "#ffcc00";
                        ctx.fillRect(-20, -5, 5, 10);
                    } 
                    // 거미 디자인
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

                // 화면 플래시 Effect
                if (screenFlash.alpha > 0) {
                    ctx.fillStyle = screenFlash.color;
                    ctx.globalAlpha = screenFlash.alpha;
                    ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
                    ctx.globalAlpha = 1.0;
                }

                // 클리어 화면
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
