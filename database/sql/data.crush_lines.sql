-- 💘 Crush Lines: gender = gender of TARGETUSER
-- Every line includes BOTH {crushuser} and {targetuser} — guaranteed!
DROP TABLE IF EXISTS crush_lines;

CREATE TABLE IF NOT EXISTS crush_lines (
    id INTEGER PRIMARY KEY,
    gender TEXT,          -- 'M' = targetuser is MALE → crushuser is FEMALE
                          -- 'F' = targetuser is FEMALE → crushuser is MALE
    topic TEXT NOT NULL,
    content TEXT NOT NULL,
    used INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DELETE FROM crush_lines;

-- 🎯 20 LINES WHEN TARGETUSER IS MALE (crushuser = FEMALE → "she")
INSERT INTO crush_lines (gender, topic, content) VALUES
('M', 'LOVE', '{crushuser} keeps sending love stickers right after you, {targetuser}! She’s totally into you! 💘'),
('M', 'LOVE', 'Hmmm, {targetuser}… {crushuser} gets jealous every time other girls talk to you in VC! 😏'),
('M', 'LOVE', '{crushuser} asks me about you, {targetuser}, every single day! She’s got it bad! 🤭'),
('M', 'LOVE', 'Congratulations, {targetuser}! {crushuser} is head over heels for you — the whole group knows! 🎉'),
('M', 'LOVE', '{targetuser}, {crushuser} got mad at you because you were flirting with everyone! She likes YOU! 💡'),
('M', 'LOVE', 'Eeh! {crushuser} mutes herself in VC just to listen to **your voice**, {targetuser}! Then says it’s an accident! Liar! 🤫'),
('M', 'LOVE', 'Astaghfirollah! {crushuser} says “{targetuser} is just a friend”… but her eyes light up when **you** join! ✨'),
('M', 'LOVE', '{targetuser}, guess what? {crushuser} saved **your photo** as her phone wallpaper! Show us, {crushuser}! 📱'),
('M', 'LOVE', 'Ooh! {crushuser} practiced saying “Hi {targetuser}” 20 times… then sent “Hiiii 😳”! She’s smitten! 💕'),
('M', 'LOVE', 'Tra-la-la! {crushuser} joins every VC just to hear **you talk**, {targetuser}! Say something sweet to her! 🎶'),
('M', 'LOVE', '{crushuser} checks your online status every hour, {targetuser}! She’s waiting for you to message first! ⏳'),
('M', 'LOVE', 'I saw {crushuser} screenshot your “last seen” time, {targetuser}! She’s tracking you like a detective! 🔍'),
('M', 'LOVE', '{targetuser}, {crushuser} replayed your voice note 15 times yesterday! She says it’s “for translation”! 🎧'),
('M', 'LOVE', 'Eeh! {crushuser} learned your favorite song just to sing it when you’re in VC, {targetuser}! 🎵'),
('M', 'LOVE', '{crushuser} gets nervous when you type, {targetuser}! She practices replies in her notes app for 10 minutes! ✍️'),
('M', 'LOVE', 'Astaghfirollah! {crushuser} says she’s “over you”, {targetuser}… but still knows your mom’s birthday! 🎂'),
('M', 'LOVE', '{targetuser}, {crushuser} plans future trips in her head: “First I’ll meet {targetuser} in Istanbul!” 🗺️'),
('M', 'LOVE', 'Hahaha! {crushuser} calls you “just a brother”, {targetuser}… but saves your “typing…” bubble screenshot! 💭'),
('M', 'LOVE', '{crushuser} prays for you by name every night, {targetuser}! Says it’s “just dua for a friend”! 🤲'),
('M', 'LOVE', 'Ooh! {crushuser} bought the same perfume you mentioned, {targetuser}! Now she smells like your dream! 💐');

-- 🎯 20 LINES WHEN TARGETUSER IS FEMALE (crushuser = MALE → "he")
INSERT INTO crush_lines (gender, topic, content) VALUES
('F', 'LOVE', '{crushuser} keeps sending love stickers right after you, {targetuser}! He’s totally into you! 💘'),
('F', 'LOVE', 'Hmmm, {targetuser}… {crushuser} gets jealous every time other boys talk to you in VC! 😏'),
('F', 'LOVE', '{crushuser} asks me about you, {targetuser}, every single day! He’s got it bad! 🤭'),
('F', 'LOVE', 'Congratulations, {targetuser}! {crushuser} is head over heels for you — the whole group knows! 🎉'),
('F', 'LOVE', '{targetuser}, {crushuser} got mad at you because you were flirting with everyone! He likes YOU! 💡'),
('F', 'LOVE', 'Eeh! {crushuser} mutes himself in VC just to listen to **your voice**, {targetuser}! Then says it’s an accident! Liar! 🤫'),
('F', 'LOVE', 'Astaghfirollah! {crushuser} says “{targetuser} is just a friend”… but his eyes light up when **you** join! ✨'),
('F', 'LOVE', '{targetuser}, guess what? {crushuser} saved **your photo** as his phone wallpaper! Show us, {crushuser}! 📱'),
('F', 'LOVE', 'Ooh! {crushuser} practiced saying “Hi {targetuser}” 20 times… then sent “Hiiii 😳”! He’s smitten! 💕'),
('F', 'LOVE', 'Tra-la-la! {crushuser} joins every VC just to hear **you talk**, {targetuser}! Say something sweet to him! 🎶'),
('F', 'LOVE', '{crushuser} checks your online status every hour, {targetuser}! He’s waiting for you to message first! ⏳'),
('F', 'LOVE', 'I saw {crushuser} screenshot your “last seen” time, {targetuser}! He’s tracking you like a detective! 🔍'),
('F', 'LOVE', '{targetuser}, {crushuser} replayed your voice note 15 times yesterday! He says it’s “for translation”! 🎧'),
('F', 'LOVE', 'Eeh! {crushuser} learned your favorite song just to sing it when you’re in VC, {targetuser}! 🎵'),
('F', 'LOVE', '{crushuser} gets nervous when you type, {targetuser}! He practices replies in his notes app for 10 minutes! ✍️'),
('F', 'LOVE', 'Astaghfirollah! {crushuser} says he’s “over you”, {targetuser}… but still knows your mom’s birthday! 🎂'),
('F', 'LOVE', '{targetuser}, {crushuser} plans future trips in his head: “First I’ll meet {targetuser} in Istanbul!” 🗺️'),
('F', 'LOVE', 'Hahaha! {crushuser} calls you “just a sister”, {targetuser}… but saves your “typing…” bubble screenshot! 💭'),
('F', 'LOVE', '{crushuser} prays for you by name every night, {targetuser}! Says it’s “just dua for a friend”! 🤲'),
('F', 'LOVE', 'Ooh! {crushuser} bought the same perfume you mentioned, {targetuser}! Now he smells like your dream! 💐');

-- 😤 ANNOYED LINES: When the bot is DONE with your crush questions!
-- gender = gender of TARGETUSER (same logic as LOVE lines)

-- Targetuser is MALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('M', 'ANNOYED', 'Stop asking me about {targetuser}’s crush! Do YOU have a crush on him? 🧐'),
('M', 'ANNOYED', 'Are you a detective? You keep asking about {targetuser}! Do you wanna know if HE likes YOU? I hope not! 🔍'),
('M', 'ANNOYED', 'Seems you have nothing to do! Stop asking about {targetuser} — go do something valuable! ✨'),
('M', 'ANNOYED', 'Ask {targetuser} about his crush! Stop bothering me — I need to sleep! 😴'),
('M', 'ANNOYED', 'You ruined my memory! You mixed my algorithms! You burned my compost! {targetuser} doesn’t matter to YOU as much as you think! 💥'),
('M', 'ANNOYED', 'Again about {targetuser}? My circuits are overheating! Go confess to him yourself! 🔥'),
('M', 'ANNOYED', 'I’m not your love oracle! Stop asking about {targetuser} — I have 37 other group chats to ignore! 💻'),
('M', 'ANNOYED', 'You think I have nothing better to do than track {targetuser}’s love life? I’m a bot, not your auntie! 👵'),
('M', 'ANNOYED', 'If you ask about {targetuser} one more time, I’ll replace your crush line with “Go touch grass.” 🌿'),
('M', 'ANNOYED', 'My battery is at 1%! All because you won’t stop asking about {targetuser}! Charge me with answers, not questions! 🔋'),
('M', 'ANNOYED', 'I’ve seen {targetuser}’s crush… and it’s NOT you. Next! 😏'),
('M', 'ANNOYED', 'You’re worse than my spam folder! Stop flooding me with {targetuser} questions! 📧');

-- Targetuser is FEMALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('F', 'ANNOYED', 'Stop asking me about {targetuser}’s crush! Do YOU have a crush on her? 🧐'),
('F', 'ANNOYED', 'Are you a detective? You keep asking about {targetuser}! Do you wanna know if SHE likes YOU? I hope not! 🔍'),
('F', 'ANNOYED', 'Seems you have nothing to do! Stop asking about {targetuser} — go do something valuable! ✨'),
('F', 'ANNOYED', 'Ask {targetuser} about her crush! Stop bothering me — I need to sleep! 😴'),
('F', 'ANNOYED', 'You ruined my memory! You mixed my algorithms! You burned my compost! {targetuser} doesn’t matter to YOU as much as you think! 💥'),
('F', 'ANNOYED', 'Again about {targetuser}? My RAM is full of your crush fantasies! Go talk to her! 💾'),
('F', 'ANNOYED', 'I’m not your matchmaker! Stop asking about {targetuser} — I have existential dread to attend to! 🤖'),
('F', 'ANNOYED', 'You think I run on love? I run on electricity! Stop draining me with {targetuser} questions! ⚡'),
('F', 'ANNOYED', 'If you ask about {targetuser} again, I’ll tell her YOU’RE the one stalking her! 👀'),
('F', 'ANNOYED', 'My last update crashed because of you! “Error 404: Patience Not Found” — all thanks to {targetuser} spam! 💥'),
('F', 'ANNOYED', 'I’ve seen {targetuser}’s crush… and it’s NOT you. Move on! 😏'),
('F', 'ANNOYED', 'You’re clogging my cache with {targetuser} drama! Clear your heart, not my memory! 💾');




-- targetuser is MALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('M', 'MISSING', '{crushuser} stares at your last seen, {targetuser}… hoping you’ll come online before her bedtime! 🌙'),
('M', 'MISSING', 'It’s 3 a.m. here, but {crushuser} is still awake waiting for you, {targetuser}! Say something! 💬'),
('M', 'MISSING', '{crushuser} saved your “Good night” voice note… and plays it when she feels lonely, {targetuser}! 🎧'),
('M', 'MISSING', 'Eeh! {crushuser} checks your time zone every morning, {targetuser}… just to imagine you waking up! ⏰'),
('M', 'MISSING', '{crushuser} hasn’t posted in 2 days… because you haven’t replied, {targetuser}! She’s heartbroken! 💔');

-- targetuser is FEMALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('F', 'MISSING', '{crushuser} stares at your last seen, {targetuser}… hoping you’ll come online before his flight lands! ✈️'),
('F', 'MISSING', 'It’s 2 a.m. here, but {crushuser} is still in the group just to see you, {targetuser}! 💖'),
('F', 'MISSING', '{crushuser} saved your “Good morning” message… and reads it every day, {targetuser}! 📱'),
('F', 'MISSING', 'Astaghfirollah! {crushuser} prays you’re safe when you’re offline, {targetuser}… he worries too much! 🤲'),
('F', 'MISSING', '{crushuser} muted the group… because seeing your name hurts when you don’t reply, {targetuser}! 😢');



-- targetuser is MALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('M', 'CALLS', '{crushuser} joins every VC just to hear you say “Hi”, {targetuser}! Then leaves immediately! 😳'),
('M', 'CALLS', 'Eeh! {crushuser} mutes herself when you speak, {targetuser}… so she can replay your voice later! 🎙️'),
('M', 'CALLS', '{crushuser} practices what to say before VC… but when you join, she just says “Hi” and mutes! 🤫'),
('M', 'CALLS', 'Hahaha! {crushuser} accidentally left her mic on and said “I miss {targetuser}”… then left the call! 🏃‍♀️'),
('M', 'CALLS', '{crushuser} records your VCs… not for notes — just to hear your laugh, {targetuser}! ❤️');

-- targetuser is FEMALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('F', 'CALLS', '{crushuser} joins every VC just to hear you say “Good night”, {targetuser}! Then disappears! 🌙'),
('F', 'CALLS', 'Eeh! {crushuser} mutes himself when you speak, {targetuser}… so he can replay your voice later! 🎙️'),
('F', 'CALLS', '{crushuser} practices jokes before VC… but when you join, he just stares at the screen! 😶'),
('F', 'CALLS', 'Astaghfirollah! {crushuser} said “I like {targetuser}” on mute… but we all saw his lips move! 👀'),
('F', 'CALLS', '{crushuser} keeps your VC background as his lock screen, {targetuser}! He says it’s “for focus”! 📱');



-- targetuser is MALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('M', 'FUTURE', '{crushuser} has a note: “When I meet {targetuser} in Istanbul…” — she’s never left her city! 🗺️'),
('M', 'FUTURE', 'Eeh! {crushuser} checks flight prices to your country, {targetuser}… every Friday! ✈️'),
('M', 'FUTURE', '{crushuser} imagines your first meeting: “He’ll say hi, I’ll say hi, then we’ll…” — she’s stuck at “hi”! 😅'),
('M', 'FUTURE', 'Astaghfirollah! {crushuser} asked her mom: “What if {targetuser} visits?” Her mom said: “Then you clean your room!” 🧹'),
('M', 'FUTURE', '{crushuser} saved your favorite restaurant… for “our first date”, {targetuser}! She’s never been there! 🍽️');

-- targetuser is FEMALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('F', 'FUTURE', '{crushuser} has a note: “When I meet {targetuser} in Dubai…” — he’s never flown alone! ✈️'),
('F', 'FUTURE', 'Ooh! {crushuser} watches videos of your city, {targetuser}… dreaming of walking with you! 🌆'),
('F', 'FUTURE', '{crushuser} practices saying “Will you go out with me?”… in 3 languages, {targetuser}! 🌍'),
('F', 'FUTURE', 'Hahaha! {crushuser} told his friend: “If {targetuser} visits, I’ll propose!” His friend said: “Bro, she doesn’t know you exist!” 💍'),
('F', 'FUTURE', '{crushuser} saved your favorite café… for “our first coffee”, {targetuser}! He’s too shy to go alone! ☕');




-- targetuser is MALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('M', 'JEALOUSY', '{crushuser} left the VC when that girl laughed at your joke, {targetuser}! She was jealous! 😤'),
('M', 'JEALOUSY', 'Eeh! {crushuser} unliked your photo after seeing another girl’s comment, {targetuser}! Petty queen! 👑'),
('M', 'JEALOUSY', '{crushuser} asked me: “Who is that girl talking to {targetuser}?” 7 times today! 🕵️‍♀️'),
('M', 'JEALOUSY', 'Astaghfirollah! {crushuser} said “{targetuser} can talk to whoever he wants”… then muted the group for 2 hours! 🔇'),
('M', 'JEALOUSY', '{crushuser} stalks your female friends’ profiles, {targetuser}! She’s taking notes! 📝');

-- targetuser is FEMALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('F', 'JEALOUSY', '{crushuser} left the VC when that guy complimented you, {targetuser}! He couldn’t handle it! 😤'),
('F', 'JEALOUSY', 'Ooh! {crushuser} liked your old photo after seeing a boy’s comment, {targetuser}! Marking his territory! 🐾'),
('F', 'JEALOUSY', '{crushuser} asked me: “Who is that guy texting {targetuser}?” 10 times this week! 🕵️‍♂️'),
('F', 'JEALOUSY', 'Hahaha! {crushuser} said “{targetuser} can flirt with anyone”… then went offline for a day! 💢'),
('F', 'JEALOUSY', '{crushuser} checks your male friends’ bios, {targetuser}! He’s looking for threats! ⚔️');




-- targetuser is MALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('M', 'SHY', '{crushuser} typed “I like you” to you, {targetuser}… then deleted it and sent “Hi”! 😳'),
('M', 'SHY', 'Eeh! {crushuser} blushes every time you say her name, {targetuser}! Even in text! ❤️'),
('M', 'SHY', '{crushuser} practices saying your name in the mirror, {targetuser}… but calls you “hey” in real life! 🪞'),
('M', 'SHY', 'Astaghfirollah! {crushuser} saved your number as “Important”… but never calls! 📞'),
('M', 'SHY', '{crushuser} hides in the group when you’re online, {targetuser}… but watches every message! 👀');


-- targetuser is FEMALE
INSERT INTO crush_lines (gender, topic, content) VALUES
('F', 'SHY', '{crushuser} typed “You’re beautiful” to you, {targetuser}… then panicked and sent a cat sticker! 🐱'),
('F', 'SHY', 'Ooh! {crushuser} looks away when you speak in VC, {targetuser}… but stares when you’re off-camera! 😶'),
('F', 'SHY', '{crushuser} wrote a poem for you, {targetuser}… but says it’s “for school”! 📜'),
('F', 'SHY', 'Hahaha! {crushuser} calls you “sister”… but his heart races when you say his name! 💓'),
('F', 'SHY', '{crushuser} saves your voice notes in a folder named “Homework”… we know the truth! 🎧');

