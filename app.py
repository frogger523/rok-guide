from __future__ import annotations

from datetime import date
from pathlib import Path

from flask import Flask, jsonify, render_template


BASE_DIR = Path(__file__).resolve().parent


ROADMAP = [
    {
        "window": "BEFORE DAY 0",
        "target": "Pick the kingdom, not just the account",
        "power": "SETUP",
        "actions": [
            "Join a coordinated restart project before creating the character; top-alliance access is the largest early accelerator.",
            "Choose China for building speed, AP recovery, and guaranteed Sun Tzu sculptures.",
            "Prefer creating in or targeting the actual destination kingdom when current mechanics allow it; treat any sleeper or jumper route as conditional.",
            "Budget honestly: F2P, micro ($5–25/month), or competitive. The route changes; the rules do not.",
        ],
        "checkpoint": "You know the final kingdom, alliance, reset time, guardian schedule, and spending ceiling.",
    },
    {
        "window": "HOURS 0–24",
        "target": "Unlock both queues and never idle",
        "power": "~150–250K",
        "actions": [
            "Rush City Hall prerequisites; use free second-builder items until VIP 6 makes the second queue permanent.",
            "Join the strongest active alliance that accepts you, teleport to territory, and collect helps before every speedup.",
            "Keep builders, research, troop training, scouts, and marches active at all times.",
            "Level Sun Tzu; unlock gatherers; spend natural AP but preserve bottles for high-return events.",
        ],
        "checkpoint": "Two builders, two scouts as soon as unlocked, four training queues, and every march gathering overnight.",
    },
    {
        "window": "DAYS 2–7",
        "target": "Convert activity into compounding speed",
        "power": "~0.7–1.5M",
        "actions": [
            "Push City Hall and Academy; research Engineering and Mathematics while villages supply free low-level economy tech.",
            "Clear fog, caves, tribal villages, Expedition, guardians, Lohar event, forts, and every alliance objective.",
            "Specialize commanders by role: use available combat pairs now, Peacekeepers for PvE, and gatherers for resources. Build toward Sun Tzu + Aethelflaed as Expedition unlocks her sculptures.",
            "Create the first couple of farms early if your playtime supports them; their simple economy loops should mature before the main hits severe resource gates.",
        ],
        "checkpoint": "Hidden Lotus at 1.5M is an optional grind benchmark—not worth crippling commander skills or speedup timing to force.",
    },
    {
        "window": "DAYS 8–20",
        "target": "Reach T3, then set up the T4 sprint",
        "power": "~2–4M",
        "actions": [
            "Continue the City Hall rush through CH16+; unlock march slots and concentrate military research into the first fighting troop.",
            "VERIFY CURRENT IN-GAME RULES before any sleeper move: confirm the exact destination, kingdom ages, Pioneer status, geographic access, and migration eligibility immediately beforehand.",
            "Collect Pass/altar/monument rewards with the top alliance and stockpile universals for timed power events.",
            "Craft one coherent set for the troop type your existing research and commander progress best support. Do not dilute materials across several marches.",
        ],
        "checkpoint": "Never build the restart around a migration that has not been verified. Eligibility and destination access are more important than a generic sleeper power benchmark.",
    },
    {
        "window": "DAYS 21–45",
        "target": "T4 online; economy becomes the weapon",
        "power": "~5–10M",
        "actions": [
            "Unlock one T4 type first, then the remaining types needed for rallies and troop balance.",
            "Push VIP 10 during More Than Gems; keep forts running for Books of Covenant and alliance credits.",
            "Move farms toward multiple gathering marches, economy tech, production, and a Trading Post; CH17 and CH22 are useful march-count targets, not reasons to build them like mains.",
            "Bank healing and training speedups for event overlap instead of spending them for cosmetic daily power.",
        ],
        "checkpoint": "One real field march, enough T4 to fill it, strong alliance standing, and a sustainable resource pipeline.",
    },
    {
        "window": "PRE-KVK → KVK 1",
        "target": "Arrive rich, focused, and healable",
        "power": "ACCOUNT-DEPENDENT",
        "actions": [
            "Spend saved AP on the highest-return Pre-KvK phase your kingdom calls; follow leadership instructions over generic guides.",
            "Enter with hospital capacity, shields, teleports, AP, and resources—not just inflated troop power.",
            "Field the strongest complete pair your account can support—often Sun Tzu + Aethelflaed or YSG by then—and wait to add a march until it has comparable support.",
            "Fight with the ball, refresh early, record deaths and kill points, and meet kingdom contribution expectations.",
        ],
        "checkpoint": "The goal is positive contribution per resource spent, not a screenshot power number.",
    },
]


