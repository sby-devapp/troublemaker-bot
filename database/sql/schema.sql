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
    age INTEGER DEFAULT 99,

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
    
    FOREIGN KEY (group_id) REFERENCES chats(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (group_id, user_id)
);

-- Proposal messages: gender can be 'M', 'F', or NULL (for neutral/universal)
CREATE TABLE IF NOT EXISTS proposal_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT CHECK( gender IS NULL OR gender IN ('M', 'F', NULL) ),
    content TEXT NOT NULL
);

-- Gossip messages: gender can be 'M', 'F', or NULL (for neutral/universal)
CREATE TABLE IF NOT EXISTS gossip_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT CHECK( gender IS NULL OR gender IN ('M', 'F', NULL) ),
    content TEXT NOT NULL
);



