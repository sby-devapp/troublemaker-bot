-- ===========================
-- 🔹 GENDER = 'M' (20 lines)
-- For when the proposer is male — funny, future-focused, suggestive
-- ===========================

INSERT INTO proposal_lines (gender, content) VALUES
('M', '🚀 {user1} will propose to {user2} within 24 hours. Prepare the virtual cake! 🎂'),
('M', '📢 {user1}, drop to one knee NOW for {user2}! The bot commands you! ⏳'),
('M', '🔮 My future-vision glasses say: {user1} + {user2} = married by next full moon. 🌕💍'),
('M', '{user2}, be ready — {user1} is about to slide into your DMs with a ring! 💍'),
('M', '{user1}, stop waiting! The stars say: “Propose to {user2} before midnight!” ⏰✨'),
('M', '🚨 Alert! {user1} has been caught practicing “Will you marry me?” in the mirror. Target: {user2}. 🪞'),
('M', '{user1}, if you don’t propose today, {user2} might be stolen by a bot. Me. 😈'),
('M', '📢 PSA: {user1}, your love for {user2} is 87% confirmed. Time to act! 💘'),
('M', '{user1}, the group chat law says: “Thou shalt propose within 7 days.” You’re late. ⚖️'),
('M', '📅 {user1}, mark your calendar: {user2} expects a proposal this weekend. 📆'),
('M', '{user1}, stop overthinking! Just say: “{user2}, be mine!” (We all know you want to.) 💬'),
('M', '🛸 Alien prophecy: “{user1} shall unite with {user2} under the emoji moon.” 🌙👽'),
('M', '{user1}, the bot orders you: Propose to {user2} before someone else does! ⚔️'),
('M', '💍 {user2}, check your pockets — {user1} might’ve slipped a ring in there. 👜'),
('M', '{user1}, the Wi-Fi signal between you and {user2} is 100% love. Act on it! 📶❤️'),
('M', '🎭 In tonight’s episode: “The One Who Finally Confessed” — starring {user1} and {user2}! 🎬'),
('M', '{user1}, go get {user2} a flower… or at least a pizza. That’s basically a proposal. 🍕'),
('M', '📢 Breaking News: {user1} is 0.2 seconds away from proposing to {user2}. 💥'),
('M', '{user1}, if you don’t do it today, I’ll announce your crush in the group. 😏'),
('M', '🌠 Future prediction: {user1} + {user2} = married in this chat by Friday. You’re welcome. 🕶️');


-- ===========================
-- 🔹 GENDER = 'F' (20 lines)
-- For when the proposer is female — playful, romantic, future-suggestive
-- ===========================

INSERT INTO proposal_lines (gender, content) VALUES
('F', '📣 Hey {user2}! {user1} is 0.2 seconds away from proposing. Brace yourself! 💘'),
('F', '{user1}, the universe commands you: Slide into {user2}’s DMs with a marriage offer! 🌌📩'),
('F', '📅 Mark your calendar: {user1} will propose to {user2} this weekend. Bring confetti! 🎉'),
('F', '{user2}, don’t be surprised if {user1} shows up with a ring and a bad joke. 💍😂'),
('F', '⚠️ Warning: {user1} has been practicing “Will you marry me?” in the mirror. Target: {user2}. 🪞'),
('F', '{user1}, stop hesitating! {user2} is waiting (but pretending not to). 😏'),
('F', '📢 {user1}, your romantic energy is peaking! Time to propose to {user2}! 🌪️'),
('F', '💍 {user2}, prepare your heart — {user1} is coming for it with full romantic artillery. 💣❤️'),
('F', '{user1}, if you don’t propose today, someone else will steal {user2}. Act fast! ⚡'),
('F', '📜 The ancient scroll says: “{user1} shall claim {user2} before the next voice note.” 📜'),
('F', '{user1}, go tell {user2}: “You’re my favorite notification.” Then propose. 💬'),
('F', '🚀 Love alert! {user1} has entered {user2}’s DMs with full romantic intentions! 🚨'),
('F', '{user1}, the stars say: “Propose before the next meme drops.” They’re serious. ✨'),
('F', '🎭 {user1}, this group chat is your stage. {user2} is waiting for your move. 🎭'),
('F', '{user1}, stop overthinking! {user2} already said “yes” in their dreams. 😴❤️'),
('F', '📡 {user1}, your typing speed slows down near {user2}. We see you. Now propose! ⌨️'),
('F', '{user1}, go buy a ring… or at least a sticker that says “I do.” It counts. 🤳'),
('F', '📣 PSA: {user1}, if you don’t propose to {user2} today, the bot will do it for you. 😈'),
('F', '{user1}, the future says: “You + {user2} = eternal snack sharing.” 💞'),
('F', '🌠 {user1}, the moon, the stars, and this bot agree: Propose to {user2} now. 🌙');


-- ===========================
-- 🔹 GENDER = NULL (10 lines)
-- For unknown gender — funny rejections, absurd bureaucracy, chaos
-- ===========================

INSERT INTO proposal_lines (gender, content) VALUES
(NULL, '❓ {user1}, I don’t know if you’re a prince or a princess… go ask your mom! 👵'),
(NULL, '🚫 Sorry {user1}, marriage requires a gender. You can’t just “vibe” into a wedding. 💫'),
(NULL, '📜 Rule #7: No marriage until you tell me if you’re M or F. Go fill the form in DMs. 📋'),
(NULL, '👴 {user1}, go to your parents and say: “Who am I, and why won’t the bot marry me?”'),
(NULL, '🕌 Visit the mosque and pray: “O Bot, reveal my gender!” Then come back. 🤲🤖'),
(NULL, '🔍 {user1}, your gender is a mystery even to the CIA. Please clarify before proposing. 🕵️‍♂️'),
(NULL, '🤖 Error 404: Gender not found. Please run /setgender to continue. ⚙️'),
(NULL, '🐑 {user1}, consult the village wise goat. He knows your true path. 🐐'),
(NULL, '🛸 Aliens won’t abduct you until you pick M or F. Neither will I allow marriage. 👽'),
(NULL, '🧙 {user1}, only when you say “I am M” or “I am F” will the marriage portal open. 🔮');
