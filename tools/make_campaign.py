"""Fault Line: a five-mission campaign for the Belgica map (Open Skies), built with Open Skies' own
scenario templates (pipeline/scenarios.py), placement checker and strict mission lint.

Story: a failed state reform splits the country along the language border. The North (Dutch-speaking,
flown as Boscali) holds Brussels at the start; the South (French-speaking, flown as Primeva) wants it.
Neither side is the villain. Nuclear weapons are off in every mission.

Usage: make_campaign.py <pipeline dir> <map.json> <build dir> <prefab cm.belgica.xxxxxxxx> <out dir>
"""
import json
import sys
from pathlib import Path

PIPELINE, CFG, BUILD, PREFAB, OUT = sys.argv[1:6]
sys.path.insert(0, PIPELINE)

import missions  # noqa: E402
import scenarios  # noqa: E402

# No nuclear weapons anywhere in the campaign (the Escalation template hands out 16 warheads per side).
_faction = missions.MissionBuilder.faction


def _no_nukes(self, name, **kw):
    kw["warheads"] = 0
    kw["reserve_warheads"] = 0
    return _faction(self, name, **kw)


missions.MissionBuilder.faction = _no_nukes

N, S = "Boscali", "Primeva"
REQ = ("Requires NOCustomMaps and the Belgica map (Nuclear Option Mod Manager). Fictional scenario: "
       "North = Boscali, South = Primeva. No nuclear weapons.")


def title(n, name):
    return f"Belgica - Fault Line {n} - {name}"


# ------------------------------------------------------------------------------------------------ 1
STRIKE = {
    "title": title(1, "Broken Sky"),
    "attacker": N,
    "time": 5.9, "weather": 0.35, "rank": 3, "minutes": 45, "percent": 0.7,
    "ai": {N: 3, S: 4},
    "bareBasesOk": True,
    "display": "Destroy the southern radar and air defence network",
    "description": (
        "FAULT LINE 1/5 - BROKEN SKY. Day one. The federal government has fallen and the army has split along "
        "the language border. The South has switched on its radars and SAMs around Beauvechain and Chievres; while "
        "they stand, nothing northern can fly south of Brussels. Fly as the North from Brussels, Kleine Brogel or "
        "Kortrijk and take the network apart: the early-warning radars, the SAM batteries and the fuel at "
        "Beauvechain. 45 minutes. Solo or co-op; the South is flown by the AI. " + REQ),
    "targets": [
        {"name": "Radar Beauvechain", "type": "radarStation1", "base": "Beauvechain Air Base", "extra": 700},
        {"name": "Fuel Beauvechain", "type": "fuelTank1", "base": "Beauvechain Air Base", "extra": 1100,
         "count": 2, "spacing": 90},
        {"name": "Radar Chievres", "type": "radarStation1", "base": "Chievres Air Base", "extra": 700},
        {"name": "Radar Wavre", "type": "radarStation1", "lat": 50.705, "lon": 4.585},
        {"name": "SAM Wavre", "type": "RadarSAM1", "lat": 50.712, "lon": 4.600},
        {"name": "SAM Nivelles", "type": "RadarSAM1", "lat": 50.600, "lon": 4.330},
    ],
    "sams": [
        {"lat": 50.712, "lon": 4.600, "launchers": 4, "aaa": 2},     # Wavre, guarding the road to Brussels
        {"lat": 50.600, "lon": 4.330, "launchers": 3, "aaa": 2},     # Nivelles
        {"lat": 50.480, "lon": 3.950, "launchers": 3, "aaa": 2},     # Mons
    ],
    "baseRings": ["Beauvechain Air Base", "Chievres Air Base", "Brussels South Charleroi Airport"],
    "intel": [
        "North, this is Brussels Control. Southern radars at Beauvechain, Chievres and Wavre are painting "
        "everything north of the language border.",
        "SAM batteries at Wavre and Nivelles cover the approach. Go low, kill the radars first, then the launchers.",
        "Southern fighters are airborne. Expect company.",
        "Destroy most of the network and the sky over Brabant is ours.",
    ],
    "winText": "The southern air defence network is down. The North owns the sky over Brabant - for now.",
}

