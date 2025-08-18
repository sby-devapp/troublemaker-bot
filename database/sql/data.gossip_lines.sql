-- 🧔‍♂️ Gossip about a male user (gender = 'M')
INSERT INTO gossip_lines (gender, content) VALUES
('M', '🚽 I heard {user} is using the WC right now… please close the door! We can hear everything! 🚪🙈'),
('M', '🍕 I saw {user} eating pizza… all alone. Share, you greedy snack dragon! 🐉🍕'),
('M', '💘 I heard {user} is meeting his secret lover tonight! Hope it’s not the fridge… again. 🧊💔'),
('M', '👕 I saw {user} wearing new clothes! Going to a party? Or sneaking into someone’s heart? 😉👚'),
('M', '👀 {user} was walking with someone… I *think* he’s dating… but I need more snacks to confirm. 🍿'),
('M', '🌹 I saw {user} buying a red rose… Ehem ehem… Yes yes… same thing you’re thinking… hehhehe! 🌹😏'),
('M', '🎉 I heard {user} is planning a surprise party for someone… hope it’s not for me! I scare easily! 😱🎁'),
('M', '🔐 I saw {user} talking privately… what could he be saying? “I love you”? “Pass the salt”? DRAMA. 📱'),
('M', '✈️ I saw {user} planning a trip with someone… wonder if it’s romantic or just a getaway from bills? 💸'),
('M', '🎮 {user} won 5 games shouting “This win is for you, @crush!” We heard. We judge. 😂');



-- 👩‍🦰 Gossip about a female user (gender = 'F')
INSERT INTO gossip_lines (gender, content) VALUES
('F', '🕌 Eeeh astaghfirollah!!! Look at this one, spying on {user}! Go do istighfar, not TikTok drama! 🤲📿'),
('F', '📿 Don’t ask me about {user} — it’s not my business! Go pray, not stalk! 🙏'),
('F', '💘 {user} has a crush from this group… but I’m sworn to secrecy! (It’s probably @bot.) 🤫🤖'),
('F', '💍 I heard {user} is getting married soon! But the mystery is… who’s the victim? I mean, partner? 😏'),
('F', '💘 I heard {user} is going to confess her feelings soon… hope she doesn’t faint mid-sentence! 💬😳'),
('F', '💘 Rumor: {user} has a secret admirer in this group! Could it be… YOU? 👀❤️'),
('F', '🌍 I heard {user} is traveling abroad! Wish her a safe journey… and Wi-Fi! 📱🧳'),
('F', '📦 I heard {user} is starting a new business… selling love potions? Or just heartbreak? 💔🧪'),
('F', '🔍 I think {user} is hiding something… but my spy glasses are on low battery. 🔋👀'),
('F', '💄 {user} practiced her “casual smile” for 15 minutes before typing. We see you. 😏');


-- 🤫 Universal / Neutral gossip (gender = NULL) – No gender mention

INSERT INTO gossip_lines (gender, content) VALUES
(NULL, '📡 {user}’s heart rate spikes every time someone types… love is in the air. 🫀💘'),
(NULL, '🛸 Aliens have flagged {user} as “high romantic risk.” They’re monitoring. 👽'),
(NULL, '🤫 {user} typed “I love you” and deleted it. We saw. We’re concerned. ❤️'),
(NULL, '🛏️ {user} fell asleep whispering a name… it wasn’t theirs. 😴'),
(NULL, '📱 {user} set a reminder: “Don’t fall for {user}.” Too late. ⏰💔'),
(NULL, '🔍 {user} searched “signs someone likes you” 7 times today. Case closed. 🕵️‍♂️'),
(NULL, '🎭 {user} is 89% likely to fall in love with someone here. The countdown begins. ⏳'),
(NULL, '🎤 {user} recorded a voice note saying “I like you”… and saved it as “Draft 17.” 😅'),
(NULL, '📦 {user} received a package labeled “Future Spouse Material.” We’re curious. 📦'),
(NULL, '👁️ {user} stared at the chat for 12 minutes without typing. Suspicious. 👀');

