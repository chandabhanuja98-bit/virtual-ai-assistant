import random

def get_random_joke():
    jokes = [
    "Why did the computer go to the doctor? Because it had a virus! ",
    "Why was the math book sad? Because it had too many problems! ",
    "What do you call a bear with no teeth? A gummy bear! ",
    "Why did the bicycle fall over? Because it was two-tired! ",
    "What do you call a sleeping bull? A bulldozer! ",
    "Why don't eggs tell jokes? Because they might crack each other up! ",
    "What did one wall say to the other wall? I'll meet you at the corner! ",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake! ",
    "What do you call a fish wearing a bowtie? Sofishticated! ",
    "Why did the programmer quit his job? Because he didn't get arrays of support! "
    ]

    return random.choice(jokes)

def get_random_quote():

    quotes = [
    "Believe in yourself and keep moving forward.",
    "Success comes from consistent effort.",
    "Every day is a new opportunity to learn.",
    "Dream big and work hard.",
    "Small steps can lead to big achievements.",
    "Never stop learning and growing.",
    "Challenges help you become stronger.",
    "Your future depends on what you do today.",
    "Stay positive and keep trying.",
    "Great things take time and patience."
    ]

    return random.choice(quotes)

def get_random_fact():

    facts = [
    "Honey never spoils when stored properly.",
    "Octopuses have three hearts.",
    "Bananas are botanically classified as berries.",
    "The Earth takes about 365.25 days to orbit the Sun.",
    "Water covers about 71 of Earth's surface.",
    "A group of flamingos is called a flamboyance.",
    "Sharks existed before trees appeared on Earth.",
    "The human brain uses about 20 of the body's energy.",
    "Lightning can heat the air around it to extremely high temperatures.",
    "The Moon has no atmosphere like Earth's."
    ]

    return random.choice(facts)


