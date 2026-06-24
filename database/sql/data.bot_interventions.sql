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

-- Initial data for bot interventions
DELETE FROM bot_interventions;

-- REACTIONS (emojis only)
INSERT INTO bot_interventions (type, content) VALUES
('reaction', '😂'),
('reaction', '👀'),
('reaction', '🍿'),
('reaction', '💀'),
('reaction', '🤔'),
('reaction', '👁️🗨️'),
('reaction', '🌶️'),
('reaction', '🔥'),
('reaction', '💯'),
('reaction', '😱');

-- OBSERVATIONS (general comments about conversation)
INSERT INTO bot_interventions (type, content) VALUES
('observation', 'This group is getting spicy! 🌶️'),
('observation', 'Interesting conversation... 👀'),
('observation', '*grabs popcorn* 🍿'),
('observation', 'Y''all are wild 😂'),
('observation', 'The drama never stops here! 💀'),
('observation', 'Someone''s about to spill tea ☕'),
('observation', 'This escalated quickly 📈'),
('observation', 'I''m living for this energy! ⚡'),
('observation', 'The plot thickens... 🕵️'),
('observation', 'Now THIS is content! 📺');

-- TEASES (playful observations)
INSERT INTO bot_interventions (type, content) VALUES
('tease', 'Someone''s been very quiet today... 👀'),
('tease', 'I see what''s happening here 😏'),
('tease', 'The group detective is watching 🕵️'),
('tease', 'Hmm, suspicious activity detected 🤨'),
('tease', 'Y''all think I''m not paying attention? 😂'),
('tease', 'Interesting choice of words... 🧐'),
('tease', 'Oh, so we''re being mysterious now? 🎭'),
('tease', 'Someone woke up and chose chaos today 😈'),
('tease', 'The audacity! 💅'),
('tease', 'And I took that personally 🤷');
