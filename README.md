# STATisfactory

Webapp to visualise statistics about resources consumption in game and their real-life equivalent.

## Tech

### Setup

1. Clone: `git clone XXX`
2. Create and activate venv: `python -m venv env; source env/bin/activate`
3. Install: `pip install -Ur requirements.txt`
4. Copy and edit file: `cp webapp/config.py.dist webapp/config.py`
5. _Tada_

### Usage

1. Activate venv if not done alread: `source env/bin/activate`
2. Launch webapp: `python wsgi.py`
3. Access localhost: https://0.0.0.0:8008 (or whatever address you configured)

## Documentation

You can generate a new funfacts file using `download_expand_and_save_funfacts` in `webapp.utilities`.

### Resources

Listed here are [resources](https://satisfactory.wiki.gg/wiki/Resources) selected for real-life comparison. Choices were made in order to have some ease of use. For instance, Iron Ore can be mixed with Reanimated SAM to create Coal (Tier 9 - Matter Conversion), but this cannot be compared in real-life.

- [Iron Ore](https://satisfactory.wiki.gg/wiki/Iron_Ore)
  - Used to create Iron Ingot, Steel Ingot, Copper Ingot.
  - In game, 1 unit of Iron Ore gives 1 unit of [Iron Ingot](https://satisfactory.wiki.gg/wiki/Iron_Ingot), which has 12 pieces on the image. We are going to use that 1 ingot is about 1kg ([source](https://fr.wikipedia.org/wiki/Lingot)).
  - Thus, 1 unit of Iron Ore in game is about 12kg of iron IRL.
- [Copper Ore](https://satisfactory.wiki.gg/wiki/Copper_Ore)
  - Used to create Copper Ingot, Iron Ingot.
  - 
  - 
- [Limestone](https://satisfactory.wiki.gg/wiki/Limestone)
  - Used to create Concrete, Iron Ingot, Silica.
  - 
  - 
- [Coal](https://satisfactory.wiki.gg/wiki/Coal)
  - Used to create Aluminium Scrap, Black Powder, Steel Ingot, Compacted Coal, Rocket Fuel.
  - In game, 1 unit of Coal gives 300MJ of Energy. 300MJ is about 10.24kg of [Coal](https://en.wikipedia.org/wiki/Coal).
  - Thus, 1 unit of Coal in game is about 10.24kg of coal IRL.
- [Water](https://satisfactory.wiki.gg/wiki/Water)
  - Used to create [quite a lot of things](https://satisfactory.wiki.gg/wiki/Water#Crafting_2).
  - In game, units are m3.
  - Thus, 1 unit of Water in game is about 1 m3 of water IRL.
- [Crude Oil](https://satisfactory.wiki.gg/wiki/Crude_Oil)
  - Used to create Fuel, Polymer, Packaged Oil, Plastic, Rubber.
  - In game, 1 unit of Crude Oil gives 320MJ of Energy. 320MJ is about 0.05 [Barrel of oil](https://en.wikipedia.org/wiki/Tonne_of_oil_equivalent).
  - Thus, 1 unit of Crude Oil in game is about 0.05 boi IRL.
- [Caterium Ore](https://satisfactory.wiki.gg/wiki/Caterium_Ore) ~= [Gold](https://satisfactory.wiki.gg/wiki/Caterium_Ore#Trivia)
  - Used to create Caterium Ingot.
  - 
  - 
- [Bauxite](https://satisfactory.wiki.gg/wiki/Bauxite)
  - Used to create Alumina Solution, Silica.
  - 
  - 
- [Raw Quartz](https://satisfactory.wiki.gg/wiki/Raw_Quartz)
  - Used to create Quartz Crystal, Silica.
  - 
  - 
- [Sulfur](https://satisfactory.wiki.gg/wiki/Sulfur)
  - Used to create Black Powder, Sulfuric Acid, Battery, Rocket Fuel.
  - 
  - 
- [Uranium](https://satisfactory.wiki.gg/wiki/Uranium)
  - Used to create Encased Uranium Cell, Non-Fissile Uranium.
  - In game, 1 [Uranium Fuel Rod](https://satisfactory.wiki.gg/wiki/Uranium_Fuel_Rod) gives 750'000MJ of Energy, and is made of 50 [Encased Uranium Cell](https://satisfactory.wiki.gg/wiki/Encased_Uranium_Cell), which are made of 100 units of Uranium. So, 1 unit of Uranium gives 7'500MJ of Energy. 1kg of Uranium gives about 500'000MJ Energy ([source](https://fr.wikipedia.org/wiki/Uranium#Produit_fissile_naturel)), so 0.015kg of Uranium gives 7'500MJ of Energy.
  - Thus, 1 unit of Uranium in game is about 0.015kg of uranium IRL.
- [Wood](https://satisfactory.wiki.gg/wiki/Wood)
  - Used to created Biomass.
  - In game, 1 unit of Wood gives 100MJ of Energy. Wood has what appears to be log wood on the image. Log wood has an energy density by volume of about 6'300 MJ/m3 ([source](https://www.forestresearch.gov.uk/tools-and-resources/fthr/biomass-energy-resources/reference-biomass/facts-figures/typical-calorific-values-of-fuels/)).
  - Thus, 1 unit of Wood in game is about 63 m3 of wood IRL.

### Real-life equivalent



## Credits

- [Satisfactory Wiki](https://satisfactory.wiki.gg/) used for documentation.
- [Unit Juggler](https://www.unitjuggler.com/index.html) used for conversions.
- Satisfactory web template inspired by [Satisfactory Tools](https://github.com/greeny/SatisfactoryTools).
- Satisfactory font used is [Satisfontory](https://natewren.com/satisfontory/) by [Nate Wren](https://natewren.com/), licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
- 
