import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Geometry Dash Mega Edition", layout="centered")
st.title("🎮 Geometry Dash - Mega 2000+ Edition")
# map_data.py - Stereo Madness 2,000+ Full Object Data (Part 1/5)

MAP_OBJECTS = [
    # === [01/50] Section 1: Intro Spikes & Basic Steps ===
    {"type": "spike", "x": 600, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 850, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 1100, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 1135, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 1450, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 1485, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 1520, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 1700, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 1730, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 1760, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 1790, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 1900, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 1930, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 1960, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 1990, "y": 250, "w": 30, "h": 120},

    # === [02/50] Section 2: Jump Pad & Ring Introduction ===
    {"type": "spike", "x": 2100, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 2220, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 2450, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 2485, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 2700, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 2730, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 2760, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 2790, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 2820, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 2850, "y": 310, "w": 30, "h": 60},
    {"type": "pad_yellow", "x": 2880, "y": 300, "w": 30, "h": 10},
    {"type": "block", "x": 3000, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 3030, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 3060, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 3090, "y": 250, "w": 30, "h": 120},
    {"type": "ring_yellow", "x": 3180, "y": 180, "w": 30, "h": 30},

    # === [03/50] Section 3: High Platforms & Step Over Spikes ===
    {"type": "block", "x": 3300, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 3330, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 3360, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 3450, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 3480, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 3510, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 3600, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 3630, "y": 250, "w": 30, "h": 120},
    {"type": "spike", "x": 3720, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 3755, "y": 335, "w": 30, "h": 35},

    # === [04/50] Section 4: First Ship Portal Tunnel (Top/Bottom Ceiling Structure) ===
    {"type": "portal_ship", "x": 4000, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 4200, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4230, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4260, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4290, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4320, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4350, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4380, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4410, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4440, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4470, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4500, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4530, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4560, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4590, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 4620, "y": 0, "w": 30, "h": 120},

    # === [05/50] Section 5: Ship Obstacles & Ceiling Spikes ===
    {"type": "spike", "x": 4300, "y": 120, "w": 30, "h": 30},
    {"type": "spike", "x": 4400, "y": 120, "w": 30, "h": 30},
    {"type": "spike", "x": 4500, "y": 120, "w": 30, "h": 30},
    {"type": "block", "x": 4650, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4680, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4710, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4740, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4770, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4800, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4830, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4860, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4890, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4920, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4950, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 4980, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 5010, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 5040, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 5070, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 5100, "y": 280, "w": 30, "h": 90},

    # === [06/50] Section 6: Extended Ship Tunnel Ceiling Top ===
    {"type": "block", "x": 5130, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5160, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5190, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5220, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5250, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5280, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5310, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5340, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5370, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5400, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5430, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5460, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5490, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5520, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5550, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5580, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5610, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5640, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5670, "y": 0, "w": 30, "h": 90},
    {"type": "block", "x": 5700, "y": 0, "w": 30, "h": 90},

    # === [07/50] Section 7: Mid-Air Columns & Obstacles ===
    {"type": "block", "x": 5730, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5760, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5790, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5820, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5850, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5880, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5910, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5940, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 5970, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 6000, "y": 180, "w": 30, "h": 190},
    {"type": "spike", "x": 5760, "y": 150, "w": 30, "h": 30},
    {"type": "spike", "x": 5880, "y": 150, "w": 30, "h": 30},
    {"type": "spike", "x": 6000, "y": 150, "w": 30, "h": 30},

    # === [08/50] Section 8: Return to Cube Mode Portal ===
    {"type": "portal_cube", "x": 6300, "y": 150, "w": 45, "h": 220},
    {"type": "spike", "x": 6500, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 6535, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 6650, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6680, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6710, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6740, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6770, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6800, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6830, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6860, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6890, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6920, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6950, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 6980, "y": 310, "w": 30, "h": 60},

    # === [09/50] Section 9: Staircase Structure & Secret Coin 1 Area ===
    {"type": "block", "x": 7100, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7130, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7160, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7190, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7220, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7250, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7280, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7310, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7340, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7370, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 7400, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 7430, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 7460, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 7490, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 7520, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 7550, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 7580, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 7610, "y": 220, "w": 30, "h": 150},

    # === [10/50] Section 10: Secret Coin 1 Platform & Trap Spikes ===
    {"type": "spike", "x": 7430, "y": 190, "w": 30, "h": 30},
    {"type": "coin", "x": 7490, "y": 160, "w": 30, "h": 30, "id": 1},
    {"type": "spike", "x": 7550, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 7700, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7730, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7760, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7790, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7820, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7850, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7880, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7910, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7940, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 7970, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 8100, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 8135, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 8170, "y": 335, "w": 30, "h": 35},

    # === [11/50] Section 11: Yellow Ring Chain Sequence ===
    {"type": "block", "x": 8300, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 8330, "y": 280, "w": 30, "h": 90},
    {"type": "ring_yellow", "x": 8450, "y": 200, "w": 30, "h": 30},
    {"type": "block", "x": 8550, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 8580, "y": 220, "w": 30, "h": 150},
    {"type": "ring_yellow", "x": 8700, "y": 140, "w": 30, "h": 30},
    {"type": "block", "x": 8800, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 8830, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 8860, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 8890, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 8920, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 8950, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 8980, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 9010, "y": 190, "w": 30, "h": 180},
    {"type": "coin", "x": 8920, "y": 130, "w": 30, "h": 30, "id": 2},

    # === [12/50] Section 12: High Platform Downward Drop ===
    {"type": "spike", "x": 9150, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 9185, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 9300, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9330, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9360, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9390, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9420, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9450, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9480, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9510, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9540, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 9570, "y": 310, "w": 30, "h": 60},

    # === [13/50] Section 13: Red Dark Ship Portal Transition ===
    {"type": "portal_ship_dark", "x": 9800, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 10000, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10030, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10060, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10090, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10120, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10150, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10180, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10210, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10240, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10270, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10300, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10330, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10360, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10390, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10420, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 10450, "y": 0, "w": 30, "h": 120},

    # === [14/50] Section 14: Dark Ship Secret Coin 3 Cavern ===
    {"type": "spike", "x": 10100, "y": 120, "w": 30, "h": 30},
    {"type": "spike", "x": 10250, "y": 120, "w": 30, "h": 30},
    {"type": "spike", "x": 10400, "y": 120, "w": 30, "h": 30},
    {"type": "coin", "x": 10300, "y": 60, "w": 30, "h": 30, "id": 3},
    {"type": "block", "x": 10500, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10530, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10560, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10590, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10620, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10650, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10680, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10710, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10740, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 10770, "y": 250, "w": 30, "h": 120},

    # === [15/50] Section 15: Finale Cube Transition & Jump Pads ===
    {"type": "portal_cube", "x": 11000, "y": 150, "w": 45, "h": 220},
    {"type": "spike", "x": 11200, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 11235, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 11350, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 11380, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 11410, "y": 310, "w": 30, "h": 60},
    {"type": "pad_yellow", "x": 11440, "y": 300, "w": 30, "h": 10},
    {"type": "block", "x": 11550, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 11580, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 11610, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 11640, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 11670, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 11800, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 11835, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 11870, "y": 335, "w": 30, "h": 35},

    # === [16/50] Section 16: Extended Run - Dense Spike Grid A ===
    {"type": "block", "x": 12000, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12030, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12060, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12090, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12120, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12150, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12180, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12210, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12240, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 12270, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 12090, "y": 280, "w": 30, "h": 30},
    {"type": "spike", "x": 12210, "y": 280, "w": 30, "h": 30},

    # === [17/50] Section 17: Extended Run - Dense Spike Grid B ===
    {"type": "block", "x": 12400, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12430, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12460, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12490, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12520, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12550, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12580, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12610, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12640, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 12670, "y": 250, "w": 30, "h": 120},
    {"type": "spike", "x": 12460, "y": 220, "w": 30, "h": 30},
    {"type": "spike", "x": 12610, "y": 220, "w": 30, "h": 30},

    # === [18/50] Section 18: Extended Run - High-Speed Jump Rings ===
    {"type": "ring_yellow", "x": 12800, "y": 250, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 12950, "y": 200, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 13100, "y": 150, "w": 30, "h": 30},
    {"type": "block", "x": 13250, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 13280, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 13310, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 13340, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 13370, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 13400, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 13430, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 13460, "y": 190, "w": 30, "h": 180},

    # === [19/50] Section 19: Precision Gap Jumps ===
    {"type": "spike", "x": 13600, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 13635, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 13750, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 13780, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 13900, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 13935, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 14050, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 14080, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 14200, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 14235, "y": 335, "w": 30, "h": 35},

    # === [20/50] Section 20: Mid-Air Stepping Blocks ===
    {"type": "block", "x": 14350, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 14450, "y": 210, "w": 30, "h": 30},
    {"type": "block", "x": 14550, "y": 170, "w": 30, "h": 30},
    {"type": "block", "x": 14650, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 14750, "y": 170, "w": 30, "h": 30},
    {"type": "block", "x": 14850, "y": 210, "w": 30, "h": 30},
    {"type": "block", "x": 14950, "y": 250, "w": 30, "h": 30},
    {"type": "spike", "x": 14450, "y": 180, "w": 30, "h": 30},
    {"type": "spike", "x": 14850, "y": 180, "w": 30, "h": 30},
  # === [21/50] Section 21: Deep Cavern Drop & Bottom Spikes ===
    {"type": "block", "x": 15100, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 15130, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 15160, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 15190, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 15220, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 15250, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 15280, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 15310, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 15160, "y": 280, "w": 30, "h": 30},
    {"type": "spike", "x": 15250, "y": 280, "w": 30, "h": 30},

    # === [22/50] Section 22: High Wall Jump Pad Launch ===
    {"type": "pad_yellow", "x": 15450, "y": 360, "w": 30, "h": 10},
    {"type": "block", "x": 15600, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 15630, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 15660, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 15690, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 15720, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 15750, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 15780, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 15810, "y": 190, "w": 30, "h": 180},

    # === [23/50] Section 23: Sky Platform Sprint ===
    {"type": "block", "x": 15950, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 15980, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 16010, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 16040, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 16070, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 16100, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 16130, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 16160, "y": 130, "w": 30, "h": 30},
    {"type": "spike", "x": 16040, "y": 100, "w": 30, "h": 30},

    # === [24/50] Section 24: Descent Step Down Sequence ===
    {"type": "block", "x": 16300, "y": 170, "w": 30, "h": 30},
    {"type": "block", "x": 16330, "y": 170, "w": 30, "h": 30},
    {"type": "block", "x": 16450, "y": 210, "w": 30, "h": 30},
    {"type": "block", "x": 16480, "y": 210, "w": 30, "h": 30},
    {"type": "block", "x": 16600, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 16630, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 16750, "y": 290, "w": 30, "h": 30},
    {"type": "block", "x": 16780, "y": 290, "w": 30, "h": 30},

    # === [25/50] Section 25: Ground Spike Hazard Grid ===
    {"type": "spike", "x": 16950, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 16985, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 17020, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 17150, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 17185, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 17220, "y": 335, "w": 30, "h": 35},

    # === [26/50] Section 26: Triple Ring Aerial Sequence ===
    {"type": "ring_yellow", "x": 17400, "y": 280, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 17550, "y": 230, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 17700, "y": 180, "w": 30, "h": 30},
    {"type": "block", "x": 17850, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 17880, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 17910, "y": 220, "w": 30, "h": 150},

    # === [27/50] Section 27: Ship Tunnel Part II - Lower Entrance ===
    {"type": "portal_ship", "x": 18100, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 18300, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 18330, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 18360, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 18390, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 18420, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 18450, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 18480, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 18510, "y": 0, "w": 30, "h": 150},

    # === [28/50] Section 28: Ship Tunnel Part II - Floor Blocks ===
    {"type": "block", "x": 18300, "y": 300, "w": 30, "h": 70},
    {"type": "block", "x": 18330, "y": 300, "w": 30, "h": 70},
    {"type": "block", "x": 18360, "y": 300, "w": 30, "h": 70},
    {"type": "block", "x": 18390, "y": 300, "w": 30, "h": 70},
    {"type": "block", "x": 18420, "y": 300, "w": 30, "h": 70},
    {"type": "block", "x": 18450, "y": 300, "w": 30, "h": 70},
    {"type": "block", "x": 18480, "y": 300, "w": 30, "h": 70},
    {"type": "block", "x": 18510, "y": 300, "w": 30, "h": 70},

    # === [29/50] Section 29: Ship Tunnel Slalom Course A ===
    {"type": "block", "x": 18650, "y": 120, "w": 30, "h": 120},
    {"type": "block", "x": 18680, "y": 120, "w": 30, "h": 120},
    {"type": "block", "x": 18710, "y": 120, "w": 30, "h": 120},
    {"type": "spike", "x": 18680, "y": 240, "w": 30, "h": 30},
    {"type": "block", "x": 18850, "y": 210, "w": 30, "h": 160},
    {"type": "block", "x": 18880, "y": 210, "w": 30, "h": 160},
    {"type": "block", "x": 18910, "y": 210, "w": 30, "h": 160},
    {"type": "spike", "x": 18880, "y": 180, "w": 30, "h": 30},

    # === [30/50] Section 30: Ship Tunnel Slalom Course B ===
    {"type": "block", "x": 19050, "y": 90, "w": 30, "h": 140},
    {"type": "block", "x": 19080, "y": 90, "w": 30, "h": 140},
    {"type": "block", "x": 19110, "y": 90, "w": 30, "h": 140},
    {"type": "spike", "x": 19080, "y": 230, "w": 30, "h": 30},
    {"type": "block", "x": 19250, "y": 230, "w": 30, "h": 140},
    {"type": "block", "x": 19280, "y": 230, "w": 30, "h": 140},
    {"type": "block", "x": 19310, "y": 230, "w": 30, "h": 140},
    {"type": "spike", "x": 19280, "y": 200, "w": 30, "h": 30},

    # === [31/50] Section 31: Exit Ship Portal to Cube ===
    {"type": "portal_cube", "x": 19500, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 19700, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 19730, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 19760, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 19790, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 19820, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 19850, "y": 310, "w": 30, "h": 60},

    # === [32/50] Section 32: Precision Staircase Climbing ===
    {"type": "block", "x": 20000, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 20030, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 20150, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 20180, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 20300, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 20330, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 20450, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 20480, "y": 190, "w": 30, "h": 180},

    # === [33/50] Section 33: High Top Corridor ===
    {"type": "block", "x": 20600, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 20630, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 20660, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 20690, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 20720, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 20750, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 20780, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 20810, "y": 190, "w": 30, "h": 30},
    {"type": "spike", "x": 20690, "y": 160, "w": 30, "h": 30},

    # === [34/50] Section 34: Long Fall & Bottom Pad ===
    {"type": "spike", "x": 20950, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 20985, "y": 335, "w": 30, "h": 35},
    {"type": "pad_yellow", "x": 21100, "y": 360, "w": 30, "h": 10},
    {"type": "block", "x": 21250, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 21280, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 21310, "y": 250, "w": 30, "h": 120},

    # === [35/50] Section 35: Floating Island Platforms A ===
    {"type": "block", "x": 21450, "y": 220, "w": 30, "h": 30},
    {"type": "block", "x": 21480, "y": 220, "w": 30, "h": 30},
    {"type": "block", "x": 21510, "y": 220, "w": 30, "h": 30},
    {"type": "block", "x": 21650, "y": 180, "w": 30, "h": 30},
    {"type": "block", "x": 21680, "y": 180, "w": 30, "h": 30},
    {"type": "block", "x": 21710, "y": 180, "w": 30, "h": 30},
    {"type": "spike", "x": 21480, "y": 190, "w": 30, "h": 30},
    {"type": "spike", "x": 21680, "y": 150, "w": 30, "h": 30},

    # === [36/50] Section 36: Floating Island Platforms B ===
    {"type": "block", "x": 21850, "y": 140, "w": 30, "h": 30},
    {"type": "block", "x": 21880, "y": 140, "w": 30, "h": 30},
    {"type": "block", "x": 21910, "y": 140, "w": 30, "h": 30},
    {"type": "block", "x": 22050, "y": 180, "w": 30, "h": 30},
    {"type": "block", "x": 22080, "y": 180, "w": 30, "h": 30},
    {"type": "block", "x": 22110, "y": 180, "w": 30, "h": 30},
    {"type": "spike", "x": 21880, "y": 110, "w": 30, "h": 30},
    {"type": "spike", "x": 22080, "y": 150, "w": 30, "h": 30},

    # === [37/50] Section 37: Ground Landing & Double Spikes ===
    {"type": "block", "x": 22250, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 22280, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 22310, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 22340, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 22450, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 22485, "y": 335, "w": 30, "h": 35},

    # === [38/50] Section 38: Rhythmic Jump Ring Steps ===
    {"type": "ring_yellow", "x": 22600, "y": 280, "w": 30, "h": 30},
    {"type": "block", "x": 22700, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 22730, "y": 250, "w": 30, "h": 120},
    {"type": "ring_yellow", "x": 22850, "y": 200, "w": 30, "h": 30},
    {"type": "block", "x": 22950, "y": 170, "w": 30, "h": 200},
    {"type": "block", "x": 22980, "y": 170, "w": 30, "h": 200},

    # === [39/50] Section 39: Wall Drop & Pit Avoidance ===
    {"type": "spike", "x": 23100, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 23135, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 23170, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 23300, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 23330, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 23360, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 23390, "y": 310, "w": 30, "h": 60},

    # === [40/50] Section 40: High Pillars & Air Gaps ===
    {"type": "block", "x": 23550, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 23580, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 23720, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 23750, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 23650, "y": 335, "w": 30, "h": 35},
  # === [41/50] Section 41: Mid-Air Bounce Track ===
    {"type": "pad_yellow", "x": 23900, "y": 360, "w": 30, "h": 10},
    {"type": "ring_yellow", "x": 24050, "y": 200, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 24200, "y": 150, "w": 30, "h": 30},
    {"type": "block", "x": 24350, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 24380, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 24410, "y": 190, "w": 30, "h": 180},

    # === [42/50] Section 42: Ship Tunnel Part III - High Entrance ===
    {"type": "portal_ship", "x": 24600, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 24800, "y": 0, "w": 30, "h": 100},
    {"type": "block", "x": 24830, "y": 0, "w": 30, "h": 100},
    {"type": "block", "x": 24860, "y": 0, "w": 30, "h": 100},
    {"type": "block", "x": 24890, "y": 0, "w": 30, "h": 100},
    {"type": "block", "x": 24920, "y": 0, "w": 30, "h": 100},
    {"type": "block", "x": 24950, "y": 0, "w": 30, "h": 100},
    {"type": "block", "x": 24980, "y": 0, "w": 30, "h": 100},
    {"type": "block", "x": 25010, "y": 0, "w": 30, "h": 100},

    # === [43/50] Section 43: Ship Tunnel Part III - Floor Support ===
    {"type": "block", "x": 24800, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 24830, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 24860, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 24890, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 24920, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 24950, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 24980, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 25010, "y": 280, "w": 30, "h": 90},

    # === [44/50] Section 44: Ship Cavern Pillars A ===
    {"type": "block", "x": 25150, "y": 100, "w": 30, "h": 160},
    {"type": "block", "x": 25180, "y": 100, "w": 30, "h": 160},
    {"type": "block", "x": 25210, "y": 100, "w": 30, "h": 160},
    {"type": "spike", "x": 25180, "y": 260, "w": 30, "h": 30},
    {"type": "block", "x": 25350, "y": 210, "w": 30, "h": 160},
    {"type": "block", "x": 25380, "y": 210, "w": 30, "h": 160},
    {"type": "block", "x": 25410, "y": 210, "w": 30, "h": 160},
    {"type": "spike", "x": 25380, "y": 180, "w": 30, "h": 30},

    # === [45/50] Section 45: Ship Cavern Pillars B ===
    {"type": "block", "x": 25550, "y": 80, "w": 30, "h": 160},
    {"type": "block", "x": 25580, "y": 80, "w": 30, "h": 160},
    {"type": "block", "x": 25610, "y": 80, "w": 30, "h": 160},
    {"type": "spike", "x": 25580, "y": 240, "w": 30, "h": 30},
    {"type": "block", "x": 25750, "y": 230, "w": 30, "h": 140},
    {"type": "block", "x": 25780, "y": 230, "w": 30, "h": 140},
    {"type": "block", "x": 25810, "y": 230, "w": 30, "h": 140},
    {"type": "spike", "x": 25780, "y": 200, "w": 30, "h": 30},

    # === [46/50] Section 46: Final Ship Challenge Passage ===
    {"type": "block", "x": 25950, "y": 120, "w": 30, "h": 120},
    {"type": "block", "x": 25980, "y": 120, "w": 30, "h": 120},
    {"type": "block", "x": 26010, "y": 120, "w": 30, "h": 120},
    {"type": "spike", "x": 25980, "y": 240, "w": 30, "h": 30},
    {"type": "block", "x": 26150, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 26180, "y": 190, "w": 30, "h": 180},
    {"type": "block", "x": 26210, "y": 190, "w": 30, "h": 180},
    {"type": "spike", "x": 26180, "y": 160, "w": 30, "h": 30},

    # === [47/50] Section 47: Return to Cube Mode Portal ===
    {"type": "portal_cube", "x": 26400, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 26600, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 26630, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 26660, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 26690, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 26720, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 26750, "y": 310, "w": 30, "h": 60},

    # === [48/50] Section 48: High Speed Platform Run ===
    {"type": "block", "x": 26900, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 26930, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 26960, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 26990, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 26945, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 27120, "y": 240, "w": 30, "h": 130},
    {"type": "block", "x": 27150, "y": 240, "w": 30, "h": 130},
    {"type": "block", "x": 27180, "y": 240, "w": 30, "h": 130},

    # === [49/50] Section 49: Final Spike Pit Gauntlet ===
    {"type": "spike", "x": 27350, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 27385, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 27420, "y": 335, "w": 30, "h": 35},
    {"type": "pad_yellow", "x": 27550, "y": 360, "w": 30, "h": 10},
    {"type": "block", "x": 27700, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 27730, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 27760, "y": 250, "w": 30, "h": 120},

    # === [50/50] Section 50: Victory Approach & Goal Structure ===
    {"type": "block", "x": 27900, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 27930, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 27960, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 27990, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 28020, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 28050, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 28080, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 28110, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 27990, "y": 280, "w": 30, "h": 30},
  # === [51/60] Section 51: Extension - Deep Descent Cavern ===
    {"type": "block", "x": 28300, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 28330, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 28360, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 28390, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 28330, "y": 250, "w": 30, "h": 30},
    {"type": "spike", "x": 28360, "y": 250, "w": 30, "h": 30},

    # === [52/60] Section 52: Extension - Double Ring Sky Leap ===
    {"type": "ring_yellow", "x": 28550, "y": 250, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 28700, "y": 200, "w": 30, "h": 30},
    {"type": "block", "x": 28850, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 28880, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 28910, "y": 180, "w": 30, "h": 190},

    # === [53/60] Section 53: Extension - Precision Low Ceiling Run ===
    {"type": "block", "x": 29050, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 29080, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 29110, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 29140, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 29170, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 29200, "y": 0, "w": 30, "h": 220},
    {"type": "spike", "x": 29080, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 29140, "y": 335, "w": 30, "h": 35},

    # === [54/60] Section 54: Extension - Pad Launch to High Platform ===
    {"type": "pad_yellow", "x": 29350, "y": 360, "w": 30, "h": 10},
    {"type": "block", "x": 29500, "y": 160, "w": 30, "h": 210},
    {"type": "block", "x": 29530, "y": 160, "w": 30, "h": 210},
    {"type": "block", "x": 29560, "y": 160, "w": 30, "h": 210},
    {"type": "block", "x": 29590, "y": 160, "w": 30, "h": 210},
    {"type": "spike", "x": 29530, "y": 130, "w": 30, "h": 30},

    # === [55/60] Section 55: Extension - Ship Portal Transition ===
    {"type": "portal_ship", "x": 29750, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 29950, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 29980, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 30010, "y": 0, "w": 30, "h": 120},
    {"type": "block", "x": 29950, "y": 270, "w": 30, "h": 100},
    {"type": "block", "x": 29980, "y": 270, "w": 30, "h": 100},
    {"type": "block", "x": 30010, "y": 270, "w": 30, "h": 100},

    # === [56/60] Section 56: Extension - Ship Narrow Corridor A ===
    {"type": "block", "x": 30150, "y": 110, "w": 30, "h": 140},
    {"type": "block", "x": 30180, "y": 110, "w": 30, "h": 140},
    {"type": "block", "x": 30210, "y": 110, "w": 30, "h": 140},
    {"type": "spike", "x": 30180, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 30350, "y": 200, "w": 30, "h": 170},
    {"type": "block", "x": 30380, "y": 200, "w": 30, "h": 170},
    {"type": "block", "x": 30410, "y": 200, "w": 30, "h": 170},
    {"type": "spike", "x": 30380, "y": 170, "w": 30, "h": 30},

    # === [57/60] Section 57: Extension - Ship Narrow Corridor B ===
    {"type": "block", "x": 30550, "y": 90, "w": 30, "h": 150},
    {"type": "block", "x": 30580, "y": 90, "w": 30, "h": 150},
    {"type": "block", "x": 30610, "y": 90, "w": 30, "h": 150},
    {"type": "spike", "x": 30580, "y": 240, "w": 30, "h": 30},
    {"type": "block", "x": 30750, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 30780, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 30810, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 30780, "y": 190, "w": 30, "h": 30},

    # === [58/60] Section 58: Extension - Final Portal Return to Cube ===
    {"type": "portal_cube", "x": 31000, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 31200, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31230, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31260, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31290, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31320, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31350, "y": 310, "w": 30, "h": 60},

    # === [59/60] Section 59: Extension - Final Quad Spike Jump ===
    {"type": "spike", "x": 31500, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 31535, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 31570, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 31605, "y": 335, "w": 30, "h": 35},
    {"type": "pad_yellow", "x": 31750, "y": 360, "w": 30, "h": 10},

    # === [60/60] Section 60: Extension - Grand Finale Victory Podium ===
    {"type": "block", "x": 31900, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31930, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31960, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 31990, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 32020, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 32050, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 32080, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 32110, "y": 310, "w": 30, "h": 60},
  # === [61/60] Final Stretch: Extreme Spike Runway ===
    {"type": "spike", "x": 32250, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 32285, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 32320, "y": 335, "w": 30, "h": 35},
    {"type": "pad_yellow", "x": 32450, "y": 360, "w": 30, "h": 10},

    # === [62/60] Final Stretch: Last Sky Rings ===
    {"type": "ring_yellow", "x": 32600, "y": 250, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 32750, "y": 200, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 32900, "y": 150, "w": 30, "h": 30},

    # === [63/60] Grand Finale: Finish Line Platform ===
    {"type": "block", "x": 33050, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33080, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33110, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33140, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33170, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33200, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33230, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33260, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33290, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 33320, "y": 280, "w": 30, "h": 90},

# === [64/100] Extended Region: Deep Lava Cavern Opening ===
    {"type": "block", "x": 33450, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 33480, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 33510, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 33480, "y": 280, "w": 30, "h": 30},
    {"type": "block", "x": 33650, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 33680, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 33710, "y": 250, "w": 30, "h": 120},
    {"type": "spike", "x": 33680, "y": 220, "w": 30, "h": 30},

    # === [65/100] High-Frequency Spike Staircase ===
    {"type": "block", "x": 33850, "y": 310, "w": 30, "h": 60},
    {"type": "spike", "x": 33850, "y": 280, "w": 30, "h": 30},
    {"type": "block", "x": 33900, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 33900, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 33950, "y": 250, "w": 30, "h": 120},
    {"type": "spike", "x": 33950, "y": 220, "w": 30, "h": 30},
    {"type": "block", "x": 34000, "y": 220, "w": 30, "h": 150},

    # === [66/100] Sky Ring Chain Gauntlet ===
    {"type": "pad_yellow", "x": 34150, "y": 360, "w": 30, "h": 10},
    {"type": "ring_yellow", "x": 34300, "y": 200, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 34450, "y": 160, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 34600, "y": 200, "w": 30, "h": 30},
    {"type": "block", "x": 34750, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 34780, "y": 280, "w": 30, "h": 90},

    # === [67/100] Extended Ship Tunnel IV - Intro ===
    {"type": "portal_ship", "x": 34950, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 35150, "y": 0, "w": 30, "h": 110},
    {"type": "block", "x": 35180, "y": 0, "w": 30, "h": 110},
    {"type": "block", "x": 35210, "y": 0, "w": 30, "h": 110},
    {"type": "block", "x": 35240, "y": 0, "w": 30, "h": 110},
    {"type": "block", "x": 35150, "y": 260, "w": 30, "h": 110},
    {"type": "block", "x": 35180, "y": 260, "w": 30, "h": 110},
    {"type": "block", "x": 35210, "y": 260, "w": 30, "h": 110},
    {"type": "block", "x": 35240, "y": 260, "w": 30, "h": 110},

    # === [68/100] Ship Waves & Slalom Pillars ===
    {"type": "block", "x": 35400, "y": 80, "w": 30, "h": 170},
    {"type": "block", "x": 35430, "y": 80, "w": 30, "h": 170},
    {"type": "spike", "x": 35415, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 35600, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 35630, "y": 180, "w": 30, "h": 190},
    {"type": "spike", "x": 35615, "y": 150, "w": 30, "h": 30},
    {"type": "block", "x": 35800, "y": 60, "w": 30, "h": 170},
    {"type": "block", "x": 35830, "y": 60, "w": 30, "h": 170},
    {"type": "spike", "x": 35815, "y": 230, "w": 30, "h": 30},

    # === [69/100] Cube Mode Speed Run & Multi-Pads ===
    {"type": "portal_cube", "x": 36000, "y": 150, "w": 45, "h": 220},
    {"type": "pad_yellow", "x": 36180, "y": 360, "w": 30, "h": 10},
    {"type": "pad_yellow", "x": 36380, "y": 360, "w": 30, "h": 10},
    {"type": "block", "x": 36550, "y": 150, "w": 30, "h": 220},
    {"type": "block", "x": 36580, "y": 150, "w": 30, "h": 220},
    {"type": "spike", "x": 36550, "y": 120, "w": 30, "h": 30},

    # === [70/100] Extreme Precision Tightropes ===
    {"type": "block", "x": 36750, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 36750, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 36900, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 36900, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 37050, "y": 160, "w": 30, "h": 210},
    {"type": "spike", "x": 37050, "y": 130, "w": 30, "h": 30},
    {"type": "block", "x": 37200, "y": 280, "w": 30, "h": 90},

    # === [71/100] Mega Spike Pit Drop ===
    {"type": "spike", "x": 37350, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 37385, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 37420, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 37455, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 37490, "y": 335, "w": 30, "h": 35},
    {"type": "ring_yellow", "x": 37420, "y": 220, "w": 30, "h": 30},
    {"type": "block", "x": 37650, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 37680, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 37710, "y": 280, "w": 30, "h": 90},
# === [72/100] High Sky Platform & Drop ===
    {"type": "pad_yellow", "x": 37850, "y": 250, "w": 30, "h": 10},
    {"type": "block", "x": 38000, "y": 140, "w": 30, "h": 230},
    {"type": "block", "x": 38030, "y": 140, "w": 30, "h": 230},
    {"type": "block", "x": 38060, "y": 140, "w": 30, "h": 230},
    {"type": "spike", "x": 38030, "y": 110, "w": 30, "h": 30},
    {"type": "block", "x": 38250, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 38280, "y": 220, "w": 30, "h": 150},

    # === [73/100] Ship Tunnel V - Narrow Zig-Zag ===
    {"type": "portal_ship", "x": 38450, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 38650, "y": 0, "w": 30, "h": 140},
    {"type": "block", "x": 38680, "y": 0, "w": 30, "h": 140},
    {"type": "block", "x": 38650, "y": 240, "w": 30, "h": 130},
    {"type": "block", "x": 38680, "y": 240, "w": 30, "h": 130},
    {"type": "block", "x": 38850, "y": 100, "w": 30, "h": 140},
    {"type": "block", "x": 38880, "y": 100, "w": 30, "h": 140},
    {"type": "spike", "x": 38865, "y": 240, "w": 30, "h": 30},

    # === [74/100] Ship Cavern Precision Pass ===
    {"type": "block", "x": 39050, "y": 200, "w": 30, "h": 170},
    {"type": "block", "x": 39080, "y": 200, "w": 30, "h": 170},
    {"type": "spike", "x": 39065, "y": 170, "w": 30, "h": 30},
    {"type": "block", "x": 39250, "y": 50, "w": 30, "h": 180},
    {"type": "block", "x": 39280, "y": 50, "w": 30, "h": 180},
    {"type": "spike", "x": 39265, "y": 230, "w": 30, "h": 30},

    # === [75/100] Dual Ring Combo Run ===
    {"type": "portal_cube", "x": 39450, "y": 150, "w": 45, "h": 220},
    {"type": "ring_yellow", "x": 39650, "y": 240, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 39800, "y": 180, "w": 30, "h": 30},
    {"type": "block", "x": 39950, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 39980, "y": 250, "w": 30, "h": 120},
    {"type": "spike", "x": 39965, "y": 220, "w": 30, "h": 30},

    # === [76/100] Low Ceiling Sprint ===
    {"type": "block", "x": 40150, "y": 0, "w": 30, "h": 230},
    {"type": "block", "x": 40180, "y": 0, "w": 30, "h": 230},
    {"type": "block", "x": 40210, "y": 0, "w": 30, "h": 230},
    {"type": "block", "x": 40240, "y": 0, "w": 30, "h": 230},
    {"type": "spike", "x": 40180, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 40240, "y": 335, "w": 30, "h": 35},

    # === [77/100] Triple Pad Launch ===
    {"type": "pad_yellow", "x": 40400, "y": 360, "w": 30, "h": 10},
    {"type": "pad_yellow", "x": 40550, "y": 260, "w": 30, "h": 10},
    {"type": "block", "x": 40700, "y": 150, "w": 30, "h": 220},
    {"type": "block", "x": 40730, "y": 150, "w": 30, "h": 220},
    {"type": "spike", "x": 40715, "y": 120, "w": 30, "h": 30},

    # === [78/100] Sky Island Hopping ===
    {"type": "block", "x": 40900, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 40900, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 41100, "y": 180, "w": 30, "h": 190},
    {"type": "spike", "x": 41100, "y": 150, "w": 30, "h": 30},
    {"type": "block", "x": 41300, "y": 140, "w": 30, "h": 230},
    {"type": "spike", "x": 41300, "y": 110, "w": 30, "h": 30},

    # === [79/100] Massive Ground Spike Array ===
    {"type": "spike", "x": 41500, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 41535, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 41570, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 41605, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 41640, "y": 335, "w": 30, "h": 35},
    {"type": "ring_yellow", "x": 41570, "y": 210, "w": 30, "h": 30},

    # === [80/100] Fortress Wall Barrier ===
    {"type": "block", "x": 41850, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 41880, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 41910, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 41940, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 41880, "y": 250, "w": 30, "h": 30},
    {"type": "spike", "x": 41910, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 42100, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 42130, "y": 310, "w": 30, "h": 60},
# === [81/100] Extended Ship Tunnel VI - Extreme Corridor ===
    {"type": "portal_ship", "x": 42300, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 42500, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 42530, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 42560, "y": 0, "w": 30, "h": 150},
    {"type": "block", "x": 42500, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 42530, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 42560, "y": 250, "w": 30, "h": 120},

    # === [82/100] Ship Tunnel Precision Narrow Gap ===
    {"type": "block", "x": 42750, "y": 80, "w": 30, "h": 160},
    {"type": "block", "x": 42780, "y": 80, "w": 30, "h": 160},
    {"type": "spike", "x": 42765, "y": 240, "w": 30, "h": 30},
    {"type": "block", "x": 42950, "y": 200, "w": 30, "h": 170},
    {"type": "block", "x": 42980, "y": 200, "w": 30, "h": 170},
    {"type": "spike", "x": 42965, "y": 170, "w": 30, "h": 30},

    # === [83/100] High-Speed Cube Switch & Ring Cascade ===
    {"type": "portal_cube", "x": 43150, "y": 150, "w": 45, "h": 220},
    {"type": "pad_yellow", "x": 43300, "y": 360, "w": 30, "h": 10},
    {"type": "ring_yellow", "x": 43450, "y": 200, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 43600, "y": 150, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 43750, "y": 200, "w": 30, "h": 30},

    # === [84/100] Tower Spike Columns ===
    {"type": "block", "x": 43900, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 43930, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 43915, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 44100, "y": 160, "w": 30, "h": 210},
    {"type": "block", "x": 44130, "y": 160, "w": 30, "h": 210},
    {"type": "spike", "x": 44115, "y": 130, "w": 30, "h": 30},

    # === [85/100] Low-Altitude Spike Minefield ===
    {"type": "block", "x": 44300, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 44330, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 44365, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 44400, "y": 335, "w": 30, "h": 35},
    {"type": "block", "x": 44550, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 44550, "y": 250, "w": 30, "h": 30},

    # === [86/100] Elevated Pad Vaults ===
    {"type": "pad_yellow", "x": 44700, "y": 360, "w": 30, "h": 10},
    {"type": "block", "x": 44850, "y": 180, "w": 30, "h": 190},
    {"type": "block", "x": 44880, "y": 180, "w": 30, "h": 190},
    {"type": "pad_yellow", "x": 44880, "y": 170, "w": 30, "h": 10},
    {"type": "block", "x": 45050, "y": 100, "w": 30, "h": 270},
    {"type": "block", "x": 45080, "y": 100, "w": 30, "h": 270},

    # === [87/100] Cavern Drop & Spike Quad ===
    {"type": "spike", "x": 45250, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 45285, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 45320, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 45355, "y": 335, "w": 30, "h": 35},
    {"type": "ring_yellow", "x": 45300, "y": 200, "w": 30, "h": 30},

    # === [88/100] Final Ship Tunnel Sequence A ===
    {"type": "portal_ship", "x": 45500, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 45700, "y": 0, "w": 30, "h": 130},
    {"type": "block", "x": 45730, "y": 0, "w": 30, "h": 130},
    {"type": "block", "x": 45700, "y": 250, "w": 30, "h": 120},
    {"type": "block", "x": 45730, "y": 250, "w": 30, "h": 120},
    {"type": "spike", "x": 45715, "y": 130, "w": 30, "h": 30},

    # === [89/100] Final Ship Tunnel Sequence B ===
    {"type": "block", "x": 45900, "y": 120, "w": 30, "h": 140},
    {"type": "block", "x": 45930, "y": 120, "w": 30, "h": 140},
    {"type": "spike", "x": 45915, "y": 260, "w": 30, "h": 30},
    {"type": "block", "x": 46100, "y": 210, "w": 30, "h": 160},
    {"type": "block", "x": 46130, "y": 210, "w": 30, "h": 160},
    {"type": "spike", "x": 46115, "y": 180, "w": 30, "h": 30},

    # === [90/100] High Runway Transition ===
    {"type": "portal_cube", "x": 46300, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 46450, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 46480, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 46510, "y": 310, "w": 30, "h": 60},
# === [91/100] High-Altitude Spike Vaults ===
    {"type": "block", "x": 46650, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 46680, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 46665, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 46850, "y": 220, "w": 30, "h": 150},
    {"type": "block", "x": 46880, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 46865, "y": 190, "w": 30, "h": 30},

    # === [92/100] Sky Ring Triple Leap ===
    {"type": "pad_yellow", "x": 47050, "y": 360, "w": 30, "h": 10},
    {"type": "ring_yellow", "x": 47200, "y": 220, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 47350, "y": 170, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 47500, "y": 220, "w": 30, "h": 30},
    {"type": "block", "x": 47650, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 47680, "y": 280, "w": 30, "h": 90},

    # === [93/100] Extended Ship Tunnel VII - Heavy Pillars ===
    {"type": "portal_ship", "x": 47850, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 48050, "y": 0, "w": 30, "h": 140},
    {"type": "block", "x": 48080, "y": 0, "w": 30, "h": 140},
    {"type": "block", "x": 48110, "y": 0, "w": 30, "h": 140},
    {"type": "block", "x": 48050, "y": 260, "w": 30, "h": 110},
    {"type": "block", "x": 48080, "y": 260, "w": 30, "h": 110},
    {"type": "block", "x": 48110, "y": 260, "w": 30, "h": 110},

    # === [94/100] Ship Tunnel Slalom Gauntlet ===
    {"type": "block", "x": 48300, "y": 90, "w": 30, "h": 160},
    {"type": "block", "x": 48330, "y": 90, "w": 30, "h": 160},
    {"type": "spike", "x": 48315, "y": 250, "w": 30, "h": 30},
    {"type": "block", "x": 48500, "y": 210, "w": 30, "h": 160},
    {"type": "block", "x": 48530, "y": 210, "w": 30, "h": 160},
    {"type": "spike", "x": 48515, "y": 180, "w": 30, "h": 30},

    # === [95/100] Precision Low Ceiling Sprint ===
    {"type": "portal_cube", "x": 48700, "y": 150, "w": 45, "h": 220},
    {"type": "block", "x": 48900, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 48930, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 48960, "y": 0, "w": 30, "h": 220},
    {"type": "block", "x": 48990, "y": 0, "w": 30, "h": 220},
    {"type": "spike", "x": 48930, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 48990, "y": 335, "w": 30, "h": 35},

    # === [96/100] Multi-Pad Bounce Tower ===
    {"type": "pad_yellow", "x": 49150, "y": 360, "w": 30, "h": 10},
    {"type": "block", "x": 49300, "y": 200, "w": 30, "h": 170},
    {"type": "pad_yellow", "x": 49300, "y": 190, "w": 30, "h": 10},
    {"type": "block", "x": 49450, "y": 120, "w": 30, "h": 250},
    {"type": "block", "x": 49480, "y": 120, "w": 30, "h": 250},

    # === [97/100] Sky Island Precision Jump ===
    {"type": "block", "x": 49650, "y": 220, "w": 30, "h": 150},
    {"type": "spike", "x": 49650, "y": 190, "w": 30, "h": 30},
    {"type": "block", "x": 49850, "y": 180, "w": 30, "h": 190},
    {"type": "spike", "x": 49850, "y": 150, "w": 30, "h": 30},
    {"type": "block", "x": 50050, "y": 140, "w": 30, "h": 230},
    {"type": "spike", "x": 50050, "y": 110, "w": 30, "h": 30},

    # === [98/100] Quintuple Spike Pit ===
    {"type": "spike", "x": 50250, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 50285, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 50320, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 50355, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 50390, "y": 335, "w": 30, "h": 35},
    {"type": "ring_yellow", "x": 50320, "y": 200, "w": 30, "h": 30},

    # === [99/100] Final Runway Platform ===
    {"type": "block", "x": 50600, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 50630, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 50660, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 50690, "y": 280, "w": 30, "h": 90},
    {"type": "spike", "x": 50660, "y": 250, "w": 30, "h": 30},

    # === [100/100] Grand Finale Podium Pre-approach ===
    {"type": "block", "x": 50850, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 50880, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 50910, "y": 310, "w": 30, "h": 60},
    {"type": "block", "x": 50940, "y": 310, "w": 30, "h": 60},
# === [101/100] Final Extreme Spike Array ===
    {"type": "spike", "x": 51100, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 51135, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 51170, "y": 335, "w": 30, "h": 35},
    {"type": "spike", "x": 51205, "y": 335, "w": 30, "h": 35},
    {"type": "pad_yellow", "x": 51300, "y": 360, "w": 30, "h": 10},

    # === [102/100] Ultimate Sky Ring Leap ===
    {"type": "ring_yellow", "x": 51450, "y": 250, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 51600, "y": 200, "w": 30, "h": 30},
    {"type": "ring_yellow", "x": 51750, "y": 150, "w": 30, "h": 30},

    # === [103/100] Victory Gate & Grand Finale Finish Line ===
    {"type": "block", "x": 51900, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 51930, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 51960, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 51990, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 52020, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 52050, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 52080, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 52110, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 52140, "y": 280, "w": 30, "h": 90},
    {"type": "block", "x": 52170, "y": 280, "w": 30, "h": 90}
]
# 8번째, 9번째 가시/오브젝트 위치 보정 (필요시 데이터 배열 수정)
if len(MAP_OBJECTS) >= 9:
    spikes = [obj for obj in MAP_OBJECTS if obj.get("type") == "spike"]
    if len(spikes) >= 9:
        # 8번째와 9번째 가시 간격을 점프 가능한 자연스러운 동선으로 보정
        spikes[7]["x"] = spikes[6]["x"] + 180
        spikes[8]["x"] = spikes[7]["x"] + 180