DAILY_LOOP = [
    ["RESET + 0–15m", "Collect VIP/chests, Tavern, daily offers, free AP; donate tech; start daily objectives."],
    ["MORNING", "Run guardians with peacekeepers, spend natural AP below cap, refresh all queues, send gatherers."],
    ["MIDDAY", "Expedition, Canyon, Courier, alliance events, forts; collect helps before finishing anything."],
    ["EVENING", "Second guardian cycle, rallies and scheduled objectives; preload long build/research with rune + title."],
    ["BEFORE BED", "Long queues, full resource nodes, protected resources, empty AP bar when an event justifies it."],
]


META_MARCHES = [
    {
        "rank": 1,
        "primary": "Qin Shi Huang",
        "secondary": "Yi Seong-Gye",
        "short_secondary": "YSG",
        "troop": "Archer",
        "archetype": "Skill / AoE",
        "formation": "Wedge",
        "grade": "S+",
        "confidence": "Core",
        "why": "QSH turns rage into relentless area pressure while bringing unusual durability for an archer march. YSG is the efficient, proven deputy; Zhuge Liang is the premium alternative when available.",
        "swap": "QSH + Zhuge Liang",
        "investment": "A theoretical top pairing and a strong first SoC option when archer gear, research, armaments, and an invested YSG already support it—not a universal first project.",
    },
    {
        "rank": 2,
        "primary": "Sun Tzu (Prime)",
        "secondary": "Bai Qi",
        "short_secondary": "Bai Qi",
        "troop": "Infantry",
        "archetype": "Smite / AoE",
        "formation": "Pincer",
        "grade": "S+",
        "confidence": "Core",
        "why": "A 900-rage cycle, fixed true-damage pressure, and Bai Qi's multi-target Smite create the defining infantry murderball march.",
        "swap": "Sun Prime + Liu Che",
        "investment": "May be the better first project for an infantry-developed account. Commit only when sculptures, deputy, Pincer armaments, research, and a complete set line up.",
    },
    {
        "rank": 3,
        "primary": "Arthur Pendragon",
        "secondary": "Achilles",
        "short_secondary": "Achilles",
        "troop": "Cavalry",
        "archetype": "Combo / Burst",
        "formation": "Wedge",
        "grade": "S",
        "confidence": "Core",
        "why": "The cleanest one-march cavalry package: excellent combo pressure, mobility, and enough threat to punish isolated targets.",
        "swap": "Gang Gamchan + Achilles",
        "investment": "A premier cavalry reference pairing. Its account priority rises sharply when cavalry tech, equipment, armaments, and commander progress are already strongest.",
    },
    {
        "rank": 4,
        "primary": "Hermann (Prime)",
        "secondary": "Alp Arslan",
        "short_secondary": "Alp Arslan",
        "troop": "Archer",
        "archetype": "Pierce / Debuff",
        "formation": "Wedge",
        "grade": "S",
        "confidence": "Deep roster",
        "why": "Alp spreads valuable poison and skill-damage-taken debuffs while Hermann supplies AoE, speed, and field utility.",
        "swap": "Alp Arslan + Zhuge Liang",
        "investment": "Excellent second archer march; skip if the armaments and gear would be weak.",
    },
    {
        "rank": 5,
        "primary": "Liu Che",
        "secondary": "Philip II",
        "short_secondary": "Philip II",
        "troop": "Infantry",
        "archetype": "Normal / Smite",
        "formation": "Pincer",
        "grade": "S",
        "confidence": "Deep roster",
        "why": "A durable second infantry line with strong sustained pressure. It frees Bai Qi for Sun Prime in a five-march lineup.",
        "swap": "Philip II + Bai Qi",
        "investment": "A roster-expansion march, not a better first project than the core three.",
    },
]


