
CREATE TABLE IF NOT EXISTS gossip_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT CHECK( gender IS NULL OR gender IN ('M', 'F', NULL) ),  -- NULL = universal
    topic TEXT NOT NULL,  -- e.g., 'love', 'gym', 'annoyed', 'daily', 'fashion'
    content TEXT NOT NULL, -- the message with {user}
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    used INTGER DEFAULT 0
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


-- 👩‍🍳 COOKING: Gossip about users' culinary adventures (or disasters!)
INSERT INTO gossip_lines (gender, topic, content) VALUES
('M', 'cooking', 'Eeh! {user} tried to cook biryani for his crush… burned the rice, the pot, and almost the kitchen! 🔥'),
('M', 'cooking', 'Lemme tell you… {user} watched 10 “5-minute recipes” but took 2 hours to boil an egg. Hehe! 🥚'),
('M', 'cooking', 'Hehe! {user} said, “Cooking is my love language.” Then he ordered pizza. Classic! 🍕'),
('M', 'cooking', 'Astaghfirollah! {user} put salt instead of sugar in his cake. His dog wouldn’t even eat it! 🐕'),
('M', 'cooking', 'Ooh! {user} bought a fancy apron that says “Chef Boy.” But he still can’t tell the difference between cumin and cinnamon! 😅'),
('M', 'cooking', 'Guess what? {user} tried to impress his date with homemade pasta… served glue. Literally. He used the wrong flour! 🍝'),
('M', 'cooking', 'I saw {user} cry when his instant noodles boiled over… twice. Bro, it’s just noodles! 😂'),
('M', 'cooking', 'Hehehe! {user} calls his burnt toast “artisanal charcoal bread.” Okay, chef! 🍞'),
('M', 'cooking', 'Eeh! {user} asked Google: “How to boil water?” …and still got it wrong. 💧'),
('M', 'cooking', 'Don’t tell anyone… but {user} thinks “al dente” is a type of pasta brand. Shhh! 🤫');

INSERT INTO gossip_lines (gender, topic, content) VALUES
('F', 'cooking', 'Eeh! {user} tried to bake a cake for her boyfriend… it came out looking like a UFO! 👽'),
('F', 'cooking', 'Lemme tell you… {user} followed a TikTok recipe and turned her kitchen into a smoke zone! 🌫️'),
('F', 'cooking', 'Hehe! {user} says she’s “Gordon Ramsay in disguise,” but her omelette looks like a sad pancake. 🥞'),
('F', 'cooking', 'Astaghfirollah! {user} used vanilla extract instead of vinegar in her salad. Her date ran away! 🥗'),
('F', 'cooking', 'Ooh! {user} bought a pink chef hat and matching spatula… but still microwaves everything. 💖'),
('F', 'cooking', 'Guess what? {user} tried to make sushi… used gummy bears as “fish.” Creative, but no! 🍣'),
('F', 'cooking', 'I saw {user} argue with her rice cooker like it’s her ex. “Why won’t you listen to me?!” 😤'),
('F', 'cooking', 'Hehehe! {user} calls her burnt cookies “crispy soul snacks.” Okay, queen! 👑'),
('F', 'cooking', 'Eeh! {user} Googled “how to peel garlic” and watched a 20-minute tutorial… then used garlic powder. 🧄'),
('F', 'cooking', 'Don’t tell anyone… but {user} thinks “sauté” means “throw it in and pray.” Shhh! 🙏')



-- 🏀 SPORT: Gossip about users' athletic (or not-so-athletic) adventures!
INSERT INTO gossip_lines (gender, topic, content) VALUES
('M', 'sport', 'Eeh! {user} said he’s “training like Ronaldo”… but his workout is lifting the remote! 📺'),
('M', 'sport', 'Lemme tell you… {user} joined a gym last week. So far, he’s only mastered the treadmill… as a clothes hanger! 👕'),
('M', 'sport', 'Hehe! {user} challenged his friend to a football match… tripped over the ball before kickoff! ⚽'),
('M', 'sport', 'Astaghfirollah! {user} wore football gloves to play FIFA on PlayStation. Bro, it’s a controller! 🎮'),
('M', 'sport', 'Ooh! {user} bought expensive sneakers… still can’t run faster than his Wi-Fi signal! 📶'),
('M', 'sport', 'Guess what? {user} says he’s “in his prime”… his prime was in 2012 when he scored one goal in school! 🥅'),
('M', 'sport', 'I saw {user} stretch for 10 minutes… then walked to the fridge. That’s his cardio! 🥤'),
('M', 'sport', 'Hehehe! {user} calls his daily walk to the mosque “ultra-marathon training.” Okay, athlete! 🏃‍♂️'),
('M', 'sport', 'Eeh! {user} tried to do a backflip… ended up calling his mom for help. Again. 📞'),
('M', 'sport', 'Don’t tell anyone… but {user} thinks “NBA” stands for “Nice Basketball App.” Shhh! 🤫');