# 맵 데이터에 비행기 변신 포탈 및 다시 큐브로 돌아오는 포탈 자동 삽입
has_portal = any(obj.get("type") in ["portal_ship", "portal_cube"] for obj in MAP_OBJECTS)
if not has_portal:
    # 2000px 지점에 비행기 포탈, 6000px 지점에 큐브 복귀 포탈 배치
    MAP_OBJECTS.append({"type": "portal_ship", "x": 2000, "y": 260, "w": 40, "h": 80})
    MAP_OBJECTS.append({"type": "portal_cube", "x": 6000, "y": 260, "w": 40, "h": 80})

map_json = json.dumps(MAP_OBJECTS)

game_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; background-color: #0b0b12; text-align: center; color: white; font-family: 'Segoe UI', Arial, sans-serif; overflow: hidden; }}
        canvas {{ border: 2px solid #00ffc8; box-shadow: 0 0 20px rgba(0, 255, 200, 0.3); border-radius: 8px; display: block; margin: 10px auto; background: linear-gradient(to bottom, #0d0d1a, #1a1a3a); }}
        .info {{ font-size: 13px; color: #8a8ab0; margin-top: 6px; font-weight: bold; }}
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="800" height="450"></canvas>
    <div class="info">⌨️ [스페이스바] / [위쪽 화살표] / [클릭 꾹 누르기] : 큐브(점프) | 비행기(상승) | [R] : 재시작</div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const mapObjects = {map_json};
        const finishX = 52100;

        let player = {{
            x: 100, y: 340, size: 30, vy: 0, rotation: 0,
            mode: "cube", isGrounded: true, isDead: false, isWin: false,
            trail: []
        }};

        let isHoldingJump = false;
        let particles = [];
        const gravity = 0.8;
        const jumpForce = -13.0;
        const speedX = 6.0;

        function tryJump() {{
            if (!player.isDead && !player.isWin && player.mode === "cube" && player.isGrounded) {{
                player.vy = jumpForce;
                player.isGrounded = false;
                createParticles(player.x + 15, player.y + 30, "#00ffc8");
            }}
        }}

        function reset() {{
            player.x = 100; player.y = 340; player.vy = 0; player.rotation = 0;
            player.mode = "cube"; player.isGrounded = true; player.isDead = false; player.isWin = false;
            player.trail = []; particles = []; isHoldingJump = false;
        }}

        function createParticles(x, y, color) {{
            for (let i = 0; i < 6; i++) {{
                particles.push({{
                    x: x, y: y,
                    vx: (Math.random() - 0.5) * 4, vy: Math.random() * 3 + 1,
                    life: 1, color: color
                }});
            }}
        }}

        window.addEventListener("keydown", (e) => {{
            if (e.code === "Space" || e.code === "ArrowUp") {{
                if (!isHoldingJump) {{
                    isHoldingJump = true;
                    tryJump();
                }}
                e.preventDefault();
            }}
            if (e.code === "KeyR") reset();
        }});

        window.addEventListener("keyup", (e) => {{
            if (e.code === "Space" || e.code === "ArrowUp") {{
                isHoldingJump = false;
            }}
        }});

        canvas.addEventListener("mousedown", () => {{
            isHoldingJump = true;
            tryJump();
        }});
        window.addEventListener("mouseup", () => {{
            isHoldingJump = false;
        }});

        function update() {{
            if (player.isDead || player.isWin) return;

            player.x += speedX;

            // 모드별 물리 계산
            if (player.mode === "cube") {{
                player.vy += gravity;
                if (!player.isGrounded) player.rotation += 8;
                else player.rotation = Math.round(player.rotation / 90) * 90;
            }} else if (player.mode === "ship") {{
                if (isHoldingJump) player.vy -= 0.65; // 부드러운 상승
                else player.vy += 0.55; // 부드러운 하강

                player.vy = Math.max(-8, Math.min(8, player.vy));
                player.rotation = player.vy * 4; // 비행기 기울기
            }}

            player.y += player.vy;
            player.isGrounded = false;

            // 기본 바닥/천장 한계선
            if (player.y >= 340) {{
                player.y = 340;
                player.vy = 0;
                player.isGrounded = true;
            }}
            if (player.y <= 0) {{
                player.y = 0;
                player.vy = 0;
            }}

            // 잔상 효과
            player.trail.push({{ x: player.x, y: player.y, rotation: player.rotation, alpha: 0.5, mode: player.mode }});
            if (player.trail.length > 5) player.trail.shift();

            // 파티클
            for (let i = particles.length - 1; i >= 0; i--) {{
                let p = particles[i];
                p.x += p.vx; p.y += p.vy; p.life -= 0.05;
                if (p.life <= 0) particles.splice(i, 1);
            }}

            // 충돌 판정 개선 (순간이동 없는 연속 바운딩 박스)
            for (let obj of mapObjects) {{
                if (obj.x > player.x + 800 || obj.x + obj.w < player.x - 200) continue;

                if (obj.type === "spike") {{
                    const margin = 7;
                    if (player.x + player.size - margin > obj.x + margin &&
                        player.x + margin < obj.x + obj.w - margin &&
                        player.y + player.size - margin > obj.y + margin &&
                        player.y + margin < obj.y + obj.h) {{
                        player.isDead = true;
                    }}
                }} 
                else if (obj.type === "block") {{
                    if (player.x + player.size > obj.x && player.x < obj.x + obj.w) {{
                        let nextBottom = player.y + player.size;
                        let prevBottom = nextBottom - player.vy;

                        // 부드러운 상단 착지 판정
                        if (prevBottom <= obj.y + 10 && nextBottom >= obj.y) {{
                            player.y = obj.y - player.size;
                            player.vy = 0;
                            player.isGrounded = true;
                        }} 
                        // 측면 충돌 (사망)
                        else if (player.y + player.size > obj.y + 6 && player.y < obj.y + obj.h - 6) {{
                            player.isDead = true;
                        }}
                    }}
                }} 
                else if (obj.type === "portal_ship") {{
                    if (player.x + player.size > obj.x && player.x < obj.x + obj.w &&
                        player.y + player.size > obj.y && player.y < obj.y + obj.h) {{
                        if (player.mode !== "ship") {{
                            player.mode = "ship";
                            createParticles(player.x, player.y, "#ff00d2");
                        }}
                    }}
                }} 
                else if (obj.type === "portal_cube") {{
                    if (player.x + player.size > obj.x && player.x < obj.x + obj.w &&
                        player.y + player.size > obj.y && player.y < obj.y + obj.h) {{
                        if (player.mode !== "cube") {{
                            player.mode = "cube";
                            createParticles(player.x, player.y, "#00ffc8");
                        }}
                    }}
                }}
            }}

            // 연속 자동 점프
            if (player.mode === "cube" && player.isGrounded && isHoldingJump) {{
                tryJump();
            }}

            if (player.x >= finishX) player.isWin = true;
        }}

        function drawPlayer(x, y, size, rotation, mode, alpha = 1.0) {{
            ctx.save();
            ctx.globalAlpha = alpha;
            ctx.translate(x + size / 2, y + size / 2);
            ctx.rotate((rotation * Math.PI) / 180);

            let half = size / 2;

            if (mode === "cube") {{
                ctx.fillStyle = "#00ffc8"; ctx.fillRect(-half, -half, size, size);
                ctx.fillStyle = "#0b0b12"; ctx.fillRect(-half + 3, -half + 3, size - 6, size - 6);
                ctx.fillStyle = "#00ffc8"; ctx.fillRect(-half + 6, -half + 6, size - 12, size - 12);
                ctx.fillStyle = "#ffffff"; ctx.fillRect(-half + 7, -half + 8, 5, 7); ctx.fillRect(-half + 18, -half + 8, 5, 7);
                ctx.fillStyle = "#000000"; ctx.fillRect(-half + 9, -half + 10, 3, 4); ctx.fillRect(-half + 20, -half + 10, 3, 4);
                ctx.fillRect(-half + 9, -half + 20, 12, 3);
            }} else if (mode === "ship") {{
                // 비행기 그래픽
                ctx.fillStyle = "#ff00d2";
                ctx.beginPath();
                ctx.moveTo(-half - 5, 0); ctx.lineTo(half + 5, -half + 5); ctx.lineTo(half + 5, half - 5);
                ctx.closePath(); ctx.fill();
                ctx.fillStyle = "#ffffff"; ctx.fillRect(-3, -5, 10, 10);
            }}

            ctx.restore();
        }}

        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const camX = player.x - 150;

            // 격자 배경
            ctx.strokeStyle = "rgba(255, 255, 255, 0.03)";
            ctx.lineWidth = 1;
            for (let x = -(camX % 40); x < canvas.width; x += 40) {{
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
            }}

            // 바닥
            ctx.fillStyle = "#07070f";
            ctx.fillRect(0, 370, canvas.width, 80);
            ctx.strokeStyle = "#00ffc8"; ctx.lineWidth = 3;
            ctx.shadowColor = "#00ffc8"; ctx.shadowBlur = 10;
            ctx.beginPath(); ctx.moveTo(0, 370); ctx.lineTo(canvas.width, 370); ctx.stroke();
            ctx.shadowBlur = 0;

            // 오브젝트 렌더링
            for (let obj of mapObjects) {{
                let sx = obj.x - camX;
                if (sx >= -60 && sx <= canvas.width + 60) {{
                    if (obj.type === "block") {{
                        ctx.fillStyle = "#1e1e38"; ctx.fillRect(sx, obj.y, obj.w, obj.h);
                        ctx.strokeStyle = "#00d2ff"; ctx.lineWidth = 2; ctx.strokeRect(sx, obj.y, obj.w, obj.h);
                    }} else if (obj.type === "spike") {{
                        ctx.fillStyle = "#ff2a6d"; ctx.beginPath();
                        ctx.moveTo(sx, obj.y + obj.h); ctx.lineTo(sx + obj.w / 2, obj.y); ctx.lineTo(sx + obj.w, obj.y + obj.h);
                        ctx.closePath(); ctx.fill();
                        ctx.strokeStyle = "#ff7597"; ctx.lineWidth = 1.5; ctx.stroke();
                    }} else if (obj.type === "portal_ship") {{
                        ctx.fillStyle = "rgba(255, 0, 210, 0.3)"; ctx.fillRect(sx, obj.y, obj.w, obj.h);
                        ctx.strokeStyle = "#ff00d2"; ctx.lineWidth = 3; ctx.strokeRect(sx, obj.y, obj.w, obj.h);
                    }} else if (obj.type === "portal_cube") {{
                        ctx.fillStyle = "rgba(0, 255, 200, 0.3)"; ctx.fillRect(sx, obj.y, obj.w, obj.h);
                        ctx.strokeStyle = "#00ffc8"; ctx.lineWidth = 3; ctx.strokeRect(sx, obj.y, obj.w, obj.h);
                    }}
                }}
            }}

            // 잔상 효과
            for (let t of player.trail) {{
                drawPlayer(t.x - camX, t.y, player.size, t.rotation, t.mode, t.alpha * 0.4);
                t.alpha -= 0.08;
            }}

            // 파티클
            for (let p of particles) {{
                ctx.fillStyle = p.color; ctx.globalAlpha = p.life; ctx.fillRect(p.x - camX, p.y, 4, 4);
            }}
            ctx.globalAlpha = 1.0;

            // 플레이어 그리기
            if (!player.isDead) {{
                drawPlayer(player.x - camX, player.y, player.size, player.rotation, player.mode, 1.0);
            }}

            // UI
            let progress = Math.min(100, Math.floor((player.x / finishX) * 100));
            ctx.fillStyle = "#ffffff"; ctx.font = "bold 18px 'Segoe UI'";
            ctx.fillText(progress + "%", 20, 35);

            if (player.isDead) {{
                ctx.fillStyle = "#ff2a6d"; ctx.font = "bold 28px 'Segoe UI'"; ctx.textAlign = "center";
                ctx.fillText("💥 GAME OVER", canvas.width / 2, 200);
                ctx.font = "16px 'Segoe UI'"; ctx.fillStyle = "#aaa";
                ctx.fillText("Press 'R' or Space to Retry", canvas.width / 2, 235);
            }} else if (player.isWin) {{
                ctx.fillStyle = "#00ffc8"; ctx.font = "bold 28px 'Segoe UI'"; ctx.textAlign = "center";
                ctx.fillText("🏆 STAGE CLEAR!!", canvas.width / 2, 200);
            }}
        }}

        function gameLoop() {{ update(); draw(); requestAnimationFrame(gameLoop); }}
        gameLoop();
    </script>
</body>
</html>
"""

components.html(game_html, height=530)
