class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


ti_reshi_lyrics = """С теб говориме отново за любов! 
Приближава се големият въпрос! 
Обичаш ли ме? 
И го отлагаме за да не чуем не! 
Но си знаеме, че е дошъл момент, да го зададем! 

Ти реши, ще ме свалиш на пода с твойто сбогом, без сълзи?
Или със мен ще си? 
Ти реши, без теб съм празно тяло, сам изцяло! 
Ти реши, ще ме обичаш ли? 

С теб избираме дори куршумите! 
Не боли от тях, като от думите! 
Обичаш ли ме? 
И го отлагаме за да не чуем не! 
Но си знаеме, че е дошъл момент, да ги изречем!

Ти реши, ще ме свалиш на пода с твойто сбогом, без сълзи?
Или със мен ще си? 
Ти реши, без теб съм празно тяло, сам изцяло! 
Ти реши, ще ме обичаш ли?"""

ti_reshi = Music("Ти реши", "Борис Дали", ti_reshi_lyrics)
print(ti_reshi.print_info())
print(ti_reshi.play())