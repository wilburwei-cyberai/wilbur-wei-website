"""Research projects: titles and fiscal year supplied by the site owner."""
from records import bi

RESEARCH_PROJECTS = [
    {
        'slug': 'nstc-fy115-llm-red-team',
        'fiscal_year': 'FY115',
        'year': 2026,
        'title': bi(
            '基於 LLM 驅動的紅隊代理攻防演練與場域模擬實戰平台',
            'LLM-Driven Red Team Agent Platform for Adversarial Drills and Real-World Scenario Simulation',
        ),
        'agency': bi('國家科學及技術委員會（國科會）', 'National Science and Technology Council (NSTC)'),
    },
]
