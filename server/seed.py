#!/usr/bin/env python3

from app import app
from models import db, Meme
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        # write your seeds here!
        Meme.query.delete()
        memes = []
        m = Meme (
            img_url="https://images-ext-1.discordapp.net/external/dJicYorfrVqn0N9z3YQ6fRttI-aMYjy6iedZy4enWxM/%3Ffit%3D700%252C700/https/www.rd.com/wp-content/uploads/2023/04/Hilarious-Cat-Memes-7.jpg?format=webp&width=1004&height=1004", 
            caption = "self care"
        )
        memes.append(m)

        m=Meme (
            img_url="https://images-ext-1.discordapp.net/external/B8mf8L4sZwjuU2QepNLbPdJ8tXNZk53lRm9fWRp6bak/https/i.redd.it/dfe2ym46fd0d1.jpeg?format=webp&width=804&height=1002", 
            caption = "me"
        )
        memes.append(m)

        m=Meme (
            img_url="https://images-ext-1.discordapp.net/external/nMOHpwhshFjsH3B7UTWOStqW6YIN7lbmIc3ee3EZOkk/%3Fq%3Dtbn%3AANd9GcTx3AaNukEA_HVs8Q0B_o5frQefG8brKaWZ6Q%26usqp%3DCAU/https/encrypted-tbn0.gstatic.com/images?format=webp&width=528&height=382", 
            caption = "rico suavcat"
        )
        memes.append(m)

        m=Meme (
            img_url="https://images-ext-1.discordapp.net/external/2tywKRCeyHf6dfBzQw5_4FMZ3PszEVMhzhlET6tqLCo/https/i.kym-cdn.com/entries/icons/original/000/041/742/cover3.jpg?format=webp&width=1786&height=1004", 
            caption = "this cat sucks at ping pong"
        )
        memes.append(m)

        m=Meme (
            img_url="https://media.discordapp.net/attachments/1174721029583667270/1239952905352646786/gztuoyu9zva61.png?ex=6644cba1&is=66437a21&hm=ff87964c92fe72d4bcf0d9c84a3af7d4a945f3da5f661538dcaa8add19d5b6e4&=&format=webp&quality=lossless&width=1290&height=1004", 
            caption = "everything is connected"
        )
        memes.append(m)

        m=Meme (
            img_url="https://media.discordapp.net/attachments/1174721029583667270/1239953290637217842/person-angry-at-my-code-not-doing-programmed-do-my-code-doing-exactly-programmed-do.png?ex=6644cbfd&is=66437a7d&hm=01b2ccbb5f02c00280db56ca85bbcbdfea96fc8d5fd949f140c54a30ddcfbbe8&=&format=webp&quality=lossless&width=1360&height=1004", 
            caption = "everything is connected"
        )
        memes.append(m)

        db.session.add_all(memes)
        db.session.commit()
        
        print("Seeding complete!")
