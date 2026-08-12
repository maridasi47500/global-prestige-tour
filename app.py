from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,password,phone,country_id) values (:username,:email,:password,:phone,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','password','phone','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','password','phone','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','password','phone','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_hotel", methods=["GET","POST"])
def add_one_hotel():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into hotel (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from hotel')

        return render_template("hotelform.html", hotels=user, one_user=one_user, the_title="add new hotel", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from hotel')
    one_user = query_db("select * from hotel limit 1", one=True)
    return render_template("hotelform.html", hotels=user, one_user=one_user, the_title="add new hotel", touslescity=touslescity)

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_concert_hall", methods=["GET","POST"])
def add_one_concert_hall():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into concert_hall (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from concert_hall')

        return render_template("concert_hallform.html", concert_halls=user, one_user=one_user, the_title="add new concert_hall", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from concert_hall')
    one_user = query_db("select * from concert_hall limit 1", one=True)
    return render_template("concert_hallform.html", concert_halls=user, one_user=one_user, the_title="add new concert_hall", touslescity=touslescity)

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey)
        user = query_db('select * from musicalinstrument')

        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_userhsainstrument", methods=["GET","POST"])
def add_one_userhsainstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into userhsainstrument (musicalinstrument_id,user_id) values (:musicalinstrument_id,:user_id)",hey)
        user = query_db('select * from userhsainstrument')

        return render_template("userhsainstrumentform.html", userhsainstruments=user, one_user=one_user, the_title="add new userhsainstrument", touslesmusicalinstrument=touslesmusicalinstrument, touslesuser=touslesuser)


    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    touslesuser= query_db("select * from user")

    user = query_db('select * from userhsainstrument')
    one_user = query_db("select * from userhsainstrument limit 1", one=True)
    return render_template("userhsainstrumentform.html", userhsainstruments=user, one_user=one_user, the_title="add new userhsainstrument", touslesmusicalinstrument=touslesmusicalinstrument, touslesuser=touslesuser)

@app.route("/add_one_backstage_note", methods=["GET","POST"])
def add_one_backstage_note():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesworld_tour= query_db("select * from world_tour")

        one_user = query_db("insert into backstage_note (user_id,content,world_tour_id) values (:user_id,:content,:world_tour_id)",hey)
        user = query_db('select * from backstage_note')

        return render_template("backstage_noteform.html", backstage_notes=user, one_user=one_user, the_title="add new backstage_note", touslesuser=touslesuser, touslesworld_tour=touslesworld_tour)


    touslesuser= query_db("select * from user")

    touslesworld_tour= query_db("select * from world_tour")

    user = query_db('select * from backstage_note')
    one_user = query_db("select * from backstage_note limit 1", one=True)
    return render_template("backstage_noteform.html", backstage_notes=user, one_user=one_user, the_title="add new backstage_note", touslesuser=touslesuser, touslesworld_tour=touslesworld_tour)

@app.route("/add_one_world_tour", methods=["GET","POST"])
def add_one_world_tour():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        tousleshotel= query_db("select * from hotel")

        touslesconcert_hall= query_db("select * from concert_hall")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into world_tour (city_id,hotel_id,concert_hall_id,user_id) values (:city_id,:hotel_id,:concert_hall_id,:user_id)",hey)
        user = query_db('select * from world_tour')

        return render_template("world_tourform.html", world_tours=user, one_user=one_user, the_title="add new world_tour", touslescity=touslescity, tousleshotel=tousleshotel, touslesconcert_hall=touslesconcert_hall, touslesuser=touslesuser)


    touslescity= query_db("select * from city")

    tousleshotel= query_db("select * from hotel")

    touslesconcert_hall= query_db("select * from concert_hall")

    touslesuser= query_db("select * from user")

    user = query_db('select * from world_tour')
    one_user = query_db("select * from world_tour limit 1", one=True)
    return render_template("world_tourform.html", world_tours=user, one_user=one_user, the_title="add new world_tour", touslescity=touslescity, tousleshotel=tousleshotel, touslesconcert_hall=touslesconcert_hall, touslesuser=touslesuser)

@app.route("/add_one_photo", methods=["GET","POST"])
def add_one_photo():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesworld_tour= query_db("select * from world_tour")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into photo (world_tour_id,pic,description,user_id) values (:world_tour_id,:pic,:description,:user_id)",hey)
        user = query_db('select * from photo')

        return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo", touslesworld_tour=touslesworld_tour, touslesuser=touslesuser)


    touslesworld_tour= query_db("select * from world_tour")

    touslesuser= query_db("select * from user")

    user = query_db('select * from photo')
    one_user = query_db("select * from photo limit 1", one=True)
    return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo", touslesworld_tour=touslesworld_tour, touslesuser=touslesuser)

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['vid']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["vid"]=uploaded_file.filename


        touslesworld_tour= query_db("select * from world_tour")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into video (world_tour_id,vid,description,user_id) values (:world_tour_id,:vid,:description,:user_id)",hey)
        user = query_db('select * from video')

        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video", touslesworld_tour=touslesworld_tour, touslesuser=touslesuser)


    touslesworld_tour= query_db("select * from world_tour")

    touslesuser= query_db("select * from user")

    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video", touslesworld_tour=touslesworld_tour, touslesuser=touslesuser)

@app.route("/add_one_score", methods=["GET","POST"])
def add_one_score():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into score (city_id,title,user_id,composer,tempo,bpm,key_signature,time_signature,content,lyrics) values (:city_id,:title,:user_id,:composer,:tempo,:bpm,:key_signature,:time_signature,:content,:lyrics)",hey)
        user = query_db('select * from score')

        return render_template("scoreform.html", scores=user, one_user=one_user, the_title="add new score", touslescity=touslescity, touslesuser=touslesuser)


    touslescity= query_db("select * from city")

    touslesuser= query_db("select * from user")

    user = query_db('select * from score')
    one_user = query_db("select * from score limit 1", one=True)
    return render_template("scoreform.html", scores=user, one_user=one_user, the_title="add new score", touslescity=touslescity, touslesuser=touslesuser)

@app.route("/add_one_media_screenshot", methods=["GET","POST"])
def add_one_media_screenshot():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into media_screenshot (user_id,pic,description) values (:user_id,:pic,:description)",hey)
        user = query_db('select * from media_screenshot')

        return render_template("media_screenshotform.html", media_screenshots=user, one_user=one_user, the_title="add new media_screenshot", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from media_screenshot')
    one_user = query_db("select * from media_screenshot limit 1", one=True)
    return render_template("media_screenshotform.html", media_screenshots=user, one_user=one_user, the_title="add new media_screenshot", touslesuser=touslesuser)