STAGES = [
    {
        "id": "kvk1",
        "eyebrow": "Days 1–120",
        "name": "KvK 1",
        "title": "Win by concentrating power",
        "summary": "One complete march beats three half-built marches. China is the cleanest start; Sun Tzu is an early anchor, while Aethelflaed is a core you build toward through Expedition.",
        "marches": [
            ["F2P target", "Sun Tzu + Aethelflaed", "An inexpensive AoE/debuff core to build toward as Expedition supplies Aethelflaed; use your best available pair in the meantime."],
            ["Best value", "Sun Tzu + YSG", "Double AoE and excellent chaining; only commit if YSG fits your swap plan."],
            ["No gold heads", "Björn + Sun Tzu", "Safe all-epic infantry pair and easy equipment path."],
            ["Cavalry utility", "Belisarius + Baibars", "Fast farm-killing and cleanup—not a murderball centerpiece."],
        ],
        "do": ["Reach VIP 10 quickly, then work toward VIP 12/14", "Run five gatherers while offline", "Craft one coherent purple/blue equipment set", "Save universals or fund one planned early commander with a verified swap exit"],
        "avoid": ["Gold heads into tavern commanders", "Three fighting marches with bad gear", "Healing bad trades just to inflate kill points"],
    },
    {
        "id": "kvk2",
        "eyebrow": "Transition season",
        "name": "KvK 2",
        "title": "The temptation trap",
        "summary": "KvK2 offers useful but often short-lived commanders. Low spenders should strengthen one march and plan the KvK3/SoC swap instead of scattering sculptures.",
        "marches": [
            ["Ceiling", "Pyrrhus + Cheok Jun-gyeong", "The current premium infantry pairing when both are properly built."],
            ["Legacy bridge", "Alexander + YSG", "Still functional and exchange-friendly, but not a fresh SoC investment."],
            ["Archer ceiling", "Cyrus + YSG", "Strong season-specific output; expensive for its remaining shelf life."],
            ["Budget bridge", "Sun Tzu + YSG", "Keep the KvK1 core if the alternative is spreading sculptures and gear."],
        ],
        "do": ["Judge every commander by current value and verified swap eligibility", "Finish accessories for the first march", "Save universals—or deliberately build one high-value donor such as YSG with a written exit plan"],
        "avoid": ["Two 5511 projects just because they unlocked", "New cavalry gear without a future cavalry pair", "Treating a tier list as an investment list"],
    },
    {
        "id": "kvk3",
        "eyebrow": "The power spike",
        "name": "KvK 3",
        "title": "Exchange into the modern game",
        "summary": "Commander swaps can turn deliberate early investment into a modern core. Exact eligibility can change, so verify the live rules before committing or transferring hundreds of sculptures.",
        "marches": [
            ["Archer pivot", "Qin Shi Huang + YSG", "The simplest elite transition when YSG was built early."],
            ["Infantry pivot", "Sun Tzu (Prime) + Bai Qi", "The Smite core; use Pincer and real infantry gear."],
            ["Lower-cost inf", "Sun Prime + Liu Che", "An excellent alternative if Liu Che already exists or Bai Qi is unavailable."],
            ["Cavalry pivot", "Arthur + Achilles", "Strong, but build after the account has a stable first march."],
        ],
        "do": ["Enter the swap window with a written donor and target plan", "Verify current swap eligibility in-game before committing", "Build the formation before expecting meta results"],
        "avoid": ["Exchanging based on one battle report", "Maxing a deputy without gear for its march", "Unlocking every new commander"],
    },
    {
        "id": "soc",
        "eyebrow": "Season of Conquest",
        "name": "SoC",
        "title": "Finish one; expand from account strength",
        "summary": "The list below is an endgame reference, not a mandatory build order. Finish the strongest march your gear, research, armaments, commanders, sculptures, and economy can support, then branch only when another march can be equipped properly.",
        "marches": [
            ["Core 1", "QSH + YSG / Zhuge", "Your archer damage engine and best mass-fight value."],
            ["Core 2", "Sun Prime + Bai Qi / Liu Che", "Infantry AoE with Pincer-driven Smite pressure."],
            ["Core 3", "Arthur + Achilles", "Cavalry burst and chase capability."],
            ["Core 4–5", "Hermann + Alp; Liu Che + Philip", "Only after gear, accessories, armaments, and Crystal Tech can support them."],
        ],
        "do": ["Max economy Crystal Tech before combat branches", "Buy tech for marches you actually field", "Expand from existing account strengths—not generic rank order", "Fight inside your murderball and refresh before red health"],
        "avoid": ["Five marches on two-march Crystal Tech", "Solo chasing into enemy territory", "Fresh heads into aging former-meta commanders"],
    },
]


