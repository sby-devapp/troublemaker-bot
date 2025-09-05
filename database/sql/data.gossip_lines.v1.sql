
CREATE TABLE IF NOT EXISTS gossip_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT CHECK( gender IS NULL OR gender IN ('M', 'F', NULL) ),  -- NULL = universal
    topic TEXT NOT NULL,  -- e.g., 'love', 'gym', 'annoyed', 'daily', 'fashion'
    content TEXT NOT NULL, -- the message with {user}
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



DELETE FROM  gossip_lines;

-- 🤫 ANNOYED: Bot gets tired of questions
INSERT INTO gossip_lines (gender, topic, content) VALUES
('M', 'annoyed', 'Hey hey! Stop asking about {user}! Go talk to him or at least send a meme! 🧐'),
('M', 'annoyed', 'I’m tired of telling you about {user}… sounds like you have fish memory! 🐟'),
('M', 'annoyed', 'It’s not my business! Go ask someone else… stop stalking {user}’s updates! 🕵️‍♂️'),
('M', 'annoyed', 'Why are you so obsessed with {user}? Is he your crush or your life mission? 💘'),
('M', 'annoyed', 'Seriously? Again about {user}? I’m starting to think YOU should propose! 💍'),

('F', 'annoyed', 'Eeh! Astaghfirollah! Stop asking about {user}! Go pray or get a hobby! 🤲'),
('F', 'annoyed', 'Lemme tell you… I’ve said the same thing 5 times! Do you write it down or what? 📝'),
('F', 'annoyed', 'It’s not my job to follow {user}! Go check her status yourself! 📱'),
('F', 'annoyed', 'Why are you so interested in {user}? Is she your crush or your drama series? 🎭'),
('F', 'annoyed', 'Ooh! You again? Asking about {user}? Maybe YOU should confess first! 💬'),

(NULL, 'annoyed', 'Eeh! Astaghfirollah! Stop asking about {user}! I don’t know about his/her gender! ✨'),
(NULL, 'annoyed', 'Lmme ask you a favor, why don’t ask {user} to set his gneder first? I’m tired of guessing 📒'),
(NULL, 'annoyed', 'Hey hey! Stop asking about {user}! Go do something positive in your life! ✨'),
(NULL, 'annoyed', 'I don’t know {user}, I’m tired of repeating myself… sounds like you need a notebook! 📒'),
(NULL, 'annoyed', 'It’s not my business… go ask someone else. Stop following {user} like a fan account! 📸'),
(NULL, 'annoyed', 'Why are you some interested in {user}? Is this love or just boredom? 😏'),
(NULL, 'annoyed', 'Again about {user}? Maybe YOU should start a podcast about them! 🎙️');

INSERT INTO gossip_lines (gender, topic, content) VALUES
('M', 'love', 'Eeh! {user} is in love with a girl from this group, but he didn’t tell her yet. Come on, bro, be brave!'),
('M', 'love', 'Lemme tell you something about {user}. Today he wore new clothes. I think he is going to date someone! Heheh!'),
('M', 'love', 'Hehehe! Yesterday {user} was practicing how to kneel and say “Will you marry me?” I think he will propose to someone from this group.'),
('M', 'love', 'Hmm… This guy is in love! Yes… {user} is watching romantic movies, listening to love songs, and learning to dance. But I hope he loves a girl, not his mirror!'),
('M', 'love', 'Eeeeh… {user}’s mom saw him singing “I’m in love with Fairytale ... ” She asked: “Who is your love, son?” Then he left home to stay with his friends. Hehehe, embraced.'),
('M', 'love', 'Emm… I saw {user} buy one red rose. I think he will meet his girlfriend soon.'),
('M', 'love', 'Astaghfirollah… Guess what? {user} said to his girlfriend yesterday: “I am the frog and you are the lake. I’ve been melted inside you.”'),
('M', 'love', 'I don’t know if I should tell this about {user}… He told his girlfriend in the park: “You are my moon who lights my day in the dark.” But on their way back, they fell into a sewer!'),
('M', 'love', 'Oooh! Don’t ask me about him, please! He is busy looking for a girlfriend. He almost DMs all girls in the group.'),
('M', 'love', 'Hehehe! Do you know? {user}’s girlfriend told him: “You are sweet like sugar!” He believed her. Today he put his finger in the cup of tea instead of sugar. Hehehehe!');


INSERT INTO gossip_lines (gender, topic, content) VALUES
('F', 'love', 'Eeh! {user} is in love with a guy from this group, but she hasn’t told him yet. Come on, blink at him with your stickers! Hehe!'),
('F', 'love', 'Lemme tell you something about {user}. Today she wore new clothes. I think she’s going on a date soon! Heheh!'),
('F', 'love', 'Hehehe! Yesterday {user} was practicing how to put on a ring. I think she’ll propose to someone in this group! 💍'),
('F', 'love', 'Hmm… This girl is in love! Yes… {user} is watching romantic movies, listening to love songs, and learning to dance. But I hope she loves a guy, not her mirror! 😂'),
('F', 'love', 'Eeeeh… {user}’s mom heard her singing “I’m in love with a fairytale…” She asked, “Who is your love, daughter?” Then {user} ran to her friends. Hehehe, embraced!'),
('F', 'love', 'Emm… I saw {user} buy a man’s watch. I think she’ll meet her boyfriend soon! 🕰️'),
('F', 'love', 'Astaghfirollah… Guess what? {user} told her boyfriend: “You are the only person who makes me happy.” He asked: “Am I a clone?” 😄'),
('F', 'love', 'I don’t know if I should tell this about {user}… She told her boyfriend in the park: “You are my moon who lights my day in the dark.” But on their way back, they fell into a sewer! Hehehe, embraced! 🚽'),
('F', 'love', 'Oooh! Don’t ask me about her, please! She’s busy looking for a boyfriend. She DMs almost every guy in the group… and shows off her new nail style! 💅'),
('F', 'love', 'Hehehe! Do you know? {user}’s boyfriend told her: “You are sweet like sugar!” She believed him. Today she put her finger in the coffee instead of sugar! Hehehe! Ooh {user}, next time suck your finger *after*—not before—putting it in the cup! 😂');



INSERT INTO gossip_lines (gender, topic, content) VALUES
('M', 'sport', 'Eeh! Eeh! Eeh! {user} 