# Belgica: a real-world map of Belgium for Nuclear Option

Belgica is a 200 x 200 km map of Belgium for [Nuclear Option](https://store.steampowered.com/app/2168680):
from the coast at Ostend to Leuven and Namur, with French Flanders and Hainaut, the south of Zeeland and
North Brabant, and a slice of the North Sea. It was made with [Open Skies](https://github.com/metasprojects/open-skies)
from real-world open data: terrain at 30 m, land cover, towns, roads and 10 real airbases.

![Belgica](docs/preview.jpg)

## Install

**With the Nuclear Option Mod Manager (NOMM):** search for **Belgica** and install it. NOCustomMaps comes with it.

**By hand:**

1. Install [BepInEx 5](https://github.com/BepInEx/BepInEx) and
   [NOCustomMaps](https://github.com/metasprojects/NOCustomMaps) 1.4 or later.
2. Download `belgica.zip` from [Releases](https://github.com/therealabradolf/nuclear-option-belgica/releases).
3. Unzip it into `<Nuclear Option>\BepInEx\plugins\NOCustomMaps\maps\`.
4. Start the game. Belgica is in the Mission Editor's **New** list.

Every player in a multiplayer game needs the same build of the map. Don't rebuild it yourself: a rebuild
counts as a different map.

## Airbases

| North (Boscali) | South (Primeva) |
| --- | --- |
| Brussels (EBBR) | Brussels South Charleroi (EBCI) |
| Antwerp Deurne (EBAW) | Beauvechain (EBBE) |
| Ostend-Bruges (EBOS) | Florennes (EBFS) |
| Kortrijk-Wevelgem (EBKT) | Lille (LFQQ) |
| Gilze-Rijen (EHGR) | Valenciennes-Denain (LFAV) |

## Missions

The map ships with Open Skies' own Free Flight, Escalation and two Strike missions.

**Fault Line** is a five-mission campaign on the [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3843138468): a fictional war in which the country splits along
the language border. North (Dutch-speaking) flies as Boscali, South (French-speaking) as Primeva. Nuclear
weapons are off in every mission. The missions need this exact build of the map (`cm.belgica.977b8a61`).

1. **Broken Sky**: air strike on the southern air defence network (solo or co-op as the North)
2. **Hainaut Offensive**: southern armoured offensive on the language border (both sides)
3. **North Sea**: amphibious landing at Westende to take Ostend-Bruges (both sides)
4. **Meuse Crossing**: northern counter-offensive towards Namur and the Meuse (both sides)
5. **Battle for Brussels**: every airbase in play (both sides)

Subscribe to the [Fault Line collection](https://steamcommunity.com/sharedfiles/filedetails/?id=3843138468) on the Steam Workshop. The mission files are also in [`missions/`](missions/), for reference.

## Build notes

The first build covered 261 km and took about 100 seconds to load, because 95% of the bundle is terrain and
road geometry. This version covers 200 km.

Belgium's road network is so dense that the full network can have more records than the NOCustomMaps loader
accepts (108,475 against a limit of 100,000 at 261 km). The build uses a patched `pipeline/roads.py`
([`tools/roads-thinning.patch`](tools/roads-thinning.patch)). When a network is over the limit, the patch
leaves out the tertiary roads to towns first. Then, in the densest town centres, it treats secondary roads as
tertiary, so they stay only where they join parts of the network.

## Credits

See [CREDITS.txt](CREDITS.txt) for the full data credits and licence notices (Copernicus DEM, ESA WorldCover,
OpenStreetMap / Overture Maps, OurAirports, AWS Terrain Tiles).

This is an unofficial community modification. It is not affiliated with, sponsored by or endorsed by
Shockfront Studios Pty Ltd. It contains no game files. Mods for Nuclear Option may not be sold or put
behind a paywall.