# ------------------------------------------------------------------------------------------------ 2
OFFENSIVE_HAINAUT = {
    "title": title(2, "Hainaut Offensive"),
    "attacker": S,
    "time": 6.2, "weather": 0.3,
    "aiAttacker": 6, "aiDefender": 6,
    "description": (
        "FAULT LINE 2/5 - HAINAUT OFFENSIVE. The South answers on the ground. Three armoured columns roll north "
        "out of Hainaut towards Ronse, Geraardsbergen and Halle, behind a rocket artillery screen near Chievres. "
        "The North holds a thin line along the language border and has a reserve at Aalst. "
        "SOUTH: break 70% of the northern line. NORTH: destroy 75% of the three columns. "
        "Both sides playable: PvP, or co-op against the AI. " + REQ),
    "line": [[50.735, 3.600], [50.760, 3.880], [50.715, 4.220]],
    "lineHeading": 180.0,
    "waves": [
        {"assembly": [50.605, 3.420], "crossing": [50.680, 3.560], "target": 0, "at": 120,
         "text": "First column moving from Tournai towards Ronse."},
        {"assembly": [50.630, 3.770], "crossing": [50.705, 3.850], "target": 1, "at": 600,
         "text": "Second column through Lessines, heading for Geraardsbergen."},
        {"assembly": [50.585, 4.060], "crossing": [50.680, 4.060], "target": 2, "at": 1080,
         "text": "Third column out of Soignies, driving on Halle and the road to Brussels."},
    ],
    "artillery": [50.560, 3.880],
    "attackerSams": [{"lat": 50.520, "lon": 3.800, "launchers": 3, "aaa": 2}],
    "defenderSams": [{"lat": 50.850, "lon": 3.620, "launchers": 3, "aaa": 2},
                     {"lat": 50.790, "lon": 4.150, "launchers": 3, "aaa": 2}],
    "attackerBaseRings": ["Chievres Air Base"],
    "defenderBaseRings": ["Kortrijk-Wevelgem International Airport"],
    "reserve": {"from": [50.935, 4.040], "to": [50.775, 3.890]},
    "text": {
        "a1": "South, the offensive begins. Keep their aircraft off our columns and open the way north.",
        "d1": "North, armour is massing in Hainaut. Hold the language border.",
        "d2": "Hit the columns at the crossings, and find the rocket artillery near Chievres.",
        "attackGoal": "Break the northern line at Ronse, Geraardsbergen and Halle",
        "defendGoal": "Destroy the southern armoured columns",
        "broken": "The northern line has collapsed. The road to Brussels is open.",
        "held": "The southern offensive has burned out in the Flemish Ardennes. The line holds.",
        "reserve": "The Aalst reserve is moving up to Geraardsbergen. Cover it.",
    },
}

# ------------------------------------------------------------------------------------------------ 3
LANDING = {
    "title": title(3, "North Sea"),
    "attacker": S,
    "target": "Ostend-Bruges International Airport",
    "time": 6.0, "weather": 0.4,
    "aiAttacker": 5, "aiDefender": 6,
    "description": (
        "FAULT LINE 3/5 - NORTH SEA. Stalled on land, the South goes around. An assault group with two "
        "assault carriers comes in from the west to land at Westende and take Ostend-Bruges airport, the "
        "North's window on the sea. The North has a small squadron off Zeebrugge, beach defences and a reserve "
        "in Bruges. SOUTH: capture Ostend-Bruges. NORTH: sink both assault carriers, and the landing craft before "
        "they reach the beach. Both sides playable: PvP, or co-op against the AI. " + REQ),
    "fleetStart": [51.520, 2.600],
    "landingZone": [51.215, 2.700],
    "beach": [51.168, 2.765],
    "beachhead": [51.150, 2.800],
    "craftStandoff": 400,
    "fleet": ["AssaultCarrier1", "AssaultCarrier1", "Destroyer1", "Destroyer1", "Frigate1", "Frigate1",
              "Corvette1", "Corvette1"],
    "fleetSpacing": 1200,
    "defences": [[51.158, 2.770], [51.190, 2.830]],
    "defenceHeading": 315.0,
    "reserve": {"from": [51.205, 3.200], "to": [51.185, 2.900]},
    "defenderSams": [{"lat": 51.230, "lon": 3.050, "launchers": 3, "aaa": 2}],
    "defenderBaseRings": ["Ostend-Bruges International Airport"],
    "attackerBaseRings": ["Merville-Calonne Airport"],
    "navy": {"at": [51.390, 3.150], "ships": ["Frigate1", "Corvette1", "Corvette1", "PatrolBoat1"]},
    "text": {
        "a1": "South, the assault group is closing the Flemish coast. Clear the beach at Westende before the "
              "craft go in.",
        "d1": "North, enemy fleet in the North Sea, heading for the coast. All units to Ostend.",
        "reserve": "The Bruges reserve is moving to Ostend. Keep the road clear.",
    },
}

