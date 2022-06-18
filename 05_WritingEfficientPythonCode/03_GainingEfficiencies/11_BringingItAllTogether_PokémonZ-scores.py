# Bringing it all together: Pokémon z-scores
# A list of 720 Pokémon names.

import numpy as np

names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron', 'Aipom', 'Alakazam', 'Alomomola', 'Altaria', 'Amaura', 'Ambipom', 'Amoonguss', 'Ampharos', 'Anorith', 'Arbok', 'Arcanine', 'Arceus', 'Archen', 'Archeops', 'Ariados', 'Armaldo', 'Aromatisse', 'Aron', 'Articuno', 'Audino', 'Aurorus', 'Avalugg', 'Axew', 'Azelf', 'Azumarill', 'Azurill', 'Bagon', 'Baltoy', 'Banette', 'Barbaracle', 'Barboach', 'Basculin', 'Bastiodon', 'Bayleef', 'Beartic', 'Beautifly', 'Beedrill', 'Beheeyem', 'Beldum', 'Bellossom', 'Bellsprout', 'Bergmite', 'Bibarel', 'Bidoof', 'Binacle', 'Bisharp', 'Blastoise', 'Blaziken', 'Blissey', 'Blitzle', 'Boldore', 'Bonsly', 'Bouffalant', 'Braixen', 'Braviary', 'Breloom', 'Bronzong', 'Bronzor', 'Budew', 'Buizel', 'Bulbasaur', 'Buneary', 'Bunnelby', 'Burmy', 'Butterfree', 'Cacnea', 'Cacturne', 'Camerupt', 'Carbink', 'Carnivine', 'Carracosta', 'Carvanha', 'Cascoon', 'Castform', 'Caterpie', 'Celebi', 'Chandelure', 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 'Chatot', 'Cherrim', 'Cherubi', 'Chesnaught', 'Chespin', 'Chikorita', 'Chimchar', 'Chimecho', 'Chinchou', 'Chingling', 'Cinccino', 'Clamperl', 'Clauncher', 'Clawitzer', 'Claydol', 'Clefable', 'Clefairy', 'Cleffa', 'Cloyster', 'Cobalion', 'Cofagrigus', 'Combee', 'Combusken', 'Conkeldurr', 'Corphish', 'Corsola', 'Cottonee', 'Cradily', 'Cranidos', 'Crawdaunt', 'Cresselia', 'Croagunk', 'Crobat', 'Croconaw', 'Crustle', 'Cryogonal', 'Cubchoo', 'Cubone', 'Cyndaquil', 'Darkrai', 'DarmanitanStandard Mode', 'DarmanitanZen Mode', 'Darumaka', 'Dedenne', 'Deerling', 'Deino', 'Delcatty', 'Delibird', 'Delphox', 'Dewgong', 'Dewott', 'Dialga', 'Diancie', 'Diggersby', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 'Donphan', 'Doublade', 'Dragalge', 'Dragonair', 'Dragonite', 'Drapion', 'Dratini', 'Drifblim', 'Drifloon', 'Drilbur', 'Drowzee', 'Druddigon', 'Ducklett', 'Dugtrio', 'Dunsparce', 'Duosion', 'Durant', 'Dusclops', 'Dusknoir', 'Duskull', 'Dustox', 'Dwebble', 'Eelektrik', 'Eelektross', 'Eevee', 'Ekans', 'Electabuzz', 'Electivire', 'Electrike', 'Electrode', 'Elekid', 'Elgyem', 'Emboar', 'Emolga', 'Empoleon', 'Entei', 'Escavalier', 'Espeon', 'Espurr', 'Excadrill', 'Exeggcute', 'Exeggutor', 'Exploud', "Farfetch'd", 'Fearow', 'Feebas', 'Fennekin', 'Feraligatr', 'Ferroseed', 'Ferrothorn', 'Finneon', 'Flaaffy', 'Flabébé', 'Flareon', 'Fletchinder', 'Fletchling', 'Floatzel', 'Floette', 'Florges', 'Flygon', 'Foongus', 'Forretress', 'Fraxure', 'Frillish', 'Froakie', 'Frogadier', 'Froslass', 'Furfrou', 'Furret', 'Gabite', 'Gallade', 'Galvantula', 'Garbodor', 'Garchomp', 'Gardevoir', 'Gastly', 'Gastrodon', 'Genesect', 'Gengar', 'Geodude', 'Gible', 'Gigalith', 'Girafarig', 'Glaceon', 'Glalie', 'Glameow', 'Gligar', 'Gliscor', 'Gloom', 'Gogoat', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Golett', 'Golurk', 'Goodra', 'Goomy', 'Gorebyss', 'Gothita', 'Gothitelle', 'Gothorita', 'Granbull', 'Graveler', 'Greninja', 'Grimer', 'Grotle', 'Groudon', 'GroudonPrimal Groudon', 'Grovyle', 'Growlithe', 'Grumpig', 'Gulpin', 'Gurdurr', 'Gyarados', 'Happiny', 'Hariyama', 'Haunter', 'Hawlucha', 'Haxorus', 'Heatmor', 'Heatran', 'Heliolisk', 'Helioptile', 'Heracross', 'Herdier', 'Hippopotas', 'Hippowdon', 'Hitmonchan', 'Hitmonlee', 'Hitmontop', 'Ho-oh', 'Honchkrow', 'Honedge', 'Hoothoot', 'Hoppip', 'Horsea', 'Houndoom', 'Houndour', 'Huntail', 'Hydreigon', 'Hypno', 'Igglybuff', 'Illumise', 'Infernape', 'Inkay', 'Ivysaur', 'Jellicent', 'Jigglypuff', 'Jirachi', 'Jolteon', 'Joltik', 'Jumpluff', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan', 'Karrablast', 'Kecleon', 'Kingdra', 'Kingler', 'Kirlia', 'Klang', 'Klefki', 'Klink', 'Klinklang', 'Koffing', 'Krabby', 'Kricketot', 'Kricketune', 'Krokorok', 'Krookodile', 'Kyogre', 'KyogrePrimal Kyogre', 'Kyurem', 'KyuremBlack Kyurem', 'KyuremWhite Kyurem', 'Lairon', 'Lampent', 'Lanturn', 'Lapras', 'Larvesta', 'Larvitar', 'Latias', 'Latios', 'Leafeon', 'Leavanny', 'Ledian', 'Ledyba', 'Lickilicky', 'Lickitung', 'Liepard', 'Lileep', 'Lilligant', 'Lillipup', 'Linoone', 'Litleo', 'Litwick', 'Lombre', 'Lopunny', 'Lotad', 'Loudred', 'Lucario', 'Ludicolo', 'Lugia', 'Lumineon', 'Lunatone', 'Luvdisc', 'Luxio', 'Luxray', 'Machamp', 'Machoke', 'Machop', 'Magby', 'Magcargo', 'Magikarp', 'Magmar', 'Magmortar', 'Magnemite', 'Magneton', 'Magnezone', 'Makuhita', 'Malamar', 'Mamoswine', 'Manaphy', 'Mandibuzz', 'Manectric', 'Mankey', 'Mantine', 'Mantyke', 'Maractus', 'Mareep', 'Marill', 'Marowak', 'Marshtomp', 'Masquerain', 'Mawile', 'Medicham', 'Meditite', 'MeowsticFemale', 'MeowsticMale', 'Meowth', 'Mesprit', 'Metagross', 'Metang', 'Metapod', 'Mew', 'Mewtwo', 'Mienfoo', 'Mienshao', 'Mightyena', 'Milotic', 'Miltank', 'Mime Jr.', 'Minccino', 'Minun', 'Misdreavus', 'Mismagius', 'Moltres', 'Monferno', 'Mothim', 'Mr. Mime', 'Mudkip', 'Muk', 'Munchlax', 'Munna', 'Murkrow', 'Musharna', 'Natu', 'Nidoking', 'Nidoqueen', 'Nidoran♀', 'Nidoran♂', 'Nidorina', 'Nidorino', 'Nincada', 'Ninetales', 'Ninjask', 'Noctowl', 'Noibat', 'Noivern', 'Nosepass', 'Numel', 'Nuzleaf', 'Octillery', 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Oshawott', 'Pachirisu', 'Palkia', 'Palpitoad', 'Pancham', 'Pangoro', 'Panpour', 'Pansage', 'Pansear', 'Paras', 'Parasect', 'Patrat', 'Pawniard', 'Pelipper', 'Persian', 'Petilil', 'Phanpy', 'Phantump', 'Phione', 'Pichu', 'Pidgeot', 'Pidgeotto', 'Pidgey', 'Pidove', 'Pignite', 'Pikachu', 'Piloswine', 'Pineco', 'Pinsir', 'Piplup', 'Plusle', 'Politoed', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Poochyena', 'Porygon', 'Porygon-Z', 'Porygon2', 'Primeape', 'Prinplup', 'Probopass', 'Psyduck', 'Pupitar', 'Purrloin', 'Purugly', 'Pyroar', 'Quagsire', 'Quilava', 'Quilladin', 'Qwilfish', 'Raichu', 'Raikou', 'Ralts', 'Rampardos', 'Rapidash', 'Raticate', 'Rattata', 'Rayquaza', 'Regice', 'Regigigas', 'Regirock', 'Registeel', 'Relicanth', 'Remoraid', 'Reshiram', 'Reuniclus', 'Rhydon', 'Rhyhorn', 'Rhyperior', 'Riolu', 'Roggenrola', 'Roselia', 'Roserade', 'Rotom', 'RotomFan Rotom', 'RotomFrost Rotom', 'RotomHeat Rotom', 'RotomMow Rotom', 'RotomWash Rotom', 'Rufflet', 'Sableye', 'Salamence', 'Samurott', 'Sandile', 'Sandshrew', 'Sandslash', 'Sawk', 'Sawsbuck', 'Scatterbug', 'Sceptile', 'Scizor', 'Scolipede', 'Scrafty', 'Scraggy', 'Scyther', 'Seadra', 'Seaking', 'Sealeo', 'Seedot', 'Seel', 'Seismitoad', 'Sentret', 'Serperior', 'Servine', 'Seviper', 'Sewaddle', 'Sharpedo', 'Shedinja', 'Shelgon', 'Shellder', 'Shellos', 'Shelmet', 'Shieldon', 'Shiftry', 'Shinx', 'Shroomish', 'Shuckle', 'Shuppet', 'Sigilyph', 'Silcoon', 'Simipour', 'Simisage', 'Simisear', 'Skarmory', 'Skiddo', 'Skiploom', 'Skitty', 'Skorupi', 'Skrelp', 'Skuntank', 'Slaking', 'Slakoth', 'Sliggoo', 'Slowbro', 'Slowking', 'Slowpoke', 'Slugma', 'Slurpuff', 'Smeargle', 'Smoochum', 'Sneasel', 'Snivy', 'Snorlax', 'Snorunt', 'Snover', 'Snubbull', 'Solosis', 'Solrock', 'Spearow', 'Spewpa', 'Spheal', 'Spinarak', 'Spinda', 'Spiritomb', 'Spoink', 'Spritzee', 'Squirtle', 'Stantler', 'Staraptor', 'Staravia', 'Starly', 'Starmie', 'Staryu', 'Steelix', 'Stoutland', 'Stunfisk', 'Stunky', 'Sudowoodo', 'Suicune', 'Sunflora', 'Sunkern', 'Surskit', 'Swablu', 'Swadloon', 'Swalot', 'Swampert', 'Swanna', 'Swellow', 'Swinub', 'Swirlix', 'Swoobat', 'Sylveon', 'Taillow', 'Talonflame', 'Tangela', 'Tangrowth', 'Tauros', 'Teddiursa', 'Tentacool', 'Tentacruel', 'Tepig', 'Terrakion', 'Throh', 'Timburr', 'Tirtouga', 'Togekiss', 'Togepi', 'Togetic', 'Torchic', 'Torkoal', 'Torterra', 'Totodile', 'Toxicroak', 'Tranquill', 'Trapinch', 'Treecko', 'Trevenant', 'Tropius', 'Trubbish', 'Turtwig', 'Tympole', 'Tynamo', 'Typhlosion', 'Tyranitar', 'Tyrantrum', 'Tyrogue', 'Tyrunt', 'Umbreon', 'Unfezant', 'Unown', 'Ursaring', 'Uxie', 'Vanillish', 'Vanillite', 'Vanilluxe', 'Vaporeon', 'Venipede', 'Venomoth', 'Venonat', 'Venusaur', 'Vespiquen', 'Vibrava', 'Victini', 'Victreebel', 'Vigoroth', 'Vileplume', 'Virizion', 'Vivillon', 'Volbeat', 'Volcanion', 'Volcarona', 'Voltorb', 'Vullaby', 'Vulpix', 'Wailmer', 'Wailord', 'Walrein', 'Wartortle', 'Watchog', 'Weavile', 'Weedle', 'Weepinbell', 'Weezing', 'Whimsicott', 'Whirlipede', 'Whiscash', 'Whismur', 'Wigglytuff', 'Wingull', 'Wobbuffet', 'Woobat', 'Wooper', 'WormadamPlant Cloak', 'WormadamSandy Cloak', 'WormadamTrash Cloak', 'Wurmple', 'Wynaut', 'Xatu', 'Xerneas', 'Yamask', 'Yanma', 'Yanmega', 'Yveltal', 'Zangoose', 'Zapdos', 'Zebstrika', 'Zekrom', 'Zigzagoon', 'Zoroark', 'Zorua', 'Zubat', 'Zweilous']

