import time

meme_dict = {
    "LOL": "komik bir şeye verilen cevap",
    "CRINGE": "garip ya da utandırıcı bir şey",
    "ROFL": "bir şakaya karşılık cevap",
    "SHEESH": "onaylamamak",
    "CREEPY": "korkunç",
    "AGGRO": "agresifleşmek/sinirlenmek",
    "YEET": "heyecan ya da sevinç ifadesi",
    "SMH": "başını sallayarak hayret etmek",
    "GOAT": "en iyisi, en büyüğü",
    "FOMO": "bir şeyi kaçırma korkusu",
    "YOLO": "bir kere yaşa, hayatı dolu dolu yaşa",
    "ICYMI": "senin için kaçıranlar için, önemli bir şeyi kaçıranlar için",
    "BTW": "bu arada",
    "IMHO": "benim dürüst düşünceme göre",
    "AFK": "klavyeden uzakta",
    "BRB": "hemen döneceğim",
    "TTYL": "seni daha sonra konuşurum"
}

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    print("eğer çıkmak istiyorsanız büyük harflerle EXIT yazın")
    time.sleep(1)
    if word == "EXIT":
        print("Programdan çıkıyorsunuz...")
        time.sleep(0.5)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        break

    if word in meme_dict.keys():
        print(word + " kelimesinin anlamı: " + meme_dict[word])
    else:
        print("Kelimeniz Sözlüğümüzde Bulunmamaktadır")