# ------------------------------------------------------------------------------------------------ 4
OFFENSIVE_MEUSE = {
    "title": title(4, "Meuse Crossing"),
    "attacker": N,
    "time": 6.4, "weather": 0.25,
    "aiAttacker": 6, "aiDefender": 6,
    "description": (
        "FAULT LINE 4/5 - MEUSE CROSSING. The North strikes back in the east. From Sint-Truiden, Tongeren and "
        "the Voeren, three columns push south on the southern line north of Liege, with the crossing at Vise as "
        "the prize. Rocket artillery near Bilzen covers them. The South holds the line and has a reserve in "
        "Seraing. NORTH: break 70% of the southern line. SOUTH: destroy 75% of the three columns. "
        "Both sides playable: PvP, or co-op against the AI. " + REQ),
    "line": [[50.715, 5.450], [50.730, 5.580], [50.735, 5.690]],
    "lineHeading": 0.0,
    "waves": [
        {"assembly": [50.815, 5.190], "crossing": [50.780, 5.330], "target": 0, "at": 120,
         "text": "First column away from Sint-Truiden, heading south-east."},
        {"assembly": [50.800, 5.440], "crossing": [50.775, 5.540], "target": 1, "at": 600,
         "text": "Second column out of Tongeren, driving on Bassenge."},
        {"assembly": [50.755, 5.800], "crossing": [50.752, 5.730], "target": 2, "at": 1080,
         "text": "Third column out of the Voeren, going for the crossing at Vise."},
    ],
    "artillery": [50.870, 5.500],
    "attackerSams": [{"lat": 50.930, "lon": 5.340, "launchers": 3, "aaa": 2}],
    "defenderSams": [{"lat": 50.640, "lon": 5.570, "launchers": 4, "aaa": 2}],
    "attackerBaseRings": ["Maastricht Aachen Airport", "Kleine Brogel Air Base"],
    "defenderBaseRings": ["Liege Airport"],
    "reserve": {"from": [50.605, 5.500], "to": [50.700, 5.620]},
    "text": {
        "a1": "North, the counter-offensive begins. Cover the columns and get us across the Meuse.",
        "d1": "South, northern armour is moving out of Limburg. Hold the line north of Liege.",
        "d2": "Hit them at the crossings, and find the rocket artillery near Bilzen.",
        "attackGoal": "Break the southern line north of Liege",
        "defendGoal": "Destroy the northern armoured columns",
        "broken": "The southern line has broken. Northern armour is across at Vise.",
        "held": "The northern offensive has stalled on the plateau. Liege holds.",
        "reserve": "The Seraing reserve is moving up to Herstal. Cover it.",
    },
}

# ------------------------------------------------------------------------------------------------ 5
ESCALATION = {
    "title": title(5, "Battle for Brussels"),
    "time": 7.5, "weather": 0.2, "ai": 5, "bareBasesOk": True,
    "factories": {N: "Brussels Airport", S: "Brussels South Charleroi Airport"},
    "description": (
        "FAULT LINE 5/5 - BATTLE FOR BRUSSELS. Neither side can win the war in pieces. Every airbase on the map "
        "is now in play, and the North's war industry sits beside Brussels Airport, the South's beside Brussels "
        "South Charleroi. Income grows with every base you hold. Take every enemy airbase and destroy the enemy "
        "factories to end the war. Both sides playable: PvP, or co-op against the AI. Long mission. " + REQ),
    "brief": {
        N: "North, this is it. Hold Brussels, take every southern airbase and destroy the factories at Charleroi.",
        S: "South, this is it. Take Brussels and every northern airbase, and destroy the factories at Zaventem.",
    },
}


def main():
    out = Path(OUT)
    out.mkdir(parents=True, exist_ok=True)
    jobs = [(scenarios.strike, STRIKE), (scenarios.offensive, OFFENSIVE_HAINAUT), (scenarios.landing, LANDING),
            (scenarios.offensive, OFFENSIVE_MEUSE), (scenarios.escalation, ESCALATION)]
    failed = []
    for fn, spec in jobs:
        print(f"\n== {spec['title']}  ({len(spec['description'])} chars of description)")
        if fn(CFG, BUILD, PREFAB, str(out), spec) != 0:
            failed.append(spec["title"])
    print("\nFAILED:" if failed else "\nALL MISSIONS WRITTEN", failed or "")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
