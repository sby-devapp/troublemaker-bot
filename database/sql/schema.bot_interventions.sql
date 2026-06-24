-- Bot Interventions: For regular conversation participation
DROP TABLE IF EXISTS bot_interventions;

CREATE TABLE IF NOT EXISTS bot_interventions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,  -- 'reaction', 'observation', 'tease'
    content TEXT NOT NULL,
    used INTEGER DEFAULT 0,
    active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_bot_interventions_type ON bot_interventions(type);
CREATE INDEX IF NOT EXISTS idx_bot_interventions_active ON bot_interventions(active);
