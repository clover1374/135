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
    {"type": "block", "x": 46510, "y": 310, "w": 30, "h": 60}
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
    {"type": "block", "x": 50940, "y": 310, "w": 30, "h": 60}
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
import pygame
import sys

# --- 게임 시작 초기화 ---
pygame.init()
pygame.mixer.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash - Mega Edition (2000+ Objects)")
clock = pygame.time.Clock()
FPS = 60

# 색상 정의
COLOR_BG = (18, 18, 28)
COLOR_FLOOR = (10, 10, 18)
COLOR_LINE = (0, 255, 200)
COLOR_CUBE = (0, 255, 128)
COLOR_SHIP = (255, 128, 0)
COLOR_SPIKE = (255, 50, 50)
COLOR_BLOCK = (40, 40, 70)
COLOR_BLOCK_BORDER = (100, 100, 150)
COLOR_RING_YELLOW = (255, 230, 0)
COLOR_PAD_YELLOW = (255, 255, 0)
COLOR_PORTAL_SHIP = (255, 120, 0)
COLOR_PORTAL_CUBE = (0, 200, 255)

# 플레이어 클래스
class Player:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = 100
        self.y = 330
        self.w = 30
        self.h = 30
        self.vy = 0
        self.mode = "cube"  # "cube" 또는 "ship"
        self.is_grounded = False
        self.angle = 0
        self.is_dead = False
        self.win = False

    def update(self, keys, map_objects):
        if self.is_dead or self.win:
            return

        # 자동 전진 (x축 이동)
        self.x += 6.5

        # 모드별 중력 및 점프/상승 처리
        if self.mode == "cube":
            self.vy += 0.8  # 중력
            if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.is_grounded:
                self.vy = -12.5
                self.is_grounded = False

            # 공중 회전 효과
            if not self.is_grounded:
                self.angle = (self.angle - 8) % 360
            else:
                self.angle = round(self.angle / 90) * 90

        elif self.mode == "ship":
            # 비행선 모드: 누르고 있으면 상승, 떼면 하강
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                self.vy -= 0.65
            else:
                self.vy += 0.65

            # 속도 제한 및 각도 연출
            self.vy = max(-7, min(7, self.vy))
            self.angle = -self.vy * 4

        # y축 위치 업데이트
        self.y += self.vy

        # 바닥 기본 충돌 (y = 340)
        if self.y + self.h >= 370:
            self.y = 370 - self.h
            self.vy = 0
            self.is_grounded = True

        # 오브젝트 충돌 검사
        player_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        
        for obj in map_objects:
            # 화면 근처에 있는 오브젝트만 충돌 처리 (성능 최적화)
            if obj["x"] > self.x + 800 or obj["x"] + obj["w"] < self.x - 200:
                continue

            obj_rect = pygame.Rect(obj["x"], obj["y"], obj["w"], obj["h"])

            if player_rect.colliderect(obj_rect):
                o_type = obj["type"]

                # 1. 가시 충돌 -> 사망
                if o_type == "spike":
                    self.is_dead = True

                # 2. 블록 충돌
                elif o_type == "block":
                    # 위에서 착지
                    if self.vy >= 0 and self.y + self.h - self.vy <= obj["y"] + 5:
                        self.y = obj["y"] - self.h
                        self.vy = 0
                        self.is_grounded = True
                    # 아래에서 머리 부딪힘
                    elif self.vy < 0 and self.y - self.vy >= obj["y"] + obj["h"] - 5:
                        self.y = obj["y"] + obj["h"]
                        self.vy = 0
                    # 측면 부딪힘 -> 사망
                    else:
                        self.is_dead = True

                # 3. 노란 패드 (밟으면 자동 점프)
                elif o_type == "pad_yellow":
                    self.vy = -15
                    self.is_grounded = False

                # 4. 노란 링 (공중에서 누르면 점프)
                elif o_type == "ring_yellow":
                    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                        self.vy = -12
                        self.is_grounded = False

                # 5. 비행선 포탈
                elif o_type == "portal_ship":
                    self.mode = "ship"

                # 6. 큐브 포탈
                elif o_type == "portal_cube":
                    self.mode = "cube"

        # 골인 지점 도달 확인 (최종 52,100 좌표)
        if self.x >= 52100:
            self.win = True


# --- 메인 게임 루프 ---
player = Player()

running = True
while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # R 키로 언제든 리셋
            if event.key == pygame.K_r:
                player.reset()
            # 사망 시 아무 키나 누르면 재시작
            elif player.is_dead:
                player.reset()

    # 플레이어 위치 업데이트
    player.update(keys, MAP_OBJECTS)

    # 카메라 추적 (x축 관전)
    camera_x = player.x - 150

    # 화면 그리기 (배경 & 바닥)
    screen.fill(COLOR_BG)
    pygame.draw.rect(screen, COLOR_FLOOR, (0, 370, SCREEN_WIDTH, 80))
    pygame.draw.line(screen, COLOR_LINE, (0, 370), (SCREEN_WIDTH, 370), 2)

    # 맵 오브젝트 그리기
    for obj in MAP_OBJECTS:
        screen_x = obj["x"] - camera_x

        # 화면 내에 있는 오브젝트만 그리기 (성능 최적화)
        if -50 <= screen_x <= SCREEN_WIDTH + 50:
            o_type = obj["type"]
            rect = (screen_x, obj["y"], obj["w"], obj["h"])

            if o_type == "block":
                pygame.draw.rect(screen, COLOR_BLOCK, rect)
                pygame.draw.rect(screen, COLOR_BLOCK_BORDER, rect, 2)

            elif o_type == "spike":
                points = [
                    (screen_x, obj["y"] + obj["h"]),
                    (screen_x + obj["w"] / 2, obj["y"]),
                    (screen_x + obj["w"], obj["y"] + obj["h"])
                ]
                pygame.draw.polygon(screen, COLOR_SPIKE, points)

            elif o_type == "pad_yellow":
                pygame.draw.rect(screen, COLOR_PAD_YELLOW, rect)

            elif o_type == "ring_yellow":
                pygame.draw.ellipse(screen, COLOR_RING_YELLOW, rect, 3)

            elif o_type == "portal_ship":
                pygame.draw.rect(screen, COLOR_PORTAL_SHIP, rect, 3)

            elif o_type == "portal_cube":
                pygame.draw.rect(screen, COLOR_PORTAL_CUBE, rect, 3)

    # 플레이어 그리기 (회전 적용)
    if not player.is_dead:
        p_color = COLOR_CUBE if player.mode == "cube" else COLOR_SHIP
        p_surf = pygame.Surface((player.w, player.h), pygame.SRCALPHA)
        p_surf.fill(p_color)
        
        # 회전 연출
        rotated_surf = pygame.transform.rotate(p_surf, player.angle)
        new_rect = rotated_surf.get_rect(center=(player.x - camera_x + player.w / 2, player.y + player.h / 2))
        screen.blit(rotated_surf, new_rect.topleft)

    # UI / 안내 메시지 표시 (최종 길이에 맞춘 진행도 계산)
    font = pygame.font.SysFont("arial", 24, bold=True)
    progress = min(100, int((player.x / 52100) * 100))
    txt_progress = font.render(f"Progress: {progress}%", True, (255, 255, 255))
    screen.blit(txt_progress, (20, 20))

    if player.is_dead:
        txt_dead = font.render("Game Over! Press Any Key / R to Restart", True, (255, 80, 80))
        screen.blit(txt_dead, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))

    if player.win:
        txt_win = font.render("STAGE CLEAR!! Press R to Play Again", True, (80, 255, 120))
        screen.blit(txt_win, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()
