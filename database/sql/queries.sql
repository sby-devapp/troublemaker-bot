SELECT gu.group_id, u.*
            FROM users u
            JOIN group_users gu ON u.id = gu.user_id
            WHERE gu.group_id = -1001


SELECT * FROM proposal_lines
        WHERE gender = 'F'
        ORDER BY RANDOM()
        LIMIT 1


SELECT * FROM proposal_lines
                WHERE gender IS NULL
                ORDER BY RANDOM()
                LIMIT 1


-- Step 1: Rename the old table
ALTER TABLE group_users RENAME TO group_users_old;

-- Step 2: Create the new table with updated schema
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

-- Step 3: Copy data from old to new
INSERT OR IGNORE INTO group_users (group_id, user_id) 
SELECT 
    group_id, 
    user_id
FROM group_users_old;

-- Step 4: Drop the old table
DROP TABLE IF EXISTS group_users_old;



SELECT u.*
    FROM users u
JOIN group_users gu ON u.id = gu.user_id
    WHERE gu.group_id = -1001980851583 
    AND u.id != 618768960  
    AND gu.is_participant = 'y'
    AND u.gender = NULL;



SELECT u.*, g.groupname, gu.is_participant
    FROM users u
INNER JOIN group_users gu ON u.id=gu.user_id
INNER JOIN groups g ON g.id = gu.group_id
    WHERE u.id = 6933133813;
    
select * from users;

DELETE FROM users where id = 6933133813;
DELETE FROM group_users where user_id = 6933133813;


ALTER TAbLE gossip_lines ADD COLUMN used INTEGER  DEFAULT 0;

SELECT * 
FROM gossip_lines 
order by DESC used;