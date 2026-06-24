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

-- Initial data for silence breakers
DELETE FROM silence_breakers;

-- GENERAL silence messages (no user mention)
INSERT INTO silence_breakers (type, content) VALUES
('general', 'Hmm! This group is silent... 🤫'),
('general', 'Is this group dead? 💀'),
('general', 'Ooh guys, where are you? 👻'),
('general', '*cricket sounds* 🦗'),
('general', 'Hello? Anyone there? 📢'),
('general', 'Did everyone fall asleep? 😴'),
('general', 'The silence is deafening! 🔇'),
('general', 'Earth to group members... 🌍'),
('general', 'Is anyone alive? Send help! 🆘'),
('general', 'This group needs CPR! 💔'),
('general', 'Wake up, people! ⏰'),
('general', 'Did I miss the memo about silence day? 🤐'),
('general', 'Someone say SOMETHING! 🗣️'),
('general', 'The ghost town vibes are real 👻'),
('general', 'I feel like I''m talking to myself... oh wait 🤖');

-- MENTION messages (with {user} placeholder)
INSERT INTO silence_breakers (type, content) VALUES
('mention', 'Ooh {user}, long time no see! 👋'),
('mention', 'Hey {user}, where have you been? 🤔'),
('mention', '{user}, come join the conversation! 💬'),
('mention', 'Missing you in the chat, {user}! 😢'),
('mention', '{user}, say something! The group is too quiet 🗨️'),
('mention', 'Wake up {user}! Time to chat! ⏰'),
('mention', '{user}, we need your wisdom here! 🧠'),
('mention', 'Calling {user}! Emergency group revival needed! 🚨'),
('mention', '{user}, don''t be a stranger! 🤗'),
('mention', 'Where art thou, {user}? 🎭'),
('mention', '{user}, your presence is requested! 📬'),
('mention', 'Yo {user}! Get in here! 📣'),
('mention', '{user}, the group misses you! 💕'),
('mention', 'Summoning {user} to break the silence! 🔮'),
('mention', '{user}, save us from this awkward silence! 🦸');
