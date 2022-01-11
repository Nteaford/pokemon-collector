from django.db import models
from django.urls import reverse

# Create your models here.
class Pokemon(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    pokedex_number = models.IntegerField()
    classification = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)
    generation = models.IntegerField()

    def __str__(self):
        return f"({self.pokedex_number}) - {self.name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

# pokemons = [
#     Pokemon('Bulbasaur','1','Seed Pokémon','grass','poison','1'),
#     Pokemon('Ivysaur','2','Seed Pokémon','grass','poison','1'),
#     Pokemon('Venusaur','3','Seed Pokémon','grass','poison','1'),
#     Pokemon('Charmander','4','Lizard Pokémon','fire','n/a','1'),
#     Pokemon('Charmeleon','5','Flame Pokémon','fire','n/a','1'),
#     Pokemon('Charizard','6','Flame Pokémon','fire','flying','1'),
#     Pokemon('Squirtle','7','Tiny Turtle Pokémon','water','n/a','1'),
#     Pokemon('Wartortle','8','Turtle Pokémon','water','n/a','1'),
#     Pokemon('Blastoise','9','Shellfish Pokémon','water','n/a','1'),
#     Pokemon('Caterpie','10','Worm Pokémon','bug','n/a','1'),
#     Pokemon('Metapod','11','Cocoon Pokémon','bug','n/a','1'),
#     Pokemon('Butterfree','12','Butterfly Pokémon','bug','flying','1'),
#     Pokemon('Weedle','13','Hairy Pokémon','bug','poison','1'),
#     Pokemon('Kakuna','14','Cocoon Pokémon','bug','poison','1'),
#     Pokemon('Beedrill','15','Poison Bee Pokémon','bug','poison','1'),
#     Pokemon('Pidgey','16','Tiny Bird Pokémon','normal','flying','1'),
#     Pokemon('Pidgeotto','17','Bird Pokémon','normal','flying','1'),
#     Pokemon('Pidgeot','18','Bird Pokémon','normal','flying','1'),
#     Pokemon('Rattata','19','Mouse Pokémon','normal','dark','1'),
#     Pokemon('Raticate','20','Mouse Pokémon','normal','dark','1'),
#     Pokemon('Spearow','21','Tiny Bird Pokémon','normal','flying','1'),
#     Pokemon('Fearow','22','Beak Pokémon','normal','flying','1'),
#     Pokemon('Ekans','23','Snake Pokémon','poison','n/a','1'),
#     Pokemon('Arbok','24','Cobra Pokémon','poison','n/a','1'),
#     Pokemon('Pikachu','25','Mouse Pokémon','electric','n/a','1'),
#     Pokemon('Raichu','26','Mouse Pokémon','electric','electric','1'),
#     Pokemon('Sandshrew','27','Mouse Pokémon','ground','ice','1'),
#     Pokemon('Sandslash','28','Mouse Pokémon','ground','ice','1'),
#     Pokemon('Nidoran♀','29','Poison Pin Pokémon','poison','n/a','1'),
#     Pokemon('Nidorina','30','Poison Pin Pokémon','poison','n/a','1'),
#     Pokemon('Nidoqueen','31','Drill Pokémon','poison','ground','1'),
#     Pokemon('Nidoran♂','32','Poison Pin Pokémon','poison','n/a','1'),
#     Pokemon('Nidorino','33','Poison Pin Pokémon','poison','n/a','1'),
#     Pokemon('Nidoking','34','Drill Pokémon','poison','ground','1'),
#     Pokemon('Clefairy','35','Fairy Pokémon','fairy','n/a','1'),
#     Pokemon('Clefable','36','Fairy Pokémon','fairy','n/a','1'),
#     Pokemon('Vulpix','37','Fox Pokémon','fire','ice','1'),
#     Pokemon('Ninetales','38','Fox Pokémon','fire','ice','1'),
#     Pokemon('Jigglypuff','39','Balloon Pokémon','normal','fairy','1'),
#     Pokemon('Wigglytuff','40','Balloon Pokémon','normal','fairy','1'),
#     Pokemon('Zubat','41','Bat Pokémon','poison','flying','1'),
#     Pokemon('Golbat','42','Bat Pokémon','poison','flying','1'),
#     Pokemon('Oddish','43','Weed Pokémon','grass','poison','1'),
#     Pokemon('Gloom','44','Weed Pokémon','grass','poison','1'),
#     Pokemon('Vileplume','45','Flower Pokémon','grass','poison','1'),
#     Pokemon('Paras','46','Mushroom Pokémon','bug','grass','1'),
#     Pokemon('Parasect','47','Mushroom Pokémon','bug','grass','1'),
#     Pokemon('Venonat','48','Insect Pokémon','bug','poison','1'),
#     Pokemon('Venomoth','49','Poison Moth Pokémon','bug','poison','1'),
#     Pokemon('Diglett','50','Mole Pokémon','ground','ground','1'),
#     Pokemon('Dugtrio','51','Mole Pokémon','ground','ground','1'),
#     Pokemon('Meowth','52','Scratch Cat Pokémon','normal','dark','1'),
#     Pokemon('Persian','53','Classy Cat Pokémon','normal','dark','1'),
#     Pokemon('Psyduck','54','Duck Pokémon','water','n/a','1'),
#     Pokemon('Golduck','55','Duck Pokémon','water','n/a','1'),
#     Pokemon('Mankey','56','Pig Monkey Pokémon','fighting','n/a','1'),
#     Pokemon('Primeape','57','Pig Monkey Pokémon','fighting','n/a','1'),
#     Pokemon('Growlithe','58','Puppy Pokémon','fire','n/a','1'),
#     Pokemon('Arcanine','59','Legendary Pokémon','fire','n/a','1'),
#     Pokemon('Poliwag','60','Tadpole Pokémon','water','n/a','1'),
#     Pokemon('Poliwhirl','61','Tadpole Pokémon','water','n/a','1'),
#     Pokemon('Poliwrath','62','Tadpole Pokémon','water','fighting','1'),
#     Pokemon('Abra','63','Psi Pokémon','psychic','n/a','1'),
#     Pokemon('Kadabra','64','Psi Pokémon','psychic','n/a','1'),
#     Pokemon('Alakazam','65','Psi Pokémon','psychic','n/a','1'),
#     Pokemon('Machop','66','Superpower Pokémon','fighting','n/a','1'),
#     Pokemon('Machoke','67','Superpower Pokémon','fighting','n/a','1'),
#     Pokemon('Machamp','68','Superpower Pokémon','fighting','n/a','1'),
#     Pokemon('Bellsprout','69','Flower Pokémon','grass','poison','1'),
#     Pokemon('Weepinbell','70','Flycatcher Pokémon','grass','poison','1'),
#     Pokemon('Victreebel','71','Flycatcher Pokémon','grass','poison','1'),
#     Pokemon('Tentacool','72','Jellyfish Pokémon','water','poison','1'),
#     Pokemon('Tentacruel','73','Jellyfish Pokémon','water','poison','1'),
#     Pokemon('Geodude','74','Rock Pokémon','rock','ground','1'),
#     Pokemon('Graveler','75','Rock Pokémon','rock','ground','1'),
#     Pokemon('Golem','76','Megaton Pokémon','rock','ground','1'),
#     Pokemon('Ponyta','77','Fire Horse Pokémon','fire','n/a','1'),
#     Pokemon('Rapidash','78','Fire Horse Pokémon','fire','n/a','1'),
#     Pokemon('Slowpoke','79','Dopey Pokémon','water','psychic','1'),
#     Pokemon('Slowbro','80','Hermit Crab Pokémon','water','psychic','1'),
#     Pokemon('Magnemite','81','Magnet Pokémon','electric','steel','1'),
#     Pokemon('Magneton','82','Magnet Pokémon','electric','steel','1'),
#     Pokemon('Farfetch-d','83','Wild Duck Pokémon','normal','flying','1'),
#     Pokemon('Doduo','84','Twin Bird Pokémon','normal','flying','1'),
#     Pokemon('Dodrio','85','Triple Bird Pokémon','normal','flying','1'),
#     Pokemon('Seel','86','Sea Lion Pokémon','water','n/a','1'),
#     Pokemon('Dewgong','87','Sea Lion Pokémon','water','ice','1'),
#     Pokemon('Grimer','88','Sludge Pokémon','poison','poison','1'),
#     Pokemon('Muk','89','Sludge Pokémon','poison','poison','1'),
#     Pokemon('Shellder','90','Bivalve Pokémon','water','n/a','1'),
#     Pokemon('Cloyster','91','Bivalve Pokémon','water','ice','1'),
#     Pokemon('Gastly','92','Gas Pokémon','ghost','poison','1'),
#     Pokemon('Haunter','93','Gas Pokémon','ghost','poison','1'),
#     Pokemon('Gengar','94','Shadow Pokémon','ghost','poison','1'),
#     Pokemon('Onix','95','Rock Snake Pokémon','rock','ground','1'),
#     Pokemon('Drowzee','96','Hypnosis Pokémon','psychic','n/a','1'),
#     Pokemon('Hypno','97','Hypnosis Pokémon','psychic','n/a','1'),
#     Pokemon('Krabby','98','River Crab Pokémon','water','n/a','1'),
#     Pokemon('Kingler','99','Pincer Pokémon','water','n/a','1'),
#     Pokemon('Voltorb','100','Ball Pokémon','electric','n/a','1'),
#     Pokemon('Electrode','101','Ball Pokémon','electric','n/a','1'),
#     Pokemon('Exeggcute','102','Egg Pokémon','grass','psychic','1'),
#     Pokemon('Exeggutor','103','Coconut Pokémon','grass','psychic','1'),
#     Pokemon('Cubone','104','Lonely Pokémon','ground','n/a','1'),
#     Pokemon('Marowak','105','Bone Keeper Pokémon','ground','fire','1'),
#     Pokemon('Hitmonlee','106','Kicking Pokémon','fighting','n/a','1'),
#     Pokemon('Hitmonchan','107','Punching Pokémon','fighting','n/a','1'),
#     Pokemon('Lickitung','108','Licking Pokémon','normal','n/a','1'),
#     Pokemon('Koffing','109','Poison Gas Pokémon','poison','n/a','1'),
#     Pokemon('Weezing','110','Poison Gas Pokémon','poison','n/a','1'),
#     Pokemon('Rhyhorn','111','Spikes Pokémon','ground','rock','1'),
#     Pokemon('Rhydon','112','Drill Pokémon','ground','rock','1'),
#     Pokemon('Chansey','113','Egg Pokémon','normal','n/a','1'),
#     Pokemon('Tangela','114','Vine Pokémon','grass','n/a','1'),
#     Pokemon('Kangaskhan','115','Parent Pokémon','normal','n/a','1'),
#     Pokemon('Horsea','116','Dragon Pokémon','water','n/a','1'),
#     Pokemon('Seadra','117','Dragon Pokémon','water','n/a','1'),
#     Pokemon('Goldeen','118','Goldfish Pokémon','water','n/a','1'),
#     Pokemon('Seaking','119','Goldfish Pokémon','water','n/a','1'),
#     Pokemon('Staryu','120','Starshape Pokémon','water','n/a','1'),
#     Pokemon('Starmie','121','Mysterious Pokémon','water','psychic','1'),
#     Pokemon('Mr. Mime','122','Barrier Pokémon','psychic','fairy','1'),
#     Pokemon('Scyther','123','Mantis Pokémon','bug','flying','1'),
#     Pokemon('Jynx','124','Humanshape Pokémon','ice','psychic','1'),
#     Pokemon('Electabuzz','125','Electric Pokémon','electric','n/a','1'),
#     Pokemon('Magmar','126','Spitfire Pokémon','fire','n/a','1'),
#     Pokemon('Pinsir','127','Stagbeetle Pokémon','bug','n/a','1'),
#     Pokemon('Tauros','128','Wild Bull Pokémon','normal','n/a','1'),
#     Pokemon('Magikarp','129','Fish Pokémon','water','n/a','1'),
#     Pokemon('Gyarados','130','Atrocious Pokémon','water','flying','1'),
#     Pokemon('Lapras','131','Transport Pokémon','water','ice','1'),
#     Pokemon('Ditto','132','Transform Pokémon','normal','n/a','1'),
#     Pokemon('Eevee','133','Evolution Pokémon','normal','n/a','1'),
#     Pokemon('Vaporeon','134','Bubble Jet Pokémon','water','n/a','1'),
#     Pokemon('Jolteon','135','Lightning Pokémon','electric','n/a','1'),
#     Pokemon('Flareon','136','Flame Pokémon','fire','n/a','1'),
#     Pokemon('Porygon','137','Virtual Pokémon','normal','n/a','1'),
#     Pokemon('Omanyte','138','Spiral Pokémon','rock','water','1'),
#     Pokemon('Omastar','139','Spiral Pokémon','rock','water','1'),
#     Pokemon('Kabuto','140','Shellfish Pokémon','rock','water','1'),
#     Pokemon('Kabutops','141','Shellfish Pokémon','rock','water','1'),
#     Pokemon('Aerodactyl','142','Fossil Pokémon','rock','flying','1'),
#     Pokemon('Snorlax','143','Sleeping Pokémon','normal','n/a','1'),
#     Pokemon('Articuno','144','Freeze Pokémon','ice','flying','1'),
#     Pokemon('Zapdos','145','Electric Pokémon','electric','flying','1'),
#     Pokemon('Moltres','146','Flame Pokémon','fire','flying','1'),
#     Pokemon('Dratini','147','Dragon Pokémon','dragon','n/a','1'),
#     Pokemon('Dragonair','148','Dragon Pokémon','dragon','n/a','1'),
#     Pokemon('Dragonite','149','Dragon Pokémon','dragon','flying','1'),
#     Pokemon('Mewtwo','150','Genetic Pokémon','psychic','n/a','1'),
#     Pokemon('Mew','151','New Species Pokémon','psychic','n/a','1'),
#     Pokemon('Chikorita','152','Leaf Pokémon','grass','n/a','2'),
#     Pokemon('Bayleef','153','Leaf Pokémon','grass','n/a','2'),
#     Pokemon('Meganium','154','Herb Pokémon','grass','n/a','2'),
#     Pokemon('Cyndaquil','155','Fire Mouse Pokémon','fire','n/a','2'),
#     Pokemon('Quilava','156','Volcano Pokémon','fire','n/a','2'),
#     Pokemon('Typhlosion','157','Volcano Pokémon','fire','n/a','2'),
#     Pokemon('Totodile','158','Big Jaw Pokémon','water','n/a','2'),
#     Pokemon('Croconaw','159','Big Jaw Pokémon','water','n/a','2'),
#     Pokemon('Feraligatr','160','Big Jaw Pokémon','water','n/a','2'),
#     Pokemon('Sentret','161','Scout Pokémon','normal','n/a','2'),
#     Pokemon('Furret','162','Long Body Pokémon','normal','n/a','2'),
#     Pokemon('Hoothoot','163','Owl Pokémon','normal','flying','2'),
#     Pokemon('Noctowl','164','Owl Pokémon','normal','flying','2'),
#     Pokemon('Ledyba','165','Five Star Pokémon','bug','flying','2'),
#     Pokemon('Ledian','166','Five Star Pokémon','bug','flying','2'),
#     Pokemon('Spinarak','167','String Spit Pokémon','bug','poison','2'),
#     Pokemon('Ariados','168','Long Leg Pokémon','bug','poison','2'),
#     Pokemon('Crobat','169','Bat Pokémon','poison','flying','2'),
#     Pokemon('Chinchou','170','Angler Pokémon','water','electric','2'),
#     Pokemon('Lanturn','171','Light Pokémon','water','electric','2'),
#     Pokemon('Pichu','172','Tiny Mouse Pokémon','electric','n/a','2'),
#     Pokemon('Cleffa','173','Star Shape Pokémon','fairy','n/a','2'),
#     Pokemon('Igglybuff','174','Balloon Pokémon','normal','fairy','2'),
#     Pokemon('Togepi','175','Spike Ball Pokémon','fairy','n/a','2'),
#     Pokemon('Togetic','176','Happiness Pokémon','fairy','flying','2'),
#     Pokemon('Natu','177','Little Bird Pokémon','psychic','flying','2'),
#     Pokemon('Xatu','178','Mystic Pokémon','psychic','flying','2'),
#     Pokemon('Mareep','179','Wool Pokémon','electric','n/a','2'),
#     Pokemon('Flaaffy','180','Wool Pokémon','electric','n/a','2'),
#     Pokemon('Ampharos','181','Light Pokémon','electric','n/a','2'),
#     Pokemon('Bellossom','182','Flower Pokémon','grass','n/a','2'),
#     Pokemon('Marill','183','Aquamouse Pokémon','water','fairy','2'),
#     Pokemon('Azumarill','184','Aquarabbit Pokémon','water','fairy','2'),
#     Pokemon('Sudowoodo','185','Imitation Pokémon','rock','n/a','2'),
#     Pokemon('Politoed','186','Frog Pokémon','water','n/a','2'),
#     Pokemon('Hoppip','187','Cottonweed Pokémon','grass','flying','2'),
#     Pokemon('Skiploom','188','Cottonweed Pokémon','grass','flying','2'),
#     Pokemon('Jumpluff','189','Cottonweed Pokémon','grass','flying','2'),
#     Pokemon('Aipom','190','Long Tail Pokémon','normal','n/a','2'),
#     Pokemon('Sunkern','191','Seed Pokémon','grass','n/a','2'),
#     Pokemon('Sunflora','192','Sun Pokémon','grass','n/a','2'),
#     Pokemon('Yanma','193','Clear Wing Pokémon','bug','flying','2'),
#     Pokemon('Wooper','194','Water Fish Pokémon','water','ground','2'),
#     Pokemon('Quagsire','195','Water Fish Pokémon','water','ground','2'),
#     Pokemon('Espeon','196','Sun Pokémon','psychic','n/a','2'),
#     Pokemon('Umbreon','197','Moonlight Pokémon','dark','n/a','2'),
#     Pokemon('Murkrow','198','Darkness Pokémon','dark','flying','2'),
#     Pokemon('Slowking','199','Royal Pokémon','water','psychic','2'),
#     Pokemon('Misdreavus','200','Screech Pokémon','ghost','n/a','2'),
#     Pokemon('Unown','201','Symbol Pokémon','psychic','n/a','2'),
#     Pokemon('Wobbuffet','202','Patient Pokémon','psychic','n/a','2'),
#     Pokemon('Girafarig','203','Long Neck Pokémon','normal','psychic','2'),
#     Pokemon('Pineco','204','Bagworm Pokémon','bug','n/a','2'),
#     Pokemon('Forretress','205','Bagworm Pokémon','bug','steel','2'),
#     Pokemon('Dunsparce','206','Land Snake Pokémon','normal','n/a','2'),
#     Pokemon('Gligar','207','Flyscorpion Pokémon','ground','flying','2'),
#     Pokemon('Steelix','208','Iron Snake Pokémon','steel','ground','2'),
#     Pokemon('Snubbull','209','Fairy Pokémon','fairy','n/a','2'),
#     Pokemon('Granbull','210','Fairy Pokémon','fairy','n/a','2'),
#     Pokemon('Qwilfish','211','Balloon Pokémon','water','poison','2'),
#     Pokemon('Scizor','212','Pincer Pokémon','bug','steel','2'),
#     Pokemon('Shuckle','213','Mold Pokémon','bug','rock','2'),
#     Pokemon('Heracross','214','Singlehorn Pokémon','bug','fighting','2'),
#     Pokemon('Sneasel','215','Sharp Claw Pokémon','dark','ice','2'),
#     Pokemon('Teddiursa','216','Little Bear Pokémon','normal','n/a','2'),
#     Pokemon('Ursaring','217','Hibernator Pokémon','normal','n/a','2'),
#     Pokemon('Slugma','218','Lava Pokémon','fire','n/a','2'),
#     Pokemon('Magcargo','219','Lava Pokémon','fire','rock','2'),
#     Pokemon('Swinub','220','Pig Pokémon','ice','ground','2'),
#     Pokemon('Piloswine','221','Swine Pokémon','ice','ground','2'),
#     Pokemon('Corsola','222','Coral Pokémon','water','rock','2'),
#     Pokemon('Remoraid','223','Jet Pokémon','water','n/a','2'),
#     Pokemon('Octillery','224','Jet Pokémon','water','n/a','2'),
#     Pokemon('Delibird','225','Delivery Pokémon','ice','flying','2'),
#     Pokemon('Mantine','226','Kite Pokémon','water','flying','2'),
#     Pokemon('Skarmory','227','Armor Bird Pokémon','steel','flying','2'),
#     Pokemon('Houndour','228','Dark Pokémon','dark','fire','2'),
#     Pokemon('Houndoom','229','Dark Pokémon','dark','fire','2'),
#     Pokemon('Kingdra','230','Dragon Pokémon','water','dragon','2'),
#     Pokemon('Phanpy','231','Long Nose Pokémon','ground','n/a','2'),
#     Pokemon('Donphan','232','Armor Pokémon','ground','n/a','2'),
#     Pokemon('Porygon2','233','Virtual Pokémon','normal','n/a','2'),
#     Pokemon('Stantler','234','Big Horn Pokémon','normal','n/a','2'),
#     Pokemon('Smeargle','235','Painter Pokémon','normal','n/a','2'),
#     Pokemon('Tyrogue','236','Scuffle Pokémon','fighting','n/a','2'),
#     Pokemon('Hitmontop','237','Handstand Pokémon','fighting','n/a','2'),
#     Pokemon('Smoochum','238','Kiss Pokémon','ice','psychic','2'),
#     Pokemon('Elekid','239','Electric Pokémon','electric','n/a','2'),
#     Pokemon('Magby','240','Live Coal Pokémon','fire','n/a','2'),
#     Pokemon('Miltank','241','Milk Cow Pokémon','normal','n/a','2'),
#     Pokemon('Blissey','242','Happiness Pokémon','normal','n/a','2'),
#     Pokemon('Raikou','243','Thunder Pokémon','electric','n/a','2'),
#     Pokemon('Entei','244','Volcano Pokémon','fire','n/a','2'),
#     Pokemon('Suicune','245','Aurora Pokémon','water','n/a','2'),
#     Pokemon('Larvitar','246','Rock Skin Pokémon','rock','ground','2'),
#     Pokemon('Pupitar','247','Hard Shell Pokémon','rock','ground','2'),
#     Pokemon('Tyranitar','248','Armor Pokémon','rock','dark','2'),
#     Pokemon('Lugia','249','Diving Pokémon','psychic','flying','2'),
#     Pokemon('Ho-Oh','250','Rainbow Pokémon','fire','flying','2'),
#     Pokemon('Celebi','251','Time Travel Pokémon','psychic','grass','2')
#     ]