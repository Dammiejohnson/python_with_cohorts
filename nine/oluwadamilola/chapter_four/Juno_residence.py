juno_data = [
    {
    "administrators": ['Seyi Barber', 'Olaoluwa Oyinbo', 'Seun Bello', 'Charity Miracle'],
    "address": "10, Emily Akinola Street, Chemist Bariga, Lagos",
    "phone_number": +2349086543267,
    "Investors": ["Sankore inc", "Semicolon.africa", "Radeecal Ltd"],
    "url": "https://www.juno.africa.homes.com",
    },

    {"residents": [
        {
        "semicolon_natives": ["Oluwadamilola", "Chinonso", "Ademijuwonlo"],
        "unilag_students": ["Busola", "Oluwapelumi", "Ayomide"],
        "working_class_peeps": {
            "lawyers": ["Chidera", "Daniel", "Ekene", "Halimat"],
            "entrepreneurs": ["Oja", "Fola cleaning services", "Judith Beddings", "Catalyst tutors"],
            "crypto_miners": ["Ademiju", "LotaChi", "Ayomide", "Olamilekan"]
                            }
         }
                ]
    },

    {"semicolon_natives": [
            {
                "full_name": "Sanni Oluwadamilola",
                 "age": 10,
                 "access_card_no": "4G58/CAR",
                 "room_number": 58,
                 "bunk_id": "A",
                 "phone_number": +2348183456781 
             },
            {
                "full_name": "Chinonso Charity",
                 "age": 15,
                 "access_card_no": "4F57/CAR",
                 "room_number": 50,
                 "bunk_id": "B",
                 "phone_number": +2348153456989
             },
             {
                "full_name": "Ademijuwonlo Tee",
                "age": 11,
                "access_card_no": "4B58/CAR",
                "room_number": 58,
                 "bunk_id": "B",
                 "phone_number": +2348193556782
              }
                    ]
    },

    {"unilag_students": [
            {
                "full_name": "Busola Owoeye",
                 "age": 7,
                 "access_card_no": "4G49/CAR",
                 "room_number": 49,
                 "bunk_id": "D",
                 "phone_number": +2348183906782
             },
            {
                "full_name": "Oluwapelumi Majekodunmi",
                 "age": 20,
                 "access_card_no": "4F57/CAR",
                 "room_number": 57,
                 "bunk_id": "C",
                 "phone_number": +2348153452084
             },
             {
                "full_name": "Ayomide Ifeoluwa",
                "age": 90,
                "access_card_no": "4B80/CAR",
                "room_number": 80,
                 "bunk_id": "D",
                 "phone_number": +2348132556788
              }
                    ]
    }

        ]
#to print Busola
print(juno_data[1]["residents"][0]["unilag_students"][0])

#to print the full name of all semicolon natives
semicolon_natives = juno_data[2]["semicolon_natives"]

for i in semicolon_natives:
    print(i["full_name"])
