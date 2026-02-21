import os

# Create _strains directory
os.makedirs('_strains', exist_ok=True)

# Strain data
strains = [
    {
        "name": "Green Aceh", "color": "green", "region": "Aceh", "price": 49.99, "speed": "balanced",
        "premium": True, "limited": False, "energy": 9, "focus": 6, "pain": 4, "anxiety": 3, "social": 9,
        "time_of_day": ["morning", "afternoon", "evening"], "tags": ["Rare", "Potent", "Social", "Experienced Only"],
        "vibe": "a critically endangered Sumatran tiger pads swiftly through the vibrant understory of an ancient jungle",
        "characteristics": "Intense - Raw - Vital",
        "short_desc": "Legendary variety, exceedingly rare. Possibly the most powerful strain of Mitragyna speciosa on earth.",
        "full_desc": """Legendary variety, exceedingly rare. 

Not a strain you're likely to find elsewhere besides the wishlist of the nerdiest of kratom connoisseurs. This is a local variety indigenous to the autonomous Aceh region of western Sumatra in the beautiful archipelago of Indonesia. Aceh's dense rainforest cradles the greatest biodiversity in all of Pacific Asia. Our Green Aceh kratom is quite possibly the most powerful strain of Mitragyna speciosa on earth and possesses extremely potent narcotic properties."""
    },
    {
        "name": "Green Dragon", "color": "green", "region": "Thai", "price": 34.99, "speed": "balanced",
        "premium": False, "limited": False, "energy": 6, "focus": 7, "pain": 5, "anxiety": 6, "social": 8,
        "time_of_day": ["morning", "afternoon"], "tags": ["Euphoric", "Balanced", "Flagship"],
        "vibe": "in a coastal cave like a hidden temple, an ancient jade dragon named Thang perches upon his pile of gems",
        "characteristics": "Euphoric - Powerful - Sparkling",
        "short_desc": "Flagship special variety. Extremely strong and well-balanced profile, dried indoors following traditional methods.",
        "full_desc": """Flagship, special variety.

The Dragon variety of kratom is kind of our Thang thang– a personal favorite of ours, quite uncommon to see for sale in the West. The extremely strong and well-balanced profile of Green Dragon, dried indoors following traditional methods to preserve potency, truly can't be beat. This alkaloid-rich Mitragyna sp. varietal originally sourced from Thailand."""
    },
    {
        "name": "Green Maeng Da", "color": "green", "region": "Thai", "price": 34.99, "speed": "fast",
        "premium": False, "limited": False, "energy": 8, "focus": 9, "pain": 6, "anxiety": 4, "social": 5,
        "time_of_day": ["morning", "afternoon"], "tags": ["Productivity", "Gold Standard", "Strong"],
        "vibe": "a neon ghost of the city sits cross-legged on a skytrain bench, humming along to music only he can hear",
        "characteristics": "Potent - Balanced - Popular",
        "short_desc": "Premium classic green blended for potency. The gold standard for productivity.",
        "full_desc": """Premium classic green blended for potency.

Hailing from Thailand, this famous variety is not so much a botanical strain as it is Thai slang for a premium grade of kratom. Much like the city of Bangkok, Green Maeng Da is a super potent blend of kratoms from the surrounding regions. Each supplier's Maeng Da will be blended differently from the next, and we think that our guy's blend is the best of the best. This powder consists of many of our farmer's most high-potency strains, blended for optimum balance and pleasure."""
    },
    {
        "name": "Green Malay", "color": "green", "region": "Borneo", "price": 34.99, "speed": "balanced",
        "premium": False, "limited": False, "energy": 6, "focus": 7, "pain": 6, "anxiety": 5, "social": 7,
        "time_of_day": ["morning", "afternoon", "evening"], "tags": ["Long Lasting", "Versatile", "Reliable"],
        "vibe": "a solitary orangutan contemplates a tangerine wash over the South China Sea, as if meditating upon the dawn",
        "characteristics": "Balanced - Uplifting - Effective",
        "short_desc": "USA Bestseller, dependable strain. Long duration and exceptionally alkaloid-rich profile.",
        "full_desc": """USA Bestseller, dependable strain.

A longstanding customer favorite, Green Malay originates in the jungles of Northern Borneo in the Malaysian states of Sabah and Sarawak. The area is a premier hotspot for ecotourism due to its vibrant biodiversity and the local variety of Mitragyna sp. is known for its exceptionally alkaloid-rich profile. Often described as euphoric, Green Malay offers well-balanced and versatile effects."""
    },
    {
        "name": "Super Green", "color": "green", "region": "Borneo", "price": 34.99, "speed": "fast",
        "premium": False, "limited": False, "energy": 10, "focus": 9, "pain": 5, "anxiety": 3, "social": 6,
        "time_of_day": ["morning"], "tags": ["Maximum Potency", "Espresso-like", "Blend"],
        "vibe": "from his bamboo porch, a hardworking father overlooks a misty plantation with a steaming morning cuppa and a hand-rolled cigarette",
        "characteristics": "Energetic - Smooth - Inspiring",
        "short_desc": "Our farmer's personal favorite strain. Maximum potency blend for smooth energy.",
        "full_desc": """Our farmer's personal favorite strain.

Another blend formulated for optimum strength, but this time also for smoothness. The effects of Super Green can be compared to a strong cup of coffee. In fact, our farmer likes to prepare his in an old school pour-over coffee maker and drink in the morning to motivate his intensive work days on the plantation."""
    },
    {
        "name": "Green Thai", "color": "green", "region": "Thai", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": False, "energy": 6, "focus": 8, "pain": 7, "anxiety": 4, "social": 6,
        "time_of_day": ["morning", "afternoon"], "tags": ["Traditional", "Calm Energy", "Pain Relief"],
        "vibe": "grandmother chews her quid as she chats, nimble fingers working tirelessly to embroider a rich, heirloom tapestry",
        "characteristics": "Gentle - Fortifying - Energetic",
        "short_desc": "Traditional green variety. Provides relief from pain and fatigue to get you through your toughest day.",
        "full_desc": """Traditional green variety.

As the name would suggest, Green Thai is a variety of Mitragyna speciosa that is Indigenous to Thailand. Traditionally chewed as a quid or prepared as tea by the local people, the Thai prize kratom for its performance enhancing effects, medicinal benefits, and as a form of hospitality. Green Thai provides relief from pain and fatigue to get you through your toughest day."""
    },
    {
        "name": "Green Dracula", "color": "green", "region": "Aceh", "price": 34.99, "speed": "fast",
        "premium": False, "limited": True, "energy": 9, "focus": 7, "pain": 4, "anxiety": 4, "social": 8,
        "time_of_day": ["afternoon", "evening"], "tags": ["Limited", "Exclusive", "Collectible"],
        "vibe": "he appears as an elegant youth, a knowing glint in dark eyes like pools reflecting many ages of man gone by",
        "characteristics": "Exclusive - Rare - Intense",
        "short_desc": "Exclusive strain with a bite. Unique opportunity, not a daily driver.",
        "full_desc": """Exclusive strain with a bite.

Limited edition collector's strain from the Aceh region. Not your typical green—this variety offers a unique alkaloid profile that bites harder than standard strains. For the connoisseur seeking something truly exclusive."""
    },
    {
        "name": "Red Aceh", "color": "red", "region": "Aceh", "price": 49.99, "speed": "slow",
        "premium": True, "limited": False, "energy": 2, "focus": 3, "pain": 10, "anxiety": 9, "social": 2,
        "time_of_day": ["evening"], "tags": ["Couch Lock", "Heavy", "Sedating", "Pain Relief"],
        "vibe": "the heavy velvet curtain of night falls over a ancient temple, incense smoke curling in thick spirals",
        "characteristics": "Narcotic - Analgesic - Sedative",
        "short_desc": "Legendary red variety, super rare. Fermented version perfect for nighttime use and heavy pain relief.",
        "full_desc": """Legendary red variety, super rare.

Not a strain you're likely to find elsewhere besides the wishlist of the nerdiest of kratom connoisseurs. This is a local variety indigenous to the autonomous Aceh region of western Sumatra in the beautiful archipelago of Indonesia. Aceh's dense rainforest cradles the greatest biodiversity in all of Pacific Asia. A fermented version of the Aceh strain, Red Aceh is perfect for nighttime use and heavy pain relief with powerful opiate-like effects."""
    },
    {
        "name": "Red Thai", "color": "red", "region": "Thai", "price": 34.99, "speed": "slow",
        "premium": False, "limited": False, "energy": 3, "focus": 4, "pain": 7, "anxiety": 6, "social": 4,
        "time_of_day": ["afternoon", "evening"], "tags": ["Traditional", "Slow Creeper", "Gentle"],
        "vibe": "a saffron-robed monk walks slowly through morning mist, each step deliberate and grounded",
        "characteristics": "Traditional - Smooth - Reliable",
        "short_desc": "Traditional red for pain relief and relaxation, strong and smooth. Slow creeper.",
        "full_desc": """Traditional red for pain relief and relaxation.

The classic Thai red profile—slow, smooth, and grounding. This strain creeps up gently but provides substantial relief. Suitable for both daytime pain management (in lower doses) and evening relaxation."""
    },
    {
        "name": "Red Dragon", "color": "red", "region": "Thai", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": False, "energy": 5, "focus": 4, "pain": 6, "anxiety": 5, "social": 9,
        "time_of_day": ["evening"], "tags": ["Social", "Aphrodisiac", "Mood Lift", "Hot Red"],
        "vibe": "candles flicker in red silk lanterns as laughter echoes through hidden courtyards",
        "characteristics": "Social - Euphoric - Unique",
        "short_desc": "Most unusual, 'hot red' variety, social lubricant and aphrodisiac. Different from Green Dragon.",
        "full_desc": """Most unusual, "hot red" variety.

Unlike the typical sedating red, Red Dragon brings heat and sociability. This is an aphrodisiac and great for socializing—a unique characteristic among red veins. Different from Green Dragon in every way except the name."""
    },
    {
        "name": "Red Bali", "color": "red", "region": "Borneo", "price": 34.99, "speed": "slow",
        "premium": False, "limited": False, "energy": 2, "focus": 2, "pain": 9, "anxiety": 8, "social": 3,
        "time_of_day": ["evening"], "tags": ["Classic", "Pain Relief", "Sedating", "Beginner Friendly"],
        "vibe": "a warm bath by candlelight, every muscle releasing tension into steaming water",
        "characteristics": "Classic - Heavy - Comforting",
        "short_desc": "Gold standard pain relief, stimulant-free. Best for relief, purely sedating.",
        "full_desc": """Gold standard pain relief.

The classic red Bali feel that built the reputation of red vein kratom. Purely sedating and stimulant-free, this is best for pain relief and deep relaxation. The standard by which all other reds are measured."""
    },
    {
        "name": "Red Maeng Da", "color": "red", "region": "Thai", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": False, "energy": 6, "focus": 5, "pain": 7, "anxiety": 5, "social": 4,
        "time_of_day": ["afternoon"], "tags": ["Premium Red", "Stronger", "Balanced"],
        "vibe": "a tiger lounges in the shade, powerful but at ease, ready to move if needed",
        "characteristics": "Premium - Strong - Balanced",
        "short_desc": "Premium classic red blended for potency. Stronger energy than typical reds.",
        "full_desc": """Premium classic red blended for potency.

Not your typical sedating red—Red Maeng Da maintains moderate energy levels while delivering premium pain relief. The middle ground for those who need relief but can't afford to be completely couch-locked."""
    },
    {
        "name": "Chocolate Bentuangie", "color": "red", "region": "Borneo", "price": 34.99, "speed": "slow",
        "premium": False, "limited": True, "energy": 1, "focus": 2, "pain": 8, "anxiety": 7, "social": 2,
        "time_of_day": ["evening"], "tags": ["Fermented", "Smooth", "Best Taste", "Limited"],
        "vibe": "rich dark chocolate melts on the tongue in a quiet, wood-paneled study",
        "characteristics": "Fermented - Smooth - Gentle",
        "short_desc": "Unique fermented kratom leaf. Best tasting, smooth, no tummy upset.",
        "full_desc": """Unique fermented kratom leaf.

The fermentation process creates a chocolate-like aroma and taste while smoothing out the edges of the kratom experience. Best tasting kratom, smooth, gentle, and easy on the stomach. Purely sedative in effects."""
    },
    {
        "name": "White Maeng Da", "color": "white", "region": "Thai", "price": 34.99, "speed": "fast",
        "premium": False, "limited": False, "energy": 9, "focus": 9, "pain": 4, "anxiety": 3, "social": 5,
        "time_of_day": ["morning"], "tags": ["Coffee Alternative", "Clean Energy", "Morning", "Beginner Friendly"],
        "vibe": "the first ray of sunlight piercing through high mountain mist, crystal clear and sharp",
        "characteristics": "Fast - Clean - Focused",
        "short_desc": "Fast energy. Good for coffee replacement. Clean stimulation, beginner friendly.",
        "full_desc": """Fast energy. Perfect coffee replacement.

Clean, fast-acting energy without the jitters of caffeine. This is the white vein standard for morning productivity and focus. Beginner friendly despite the potency."""
    },
    {
        "name": "White Aceh", "color": "white", "region": "Aceh", "price": 49.99, "speed": "fast",
        "premium": True, "limited": False, "energy": 9, "focus": 8, "pain": 3, "anxiety": 4, "social": 6,
        "time_of_day": ["morning", "afternoon"], "tags": ["Intense", "Smooth", "Premium", "Rare"],
        "vibe": "lightning captured in a bottle, electric and brilliant but controlled",
        "characteristics": "Intense - Smooth - Premium",
        "short_desc": "Legendary, rare variety for fast, potent energy. Smoother but more intense than White MD.",
        "full_desc": """Legendary, rare variety for fast, potent energy.

Smooth but intense. Medium duration, maybe stronger than White MD. From the same Aceh region as our premium Green and Red Aceh, this white vein carries the intensity and rarity of its lineage."""
    },
    {
        "name": "White Horn", "color": "white", "region": "Borneo", "price": 34.99, "speed": "fast",
        "premium": False, "limited": False, "energy": 8, "focus": 7, "pain": 3, "anxiety": 3, "social": 5,
        "time_of_day": ["morning"], "tags": ["Potent", "Energetic", "Premium", "Athletes"],
        "vibe": "a sprinter exploding from starting blocks, pure kinetic force unleashed",
        "characteristics": "Potent - Energetic - Aggressive",
        "short_desc": "Special horned leaf loved by athletes. Premium energetic profile, not smooth come-up.",
        "full_desc": """Special horned leaf loved by athletes.

Named for the horn-shaped leaves of the mature trees. Not a smooth come-up, but delivers aggressive energy perfect for physical performance. Premium energetic profile favored by those who need to push their limits."""
    },
    {
        "name": "White Sumatra", "color": "white", "region": "Sumatra", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": False, "energy": 6, "focus": 8, "pain": 4, "anxiety": 5, "social": 4,
        "time_of_day": ["morning"], "tags": ["Light", "Focus", "Gentle", "Beginner Friendly"],
        "vibe": "a clear mountain stream flowing over smooth stones, steady and refreshing",
        "characteristics": "Light - Focused - Smooth",
        "short_desc": "Traditional white type for smooth energy. Lighter regional variety, best for focus.",
        "full_desc": """Traditional white type for smooth energy.

Heavier or lighter than other whites? Lighter. Best for focus and concentration without the intensity of Maeng Da or Aceh. A gentle introduction to white veins for beginners."""
    },
    {
        "name": "White Elephant", "color": "white", "region": "Borneo", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": False, "energy": 7, "focus": 6, "pain": 5, "anxiety": 5, "social": 5,
        "time_of_day": ["morning", "afternoon"], "tags": ["Unusual", "Strong", "Large Leaf", "Balanced"],
        "vibe": "a wise matriarch leads her herd with steady, purposeful steps through dense jungle",
        "characteristics": "Unusual - Strong - Balanced",
        "short_desc": "Special elephant leaf. Unusual large leaf type with strong but manageable profile.",
        "full_desc": """Special elephant leaf.

Large leaves from mature trees create a different alkaloid profile—strong but more mellow than typical whites. Unusual leaf type for those seeking something off the beaten path."""
    },
    {
        "name": "White Zombie", "color": "white", "region": "Thai", "price": 34.99, "speed": "fast",
        "premium": False, "limited": True, "energy": 8, "focus": 7, "pain": 4, "anxiety": 4, "social": 7,
        "time_of_day": ["morning"], "tags": ["Limited", "Novelty", "Rare", "Exclusive"],
        "vibe": "a rock concert at midnight, electric energy surging through a sea of raised hands",
        "characteristics": "Exclusive - Energetic - Novelty",
        "short_desc": "Exclusively bred strain by Sitra. Named after the band, rare collector item.",
        "full_desc": """Exclusively bred strain by Sitra.

Named after the band, this novelty strain is a rare collector item. Fine for beginners despite the aggressive name. Exclusive limited release."""
    },
    {
        "name": "Yellow Dragon", "color": "yellow", "region": "Thai", "price": 34.99, "speed": "balanced",
        "premium": False, "limited": False, "energy": 5, "focus": 5, "pain": 5, "anxiety": 8, "social": 8,
        "time_of_day": ["evening"], "tags": ["Euphoric", "Social", "Evening", "Anxiety Relief"],
        "vibe": "golden hour sunlight spilling through amber whiskey in a crystal glass",
        "characteristics": "Euphoric - Social - Smooth",
        "short_desc": "Thang's personal favorite for euphoric anxiety relief. More euphoric than other yellows.",
        "full_desc": """Thang's personal favorite for euphoric anxiety relief.

More euphoric than other yellows. Evening or for daytime anxiety—this is the social yellow. The Dragon name carries the same quality as its green counterpart but with a golden twist."""
    },
    {
        "name": "Yellow Hulu", "color": "yellow", "region": "Hulu", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": False, "energy": 4, "focus": 6, "pain": 5, "anxiety": 9, "social": 6,
        "time_of_day": ["afternoon"], "tags": ["Anxiolytic", "Kapuas", "Balanced", "Best for Anxiety"],
        "vibe": "a quiet canoe drifting down a misty river, surrounded by ancient forest",
        "characteristics": "Anxiolytic - Smooth - Gentle",
        "short_desc": "Best strain for anxiety relief. Kapuas region, medium duration, smooth.",
        "full_desc": """Best strain for anxiety relief.

From the Kapuas region of Borneo, this variety specializes in anxiolytic properties. Medium duration, smooth, and specifically targeted at anxiety without heavy sedation."""
    },
    {
        "name": "Yellow Vietnam", "color": "yellow", "region": "Vietnam", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": False, "energy": 6, "focus": 7, "pain": 4, "anxiety": 8, "social": 5,
        "time_of_day": ["morning", "afternoon"], "tags": ["Rare", "Clear-headed", "Anxiety Relief", "Regional"],
        "vibe": "rice paddies reflect the morning sun like a thousand mirrors, peaceful and bright",
        "characteristics": "Rare - Clear-headed - Uplifting",
        "short_desc": "Well-rounded energy and relaxation. Great for anxiety without sedation.",
        "full_desc": """Well-rounded energy and relaxation.

Great for anxiety without sedation. Faster than other yellows but still balanced. Rare regional variety from the Vietnamese highlands."""
    },
    {
        "name": "Yellow Maeng Da", "color": "yellow", "region": "Thai", "price": 34.99, "speed": "balanced",
        "premium": False, "limited": False, "energy": 5, "focus": 6, "pain": 5, "anxiety": 7, "social": 6,
        "time_of_day": ["afternoon"], "tags": ["Premium Process", "Balanced", "Smooth", "Blend"],
        "vibe": "a master craftsman perfecting his technique, every movement precise and intentional",
        "characteristics": "Premium - Balanced - Refined",
        "short_desc": "Premium yellow blend for balanced potency. Premium drying process creates great balance.",
        "full_desc": """Premium yellow blend for balanced potency.

Premium drying process. Great balanced blend that represents the middle path—equal parts energy and relaxation, suitable for any afternoon."""
    },
    {
        "name": "Yellow Thai", "color": "yellow", "region": "Thai", "price": 34.99, "speed": "moderate",
        "premium": False, "limited": True, "energy": 4, "focus": 5, "pain": 6, "anxiety": 8, "social": 6,
        "time_of_day": ["evening"], "tags": ["Limited", "Traditional", "Gentle", "Pain Relief"],
        "vibe": "old scrolls and sandalwood in a quiet temple library, wisdom passed down through generations",
        "characteristics": "Traditional - Gentle - Strong",
        "short_desc": "Gentle, uplifting anxiety and pain relief. Traditional method, well-balanced anxiolytic.",
        "full_desc": """Gentle, uplifting anxiety and pain relief.

Traditional Thai method creates a gentle but strong, well-balanced anxiolytic. Limited availability. When to choose this? To take the edge off without losing yourself."""
    }
]