# Each Pokémon's corresponding Health Points is stored in a NumPy array called hps. You want to analyze the Health Points using the z-score to see how many standard deviations each Pokémon's HP is from the mean of all HPs.
hps = np.array([ 80.  60. 131.  62.  71. 109.  45.  53.  73.  60.  37.  63.  59.  84.
  25.  50.  98. 116.  29.  85.  43.  46.  46.  57.  94.  87.  70.  59.
  68.  65.  89.  52.  68.  66.  67.  75.  73. 103.  66. 109.  60.  56.
  71.  77.  75. 102.  98.  81.  60.  66. 105.  74.  34.  50.  53.  98.
  65. 127.  85.  71.  57.  93.  62.  47.  83.  69.  99.  66.   1.  89.
  20. 108. 115.  57.  38.  32.  91.  63.  53.  62. 122.  77.  87.  88.
  95.  96.  50.  63.  49.  50.  98.  55.  66.  50.  53.  89.  57.  56.
  81.  81.  89.  73.  23.  85.  81.  95.  46. 133.  36.  87.  69.  56.
  89.  61.   8.  38.  80. 126.  30.  68. 106.  84.  59.  32.  22.  49.
  59.  10.  24.  76.  58.  49.  58.  47.  92. 111. 122.  87.  88. 106.
 113. 106. 100.  52.  27.  91.  66.  67.  45.  35. 104.  80.  41.  78.
  76.  82. 126.  67.  35.  69.  52.  82.  74.  77.  54.  79.  55.  82.
  60.  39.  81.  50. 106.  80.  80.  71.  67.   7. 100.  47.  93.  52.
  65.  62.  41.  64.  81.  58.  36.  53.  75.  98.  90.  76.  43.  92.
  69.  62.  92.  84.  81.  38.  52.  24.  73.  69.  92.  74.  59. 123.
  42.  34.  52.  82.  59.  57.  39. 106.  52.  40.  65.  47.  62. 103.
  57.  67.  59.  63.  89.  82.  59.  44.  65.  90.  68.  65.  22.  94.
  30.  35.  59.  69.  69.  48.  60.  53.  21.  62.  50.  79.  64.  93.
  86.  91.  99.  86.  64. 103.  44.  67.  90.  61.  87.  47.  54.  82.
  87.  99.  66.  76.  84.  80.  35.  54. 105.  36.  84.  57.  94.  48.
  69.  16.  67.  96.  29.  99.  50.  67.   1.  96.  46.  54.  35.  43.
  98.  55.  91.  64.  77.  55.  79. 135.  85.  81.  56.  94. 103.  24.
  33. 123.  79.  72.  83.  97.  89.  62. 122.  69.  46.  54.  65.  58.
  63.  76.   1.  48.  93.  83.  51.  52.  98.  62.  55. 116.  59.  86.
  67.  70.  44.  47. 101.  39.  75.  37.  62.  67.  26.  98.  63. 100.
  44.  92. 129.  74.  52.  81.  72.  63.  65.  53.  79.  58.  46.  89.
  64. 137.  62.  50.  54.  78.  50.  36. 111.  36. 107.  72.  41. 111.
  63.  42.  70. 101.  86.  90. 114.  74.  78.  62.  31.  64. 110.  24.
 103.  75.  45.  70. 114.  53.  89.  97.  45.  85.  82.  56.  86.  59.
  53.  36.  78.  57.  54.  39.  33.  48.  87.  47. 106.  79.  72.  37.
 119.  31.  82. 112.  63.  51.  68.  92. 103.  84.  41.  51.  73.  35.
  62. 126.  41.  98.  44.  59.  66.  29.  66. 102.  87.  86.  47.  64.
  73.  86. 103.  42. 112.  61.  62.  37.  66.  62.  36.  61.  71.  58.
  88.  42.  91.  63.  78.  21.  72.  67.  92.  38. 103.  40. 102.  83.
  49. 124.  37.  64.  74.  82.  74.  89.  80.  69.  44.  59.  92.  38.
  71.  15.  50.  26. 100.  21.  62.  87.  84.  88.  96.  80.  90.  67.
  68.  23.  73. 101.  49.  38.  71.  98.  99.  29.  80.  51.  75.  10.
  92.  58.  74.  64.  42.  82.  56.  50.  85.  66.  50.  92.  53.  67.
  87.  93.  99. 111.  69.  48. 111. 104.  60.  86.  58.  28.  95.  77.
  71. 112. 105.  52.  40.  19.  68.  58.  78.  69.  51.  58.  28. 100.
  54.  84.  51.  70.  84.  61.  47. 128.  63.  83.  66.  48. 102.  78.
  77.   9.  76.  90.  76.  64.  99.  75.  83.  95.  94.  34.  77.  49.
  16.  76.  23.  56.   3.  42.  56.  68.  54.  44.  45. 108.  56.  66.
 117.  23.  15.  42.  58.  39.  67.  66.  28.  72.  31.  86.  74. 125.
  89.  63.  77.  72.  49.  31.  96. 107.  56.  61.  56.  94.  99.  46.
  59.  54.  74.  88.  96.  61.  43.  82.  83.  59.  72.  77.  91.  70.
  81.  73.  43.  86.  71.  95.  38.  50.  77.  24.  65.  57.  57.  62.
  11.  69.  70.  95. 106.  77.  92.   6.  82.  97.  91.  74.  59.  59.
  69.  79.  83.  66.  36. 115.  46.   1. 105.  94.  73.  93.  80.  47.
  71.  36.  51.  46.  72.  96.  52.  80.  13.  41.  82.  93.  93.  96.
  26.  55.   2.  64.  74.  59.  44.  79.  82.  72.  53.  69.  70.  75.
  84.  68.  31.  61.  78.  57.])