SOURCES = [
    {
        "name": "RoK subreddit — August 2026 restart conditions",
        "url": "https://www.reddit.com/r/RiseofKingdoms/comments/1viuxqx/restarting_new_account/",
        "date": "August 8, 2026",
        "use": "Current warning on Pioneer kingdoms, regional access, and restart-project volatility.",
    },
    {
        "name": "RoK subreddit — current sleeper viability",
        "url": "https://www.reddit.com/r/RiseofKingdoms/comments/1ulcgsg/restart_account/",
        "date": "July 2, 2026",
        "use": "Current restart-project consensus: sleepers remain conditional and may be restricted.",
    },
    {
        "name": "Heaven Guardian — 2026 beginner guide",
        "url": "https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/",
        "date": "July 22, 2026",
        "use": "Civilization, city growth, gathering, AP, and early-account fundamentals.",
    },
    {
        "name": "Heaven Guardian — gem spending priority",
        "url": "https://heaven-guardian.com/rise-of-kingdoms-gem-spending-guide/",
        "date": "June 23, 2026",
        "use": "VIP 6/10, More Than Gems, and Castle bottleneck priorities.",
    },
    {
        "name": "Rise of Kingdoms Guides — farm accounts",
        "url": "https://riseofkingdomsguides.com/rise-of-kingdoms-farm-account/",
        "date": "January 2, 2026",
        "use": "Two-character limit per kingdom/account and economic farm setup.",
    },
    {
        "name": "Rise of Kingdoms Guides — City Hall requirements",
        "url": "https://riseofkingdomsguides.com/rise-of-kingdoms-city-hall-requirements-and-cost/",
        "date": "January 2, 2026",
        "use": "CH25 path, prerequisites, costs, and speedup constraints.",
    },
    {
        "name": "RoK subreddit — July 2026 early power benchmarks",
        "url": "https://www.reddit.com/r/RiseofKingdoms/comments/1uydjo9/where_am_i_lacking_power/",
        "date": "July 16, 2026",
        "use": "Real-player day-one and day-seven power ranges; used as soft benchmarks only.",
    },
    {
        "name": "AllClash — current five- and seven-march pairings",
        "url": "https://www.allclash.com/best-commander-pairings-defense-rally-open-field-canyon-barbarians/",
        "date": "Updated May 9, 2026",
        "use": "Primary pairing consensus and roster construction.",
    },
    {
        "name": "AllClash — commander tier list",
        "url": "https://www.allclash.com/best-commanders-tier-list-in-rise-of-kingdoms-with-talents/",
        "date": "Updated July 24, 2026",
        "use": "Newest commander placement, including Vercingetorix and Elizabeth I.",
    },
    {
        "name": "Rise of Kingdoms Guides — Alp Arslan",
        "url": "https://riseofkingdomsguides.com/alp-arslan-talent-tree-build-and-guide/",
        "date": "July 1, 2026",
        "use": "Pierce/debuff mechanics and current deputies.",
    },
    {
        "name": "Rise of Kingdoms Guides — Qin Shi Huang",
        "url": "https://riseofkingdomsguides.com/qin-shi-huang-talent-tree-build-guide-rise-of-kingdoms/",
        "date": "January 2, 2026",
        "use": "QSH mechanics, role, and pairings.",
    },
    {
        "name": "Rise of Kingdoms Guides — Crystal Tech changes",
        "url": "https://riseofkingdomsguides.com/season-of-conquest-crystal-tech-changes-in-rise-of-kingdoms/",
        "date": "January 2, 2026",
        "use": "Current Crystal Tech changes and season economy.",
    },
    {
        "name": "RoK subreddit — roster construction discussion",
        "url": "https://www.reddit.com/r/RiseofKingdoms/comments/1ts06sj/how_many_troop_type_marches/",
        "date": "May 30, 2026",
        "use": "Active-player discussion of balanced rosters, specialization, march support, and Crystal Tech.",
    },
    {
        "name": "RoK subreddit — current KvK1 recommendations",
        "url": "https://www.reddit.com/r/RiseofKingdoms/comments/1ru92ge/for_everyone_who_wants_good_kvk_1_march_recs/",
        "date": "March 15, 2026",
        "use": "Early-season, spend-tiered march recommendations.",
    },
    {
        "name": "RoK subreddit — current KvK2 discussion",
        "url": "https://www.reddit.com/r/RiseofKingdoms/comments/1uwz4qt/best_kvk_2_marches_for_f2p_one_inf_and_one_cav/",
        "date": "July 15, 2026",
        "use": "Concentration-versus-expansion tradeoff for low spenders.",
    },
]


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(JSON_SORT_KEYS=False)
    if test_config:
        app.config.update(test_config)

    @app.get("/")
    def index():
        return render_template(
            "index.html",
            marches=META_MARCHES,
            stages=STAGES,
            roadmap=ROADMAP,
            daily_loop=DAILY_LOOP,
            sources=SOURCES,
            researched_on=date(2026, 8, 8),
        )

    @app.get("/api/meta")
    def meta_api():
        return jsonify(
            {
                "as_of": "2026-08-08",
                "scope": "Open-field account progression with Season of Conquest emphasis",
                "marches": META_MARCHES,
                "stages": STAGES,
                "roadmap": ROADMAP,
                "daily_loop": DAILY_LOOP,
                "sources": SOURCES,
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


app = create_app()
