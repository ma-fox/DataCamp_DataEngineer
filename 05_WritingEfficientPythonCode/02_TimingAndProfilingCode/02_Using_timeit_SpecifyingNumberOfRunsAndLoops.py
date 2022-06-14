# Using %timeit: specifying number of runs and loops

# %timeit lets you specify the number of runs and number of loops you want to consider with the -r and -n flags.
# You can use -r5 and -n25 to specify 5 iterations each with 25 loops when calculating the average and standard deviation of runtime for your code.

# A list of 480 superheroes provided by Marvel.com

heroes = [
    'A-Bomb', 'Abe Sapien', 'Abin Sur', 'Abomination', 'Absorbing Man',
    'Adam Strange', 'Agent 13', 'Agent Bob', 'Agent Zero', 'Air-Walker',
    'Ajax', 'Alan Scott', 'Alfred Pennyworth', 'Alien', 'Amazo', 'Ammo',
    'Angel', 'Angel Dust', 'Angel Salvadore', 'Animal Man', 'Annihilus',
    'Ant-Man', 'Ant-Man II', 'Anti-Venom', 'Apocalypse', 'Aqualad', 'Aquaman',
    'Arachne', 'Archangel', 'Arclight', 'Ardina', 'Ares', 'Ariel', 'Armor',
    'Atlas', 'Atom', 'Atom Girl', 'Atom II', 'Aurora', 'Azazel', 'Bane',
    'Banshee', 'Bantam', 'Batgirl', 'Batgirl IV', 'Batgirl VI', 'Batman',
    'Batman II', 'Battlestar', 'Beak', 'Beast', 'Beast Boy', 'Beta Ray Bill',
    'Big Barda', 'Big Man', 'Binary', 'Bishop', 'Bizarro', 'Black Adam',
    'Black Bolt', 'Black Canary', 'Black Cat', 'Black Knight III',
    'Black Lightning', 'Black Mamba', 'Black Manta', 'Black Panther',
    'Black Widow', 'Black Widow II', 'Blackout', 'Blackwing', 'Blackwulf',
    'Blade', 'Bling!', 'Blink', 'Blizzard II', 'Blob', 'Bloodaxe',
    'Blue Beetle II', 'Boom-Boom', 'Booster Gold', 'Box III', 'Brainiac',
    'Brainiac 5', 'Brother Voodoo', 'Buffy', 'Bullseye', 'Bumblebee', 'Cable',
    'Callisto', 'Cannonball', 'Captain America', 'Captain Atom',
    'Captain Britain', 'Captain Mar-vell', 'Captain Marvel',
    'Captain Marvel II', 'Carnage', 'Cat', 'Catwoman', 'Cecilia Reyes',
    'Century', 'Chamber', 'Changeling', 'Cheetah', 'Cheetah II', 'Cheetah III',
    'Chromos', 'Citizen Steel', 'Cloak', 'Clock King', 'Colossus', 'Copycat',
    'Corsair', 'Cottonmouth', 'Crimson Dynamo', 'Crystal', 'Cyborg', 'Cyclops',
    'Cypher', 'Dagger', 'Daredevil', 'Darkhawk', 'Darkseid', 'Darkstar',
    'Darth Vader', 'Dash', 'Dazzler', 'Deadman', 'Deadpool', 'Deadshot',
    'Deathlok', 'Deathstroke', 'Demogoblin', 'Destroyer', 'Diamondback',
    'Doc Samson', 'Doctor Doom', 'Doctor Doom II', 'Doctor Fate',
    'Doctor Octopus', 'Doctor Strange', 'Domino', 'Donna Troy', 'Doomsday',
    'Doppelganger', 'Drax the Destroyer', 'Elastigirl', 'Electro', 'Elektra',
    'Elongated Man', 'Emma Frost', 'Enchantress', 'Etrigan', 'Evil Deadpool',
    'Evilhawk', 'Exodus', 'Fabian Cortez', 'Falcon', 'Feral', 'Fin Fang Foom',
    'Firebird', 'Firelord', 'Firestar', 'Firestorm', 'Flash', 'Flash II',
    'Flash III', 'Flash IV', 'Forge', 'Franklin Richards', 'Franklin Storm',
    'Frenzy', 'Frigga', 'Galactus', 'Gambit', 'Gamora', 'Genesis',
    'Ghost Rider', 'Giganta', 'Gladiator', 'Goblin Queen', 'Goku',
    'Goliath IV', 'Gorilla Grodd', 'Granny Goodness', 'Gravity', 'Green Arrow',
    'Green Goblin', 'Green Goblin II', 'Green Goblin III', 'Green Goblin IV',
    'Groot', 'Guy Gardner', 'Hal Jordan', 'Han Solo', 'Harley Quinn', 'Havok',
    'Hawk', 'Hawkeye', 'Hawkeye II', 'Hawkgirl', 'Hawkman', 'Hawkwoman',
    'Hawkwoman III', 'Heat Wave', 'Hela', 'Hellboy', 'Hellcat', 'Hellstorm',
    'Hercules', 'Hobgoblin', 'Hope Summers', 'Howard the Duck', 'Hulk',
    'Human Torch', 'Huntress', 'Husk', 'Hybrid', 'Hydro-Man', 'Hyperion',
    'Iceman', 'Impulse', 'Ink', 'Invisible Woman', 'Iron Fist', 'Iron Man',
    'Jack of Hearts', 'Jack-Jack', 'James T. Kirk', 'Jean Grey',
    'Jennifer Kale', 'Jessica Jones', 'Jigsaw', 'John Stewart', 'John Wraith',
    'Joker', 'Jolt', 'Jubilee', 'Juggernaut', 'Justice', 'Kang', 'Karate Kid',
    'Killer Croc', 'Kilowog', 'Kingpin', 'Klaw', 'Kraven II',
    'Kraven the Hunter', 'Krypto', 'Kyle Rayner', 'Lady Deathstrike', 'Leader',
    'Legion', 'Lex Luthor', 'Light Lass', 'Lightning Lad', 'Lightning Lord',
    'Living Brain', 'Lizard', 'Lobo', 'Loki', 'Longshot', 'Luke Cage',
    'Luke Skywalker', 'Mach-IV', 'Machine Man', 'Magneto', 'Man-Thing',
    'Man-Wolf', 'Mandarin', 'Mantis', 'Martian Manhunter', 'Marvel Girl',
    'Master Brood', 'Maverick', 'Maxima', 'Medusa', 'Meltdown', 'Mephisto',
    'Mera', 'Metallo', 'Metamorpho', 'Metron', 'Micro Lad', 'Mimic',
    'Miss Martian', 'Mister Fantastic', 'Mister Freeze', 'Mister Sinister',
    'Mockingbird', 'MODOK', 'Molten Man', 'Monarch', 'Moon Knight',
    'Moonstone', 'Morlun', 'Morph', 'Moses Magnum', 'Mr Immortal',
    'Mr Incredible', 'Ms Marvel II', 'Multiple Man', 'Mysterio', 'Mystique',
    'Namor', 'Namora', 'Namorita', 'Naruto Uzumaki', 'Nebula', 'Nick Fury',
    'Nightcrawler', 'Nightwing', 'Northstar', 'Nova', 'Odin', 'Omega Red',
    'Omniscient', 'One Punch Man', 'Onslaught', 'Oracle', 'Paul Blart',
    'Penance II', 'Penguin', 'Phantom Girl', 'Phoenix', 'Plantman',
    'Plastic Man', 'Plastique', 'Poison Ivy', 'Polaris', 'Power Girl',
    'Predator', 'Professor X', 'Professor Zoom', 'Psylocke', 'Punisher',
    'Purple Man', 'Pyro', 'Question', 'Quicksilver', 'Quill', "Ra's Al Ghul",
    'Raven', 'Ray', 'Razor-Fist II', 'Red Arrow', 'Red Hood', 'Red Hulk',
    'Red Robin', 'Red Skull', 'Red Tornado', 'Rhino', 'Rick Flag', 'Ripcord',
    'Robin', 'Robin II', 'Robin III', 'Robin V', 'Rocket Raccoon', 'Rogue',
    'Ronin', 'Rorschach', 'Sabretooth', 'Sage', 'Sandman', 'Sasquatch',
    'Scarecrow', 'Scarlet Spider', 'Scarlet Spider II', 'Scarlet Witch',
    'Scorpion', 'Sentry', 'Shadow King', 'Shadow Lass', 'Shadowcat',
    'Shang-Chi', 'Shatterstar', 'She-Hulk', 'She-Thing', 'Shocker', 'Shriek',
    'Sif', 'Silver Surfer', 'Silverclaw', 'Sinestro', 'Siren', 'Siryn',
    'Skaar', 'Snowbird', 'Solomon Grundy', 'Songbird', 'Space Ghost', 'Spawn',
    'Spider-Girl', 'Spider-Gwen', 'Spider-Man', 'Spider-Woman',
    'Spider-Woman III', 'Spider-Woman IV', 'Spock', 'Spyke', 'Star-Lord',
    'Starfire', 'Stargirl', 'Static', 'Steel', 'Steppenwolf', 'Storm',
    'Sunspot', 'Superboy', 'Superboy-Prime', 'Supergirl', 'Superman', 'Swarm',
    'Synch', 'T-1000', 'Taskmaster', 'Tempest', 'Thanos', 'The Comedian',
    'Thing', 'Thor', 'Thor Girl', 'Thunderbird', 'Thunderbird III',
    'Thunderstrike', 'Thundra', 'Tiger Shark', 'Tigra', 'Tinkerer', 'Toad',
    'Toxin', 'Trickster', 'Triplicate Girl', 'Triton', 'Two-Face', 'Ultragirl',
    'Ultron', 'Utgard-Loki', 'Vagabond', 'Valerie Hart', 'Valkyrie',
    'Vanisher', 'Vegeta', 'Venom', 'Venom II', 'Venom III', 'Vertigo II',
    'Vibe', 'Vindicator', 'Violet Parr', 'Vision', 'Vision II', 'Vixen',
    'Vulture', 'Walrus', 'War Machine', 'Warbird', 'Warlock', 'Warp',
    'Warpath', 'Wasp', 'White Queen', 'Winter Soldier', 'Wiz Kid', 'Wolfsbane',
    'Wolverine', 'Wonder Girl', 'Wonder Man', 'Wonder Woman', 'Wyatt Wingfoot',
    'X-23', 'X-Man', 'Yellow Claw', 'Yellowjacket', 'Yellowjacket II', 'Yoda',
    'Zatanna', 'Zoom'
]

# Instead of relying on the default settings for %timeit, you'd like to only use 5 runs and 25 loops per each run.
# -r is the number of runs.
# -n is the number of loops.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# In contrast, Python dictionaries are unordered, changeable and indexed.
%timeit -r5 -n25 set(heroes)


# Note:
# %timeit is a Python built-in function that runs a given statement multiple times and reports the time it takes to do so.
# But it is not a standard library function and works only in the IPython shell, or Jupyter Notebook.