# https://en.wikipedia.org/wiki/Standard_score

# The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based on their z-scores:

poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
high_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        high_hp_pokemon.append((name, hp, zscore))

# Use NumPy to eliminate the for loop used to create the z-scores.
# Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2.
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# <script.py> output:
#     ('Abomasnow', 80.0, 0.46797638117739043)
#     ('Abra', 60.0, -0.3271693284337512)
#     ('Absol', 131.0, 2.4955979406858013)

# Use list comprehension to replace the for loop used to collect Pokémon with the highest HPs based on their z-score.
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# <script.py> output:
#     ('Abomasnow', 80.0, 0.46797638117739043)
#     ('Abra', 60.0, -0.3271693284337512)
#     ('Absol', 131.0, 2.4955979406858013)




# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon = [(name, hp, zscore) for name, hp, zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon, sep='\n')

# <script.py> output:
#     ('Absol', 131.0, 2.4955979406858013)
#     ('Bonsly', 127.0, 2.3365687987635733)
#     ('Caterpie', 122.0, 2.137782371360788)
#     ('Cofagrigus', 133.0, 2.575112511646916)
#     ('Cresselia', 126.0, 2.296811513283016)
#     ('Dewgong', 122.0, 2.137782371360788)
#     ('Druddigon', 126.0, 2.296811513283016)
#     ('Froakie', 123.0, 2.1775396568413448)
#     ('Kadabra', 135.0, 2.65462708260803)
#     ('Klang', 123.0, 2.1775396568413448)
#     ('Kricketune', 122.0, 2.137782371360788)
#     ('Lumineon', 129.0, 2.4160833697246873)
#     ('Magnemite', 137.0, 2.734141653569144)
#     ('Nidorina', 119.0, 2.0185105149191167)
#     ('Onix', 126.0, 2.296811513283016)
#     ('Prinplup', 124.0, 2.217296942321902)
#     ('Skuntank', 128.0, 2.3763260842441305)
#     ('Swellow', 125.0, 2.2570542278024592)


