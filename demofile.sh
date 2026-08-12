
mkdir templates 
python3 scaffold.py user username email password phone country_id:references
python3 scaffold.py country name
python3 scaffold.py hotel name city_id:references
python3 scaffold.py city name country_id:references
python3 scaffold.py concert_hall name city_id:references
python3 scaffold.py musicalinstrument name
python3 scaffold.py userhsainstrument musicalinstrument_id:references user_id:references
python3 scaffold.py backstage_note user_id:references content world_tour_id:references
python3 scaffold.py world_tour city_id:references hotel_id:references concert_hall_id:references user_id:references
python3 scaffold.py photo world_tour_id:references pic:file description user_id:references
python3 scaffold.py video world_tour_id:references vid:file description user_id:references
python3 scaffold.py score city_id:references title user_id:references composer tempo bpm key_signature time_signature content lyrics
python3 scaffold.py media_screenshot user_id:references pic:file description
