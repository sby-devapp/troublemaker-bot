PRAGMA encoding = "UTF-8";

-- DROP TABLE IF EXISTS users;
-- DROP TABLE IF EXISTS chats;
-- DROP TABLE IF EXISTS groups;
-- DROP TABLE IF EXISTS group_users;
-- DROP TABLE IF EXISTS proposal_lines;
-- ROP TABLE IF EXISTS gossip_lines;
-- DROP TABLE IF EXISTS actions;
-- DROP TABLE IF EXISTS propositions;




CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    last_name TEXT,
    gender TEXT CHECK(gender IS NULL OR gender IN ('M', 'F', NULL)),
    age INTEGER DEFAULT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY,
    username TEXT,
    type TEXT DEFAULT 'private',  -- e.g., 'private', 'group', 'channel'
    last_message_id INTEGER,
    last_message_sent_at TIMESTAMP, -- Time of the last message in the chat

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    groupname TEXT
);


CREATE TABLE IF NOT EXISTS group_users (
    group_id INTEGER,
    user_id INTEGER,
    is_participant TEXT DEFAULT 'y',  -- 'y' = yes, 'n' = no
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (group_id) REFERENCES chats(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE (group_id, user_id)
);

-- Proposal messages: gender can be 'M', 'F', or NULL (for neutral/universal)
CREATE TABLE IF NOT EXISTS proposal_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT CHECK( gender IS NULL OR gender IN ('M', 'F', NULL) ),
    content TEXT NOT NULL,
    used INTEGER DEFAULT 0
);

-- Gossip messages: gender can be 'M', 'F', or NULL (for neutral/universal)
CREATE TABLE IF NOT EXISTS gossip_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT CHECK( gender IS NULL OR gender IN ('M', 'F', NULL) ),
    content TEXT NOT NULL,
    used INTEGER DEFAULT 0
);

CREATE TABLE crush_lines (
    id INTEGER PRIMARY KEY,
    gender TEXT,          -- 'M', 'F', or NULL
    topic TEXT NOT NULL,
    content TEXT NOT NULL,
    used INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