# Use %%timeit (cell magic mode) within your IPython console to compare the runtimes between the original code blocks and the new code you developed using NumPy and list comprehension.
# Don't include the print() statements when timing. You should include ten lines of code when timing the original code blocks and five lines of code when timing the new code you developed. You may need to press SHIFT+ENTER after entering %%timeit to get to a new line within your IPython console.

# %%timeit
poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
high_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        high_hp_pokemon.append((name, hp, zscore))


# %%timeit
# 79.8 ms +- 18.8 ms per loop (mean +- std. dev. of 7 runs, 10 loops each)

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]

highest_hp_pokemon = [(name, hp, zscore) for name, hp, zscore in poke_zscores2 if zscore > 2]

# 510 us +- 138 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

# Which approach was the faster?

# The total time for executing both of the original code blocks was faster.
# Both approaches had the same execution time.

#YES - The total time for executing the updated solution using NumPy and list comprehension was faster.

# Great job! You're Catching 'Em All (efficiencies that is). You eliminated two loops using NumPy broadcasting and list comprehension. Did you notice how much faster the approach you developed was compared to the original loops? What a great improvement!
# Remember the techniques you've learned throughout this chapter as you continue writing Python code outside this course. Keep in mind the built-in functions and modules you covered to eliminate loops and remember to check your unavoidable loops for things that can be moved outside.
