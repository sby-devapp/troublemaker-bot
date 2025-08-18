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