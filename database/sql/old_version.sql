-- Insert gender-specific messages only (no "neutral")
INSERT INTO propositions(action_id, gender, proposition) VALUES

-- 🧔‍♂️ Male proposing to female
(1, "male", "🎉 Oh snap! {user1} just got down on one knee for {user2}! Someone call the meme squad! 🎉💍"),
(1, "male", "👀 Look at {user1} going full romantic hero for {user2}! Hollywood, take notes! 🎬❤️"),
(1, "male", "🐐 {user1} made the ultimate move — {user2}, you’re not just loved, you’re *claimed*! 😎💘"),
(1, "male", "💥 Classic {user1} energy! Dropped a proposal like it was a surprise beat drop! 🎧❤️"),
(1, "male", "🎯 Ehem Ehem! {user1} chose wisely — {user2} is literally the GOAT! 🐐💍"),
(1, "male", "🏡 I hope you both have a wonderful life together, {user1} and {user2} — starting with a group chat wedding! 📢💍"),
(1, "male", "🥂 Cheers to the happy couple, {user1} and {user2}! May your DMs always be spicy! 🔥😏"),
(1, "male", "🚀 This is the best news ever! {user1} and {user2} are ENGAGED! 🚨💍 Prepare the virtual confetti! 🎉"),
(1, "male", "🌍 I wish {user1} and {user2} all the happiness in the world… and unlimited emoji reactions! 😍❤️"),
(1, "male", "🌱 May your love grow stronger every day — like a plant that never needs watering! 🌱😂"),

-- 👩‍🦰 Female proposing to male
(1, "female", "🔥 BAM! {user1} just popped the question to {user2}! Who said ladies can’t make the first move? 💍💥"),
(1, "female", "🎯 Ladies and gentlemen, {user1} took the leap and asked {user2} to spend forever together! 🥹💞"),
(1, "female", "👑 {user1} didn’t wait — she went full queen and claimed her king, {user2}! 👑❤️"),
(1, "female", "🚀 {user1} just rewrote the rules! Who needs traditions when you’ve got *love and courage*? 💪❤️"),
(1, "female", "💘 I *know* {user1} is in love with {user2} — and guess what? She said ""Marry me!"" instead of sending a voice note! 🎙️❤️"),
(1, "female", "🎊 Big news! {user1} proposed to {user2}! Group chat wedding planning starts NOW! 📢💍"),
(1, "female", "🍿 This love story is better than any drama series — and it’s only episode one! 🎬💞"),
(1, "female", "🎂 Cake for everyone! {user1} and {user2} are ENGAGED! 🎉❤️"),
(1, "female", "💞 You two are meant to be together, {user1} and {user2}! Like socks… but less smelly. 🧦❤️"),
(1, "female", "👰‍♂️🤵‍♀️ I can't wait to see you both walk down the aisle… probably arguing about who ate the last samosa. 😂"),

(1, "NULL", "Tell me your gender, so I can give you a proper proposal!");

-- Gossip: Male context
INSERT INTO propositions(action_id, gender, proposition) VALUES

-- 🧔‍♂️ Gossip about a male user
(2, "male", "🚽 I heard {user} is using the WC right now… please close the door! We can hear everything! 🚪🙈"),
(2, "male", "🍕 I saw {user} eating pizza… all alone. Share, you greedy snack dragon! 🐉🍕"),
(2, "male", "💘 I heard {user} is going to meet his secret lover tonight! Hope it’s not the fridge… again. 🧊💔"),
(2, "male", "👗 I saw {user} wearing new clothes! Going to a party? Or sneaking into someone’s heart? 😉👚"),
(2, "male", "👀 {user} was walking with someone… I *think* he’s dating… but I need more snacks to confirm. 🍿"),
(2, "male", "🌹 I saw {user} buying a red rose… Ehem ehem… Yes yes… same thing you’re thinking… hehhehe! 🌹😏"),
(2, "male", "🎉 I heard {user} is planning a surprise party for someone… hope it’s not for me! I scare easily! 😱🎁"),
(2, "male", "🔐 I saw {user} talking privately… what could he be saying? “I love you”? “Pass the salt”? DRAMA. 📱"),
(2, "male", "✈️ I saw {user} planning a trip with someone… wonder if it’s romantic or just a getaway from bills? 💸"),

-- 👩‍🦰 Gossip about a female user
(2, "female", "🕌 Eeeh astaghfirollah!!! Look at this one, spying on {user}! Go do istighfar, not TikTok drama! 🤲📿"),
(2, "female", "📿 Don’t ask me about {user} — it’s not my business! Go pray, not stalk! 🙏"),
(2, "female", "💘 {user} has a crush from this group… but I’m sworn to secrecy! (It’s probably @bot.) 🤫🤖"),
(2, "female", "💍 I heard {user} is getting married soon! But the mystery is… who’s the victim? I mean, partner? 😏"),
(2, "female", "💘 I heard {user} is going to confess her feelings soon… hope she doesn’t faint mid-sentence! 💬😳"),
(2, "female", "💘 Rumor: {user} has a secret admirer in this group! Could it be… YOU? 👀❤️"),
(2, "female", "🌍 I heard {user} is traveling abroad! Wish her a safe journey… and Wi-Fi! 📱🧳"),
(2, "female", "📦 I heard {user} is starting a new business… selling love potions? Or just heartbreak? 💔🧪"),
(2, "female", "🔍 I think {user} is hiding something… but my spy glasses are on low battery. 🔋👀"),

(2, "NULL", "Tell me your gender");