INSERT INTO gossip_lines (gender, topic, content) VALUES
('F', 'sport', 'Eeh! {user} said she’s “Serena Williams in disguise”… but her tennis racket is still in the box! 🎾'),
('F', 'sport', 'Lemme tell you… {user} signed up for yoga. So far, she’s mastered “corpse pose” — during Netflix! 🛋️'),
('F', 'sport', 'Hehe! {user} challenged her friend to a race… lost to a toddler on a scooter! 🛴'),
('F', 'sport', 'Astaghfirollah! {user} wore full sports gear just to walk her dog… who walked her instead! 🐕'),
('F', 'sport', 'Ooh! {user} bought a fitness tracker… it’s confused why her heart rate spikes during drama series! ❤️‍🔥'),
('F', 'sport', 'Guess what? {user} says she “runs 5K daily”… it’s 5K steps to the kitchen and back! 👟'),
('F', 'sport', 'I saw {user} do one push-up… then posted it as “Day 1 of my transformation.” We believe in you! 💪'),
('F', 'sport', 'Hehehe! {user} calls her dance party in the room “high-intensity interval training.” Valid! 🎶'),
('F', 'sport', 'Eeh! {user} tried to shoot a basketball… hit the lightbulb. Now we’re in the dark! 💡'),
('F', 'sport', 'Don’t tell anyone… but {user} thinks “FIFA” is a type of salad. Shhh! 🥗');



-- 👗 CLOTHES: Spicy, exaggerated, and actually funny fashion gossip!
INSERT INTO gossip_lines (gender, topic, content) VALUES
('M', 'clothes', 'Eeh! {user} wore socks with sandals to a wedding… and called it “fusion fashion.” Bro, you’re not a tourist! 🩴'),
('M', 'clothes', 'Lemme tell you… {user} spent 3 hours doing his hair, then wore a beanie. The mirror cried! 😭'),
('M', 'clothes', 'Hehe! {user} says his ripped jeans are “high fashion”… bro, your mom asked if you got attacked by a dog! 🐕'),
('M', 'clothes', 'Astaghfirollah! {user} tried to layer 3 hoodies “like in K-dramas”… now he’s sweating like he ran a marathon! 💦'),
('M', 'clothes', 'Ooh! {user} bought fake designer shades… they fog up when he lies. Very useful! 😎'),
('M', 'clothes', 'Guess what? {user} wore a tuxedo T-shirt to a job interview. HR said, “We hire humans, not memes.” 🤡'),
('M', 'clothes', 'I saw {user} iron his shirt… then spill biryani on it. Now it’s “edible couture.” 🍛'),
('M', 'clothes', 'Hehehe! {user} says his all-black outfit is “mysterious”… nah, you just forgot laundry day! 🖤'),
('M', 'clothes', 'Eeh! {user} wore neon green pants to the mosque. Even the imam blinked twice! 🟢'),
('M', 'clothes', 'Don’t tell anyone… but {user} thinks “tailored fit” means “tight enough to scare your future kids.” Shhh! 👶');

INSERT INTO gossip_lines (gender, topic, content) VALUES
('F', 'clothes', 'Eeh! {user} wore 7-inch heels to a picnic… now she’s stuck in the grass like a flamingo! 🦩'),
('F', 'clothes', 'Lemme tell you… {user}’s “casual outfit” cost more than my monthly rent. And she’s going to the *library*! 📚'),
('F', 'clothes', 'Hehe! {user} says her dress is “breathable”… but it’s so tight, her phone can’t fit in the pocket! 📱'),
('F', 'clothes', 'Astaghfirollah! {user} wore a fur coat in 45°C… says it’s “vintage.” Girl, it’s melting! ❄️🔥'),
('F', 'clothes', 'Ooh! {user} matched her lipstick to her handbag… but forgot to wear pants. Wait—was that intentional? 👜'),
('F', 'clothes', 'Guess what? {user} tried “quiet luxury”… but her gold chain says “Property of Drama Queen.” ✨'),
('F', 'clothes', 'I saw {user} change outfits 5 times before a Zoom call… camera was off the whole time! 📹'),
('F', 'clothes', 'Hehehe! {user} calls her oversized sunglasses “face armor.” Honestly? They’re hiding 3 days of no sleep! 😴'),
('F', 'clothes', 'Eeh! {user} wore a wedding guest dress to buy groceries… now the cashier asked for her autograph! 🛒'),
('F', 'clothes', 'Don’t tell anyone… but {user} thinks “boho chic” means “I lost my scarf in 2019 and never looked back.” Shhh! 🧣');







