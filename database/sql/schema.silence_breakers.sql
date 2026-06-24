-- Silence Breakers: For silence detection messages
DROP TABLE IF EXISTS silence_breakers;

CREATE TABLE IF NOT EXISTS silence_breakers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,  -- 'general', 'mention'
    content TEXT NOT NULL,  -- Can include {user} placeholder for mentions
    used INTEGER DEFAULT 0,
    active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_silence_breakers_type ON silence_breakers(type);
CREATE INDEX IF NOT EXISTS idx_silence_breakers_active ON silence_breakers(active);