def format_list(items):
    """Format Python list as YAML list"""
    if not items:
        return "[]"
    return "\n" + "\n".join([f"  - {item}" for item in items])

def format_front_matter(strain):
    """Manually format YAML front matter to avoid yaml dependency"""
    lines = [
        "---",
        f"name: {strain['name']}",
        f"color: {strain['color']}",
        f"region: {strain['region']}",
        f"price: {strain['price']}",
        f"speed: {strain['speed']}",
        f"premium: {'true' if strain['premium'] else 'false'}",
        f"limited: {'true' if strain['limited'] else 'false'}",
        f"energy: {strain['energy']}",
        f"focus: {strain['focus']}",
        f"pain: {strain['pain']}",
        f"anxiety: {strain['anxiety']}",
        f"social: {strain['social']}",
        f"time_of_day:{format_list(strain['time_of_day'])}",
        f"tags:{format_list(strain['tags'])}",
        f"vibe: \"{strain['vibe']}\"",
        f"characteristics: \"{strain['characteristics']}\"",
        f"short_desc: \"{strain['short_desc']}\"",
        "---"
    ]
    return "\n".join(lines)

# Generate files
for strain in strains:
    # Create filename
    filename = strain['name'].lower().replace(' ', '-').replace('(', '').replace(')', '') + '.md'
    filepath = os.path.join('_strains', filename)
    
    # Build content
    content = f"""{format_front_matter(strain)}

**VIBES:** {strain['vibe']}

**{strain['characteristics']}**

{strain['full_desc']}
"""
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {filename}")

print(f"\n✅ Generated {len(strains)} strain files in _strains/")
print("Next steps:")
print("1. Delete the hardcoded cards from catalog.html")
print("2. Update _config.yml to include the strains collection:")
print("""
collections:
  strains:
    output: true
    permalink: /strains/:name/
""")
print("3. Run: bundle exec jekyll serve")