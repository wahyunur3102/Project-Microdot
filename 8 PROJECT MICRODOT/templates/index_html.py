# Autogenerated file
def render(*a, **d):
    yield """<!doctype html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\"
          content=\"width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0\">
    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">
    <title>Smart Dashboard</title>

    <!-- STYLE CSS -->
    <link rel=\"stylesheet\" href=\"/static/style.css\">
</head>

<style>
    body """
    yield """{
        background-image: url(\"/static/img/bg.jpeg\");
        background-size: 100% 200%;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>

<body>
<div class=\"logo_tut\">
    <img src=\"/static/img/tut.png\" style=\"width: 85px; height: 85px;\"></div>

<div class=\"logo_vedc\">
    <img src=\"/static/img/vedc.png\" style=\"width: 100px; height: 70px;\"></div>

<div class=\"pos_font\">
    <h1 style=\"font-family: 'Bookman Old Style'\">DEPARTEMEN TEKNOLOGI INFORMASI</h1>
    <h3 style=\"font-family: 'Berlin Sans FB Demi'\">Balai Besar Pengemangan Penjaminan Mutu
        Pendidikan Vokasi Bidang Otomotif dan Elektronika</h3>
    <h5 style=\"font-family: 'Berlin Sans FB Demi'\"><u>Jl. Teluk Mandar, Arjosari, Kec. Blimbing, Kota Malang, Jawa Timur 65102</u></h5>
</div>

<div class=\"row\">
    <div class=\"navigation\">
        <h4 style=\"font-family: Gadugi\">DASHBOARD SISTEM MONITORING DAN CONTROLLING</h4>
    </div>
    <div class=\"ip\" style=\"text-align: center; margin-top: -2px\">
        <h3></h3>
    </div>

</div>


<div class=\"gauge-container\">
    <div class=\"gauge-card-1\">
        <h4>TEMPERATURE</h4>
        <div class=\"gauge\">
            <div class=\"gauge__body\">
                <div class=\"gauge__fill\"></div>
                <div class=\"gauge__cover\"></div>
            </div>
        </div>
    </div>

    <div class=\"gauge-card-2\">
        <h4>HUMIDITY</h4>
        <div class=\"gauge\">
            <div class=\"gauge__body\">
                <div class=\"gauge__fill\"></div>
                <div class=\"gauge__cover\"></div>
            </div>
        </div>
    </div>

    <div class=\"gauge-card-3\">
        <h4>ALTITUDE</h4>
        <div class=\"gauge\">
            <div class=\"gauge__body\">
                <div class=\"gauge__fill\"></div>
                <div class=\"gauge__cover\"></div>
            </div>
        </div>
    </div>

    <div class=\"gauge-card-4\">
        <h4>PRESSURE</h4>
        <div class=\"gauge\">
            <div class=\"gauge__body\">
                <div class=\"gauge__fill\"></div>
                <div class=\"gauge__cover\"></div>
            </div>
        </div>
    </div>

    <div class=\"gauge-card-5\">
        <h4>TEMPERATURE, HUMIDITY</h4>
        <canvas id=\"lineChart\"></canvas>
    </div>

    <div class=\"gauge-card-6\">
        <h4 style>AIR QUALITY</h4>
        <div class=\"gauge\">
            <div class=\"gauge__body\">
                <div class=\"gauge__fill\"></div>
                <div class=\"gauge__cover\"></div>
            </div>
        </div>
    </div>

    <div class=\"gauge-card-7\">
        <h4 style>STATUS</h4><hr>
        <div class=\"quality\"><h5></h5><br></div>
        <p>GARDEN LAMP :</p><br>
        <div class=\"lamp1\"><h3></h3><br></div>
        <P>TERRACE LAMP :</P><br>
        <div class=\"lamp2\"><h3></h3><br></div>
        <p>ROOM LAMP :</p><br>
        <div class=\"lamp3\"><h3></h3></div>
    </div>

    <div class=\"main-card-1\">
        <h3>GARDEN</h3><br>
        <div class=\"button-container\">
            <button type=\"button\" name=\"button-settings\" id=\"Hijau1\" class=\"button button1\" value=\"on1\"
                    onClick=\"changeStatus(this.value)\">ON</button>
            <button type=\"button\" name=\"button-settings\" id=\"Merah1\" class=\"button button2\" value=\"off1\"
                    onClick=\"changeStatus(this.value)\">OFF</button>
        </div>
    </div>

    <div class=\"main-card-2\">
        <h3>TERRACE</h3><br>
        <div class=\"button-container\">
            <button type=\"button\" name=\"button-settings\" id=\"Hijau2\" class=\"button button1\" value=\"on2\"
                    onClick=\"changeStatus(this.value)\">ON</button>
            <button type=\"button\" name=\"button-settings\" id=\"Merah2\" class=\"button button2\" value=\"off2\"
                    onClick=\"changeStatus(this.value)\">OFF</button>
        </div>
    </div>

    <div class=\"main-card-3\">
        <h3>ROOM</h3><br>
        <div class=\"button-container\">
            <button type=\"button\" name=\"button-settings\" id=\"Hijau3\" class=\"button button1\" value=\"on3\"
                    onClick=\"changeStatus(this.value)\">ON</button>
            <button type=\"button\" name=\"button-settings\" id=\"Merah3\" class=\"button button2\" value=\"off3\"
                    onClick=\"changeStatus(this.value)\">OFF</button>
        </div>
    </div>

    <div class=\"main-card-4\">
        <h3>ALARM</h3><br>
        <div class=\"button-container\">
            <button type=\"button\" name=\"button-settings\" id=\"Hijau4\" class=\"button button1\" value=\"on4\"
                    onClick=\"changeStatus(this.value)\">ON</button>
            <button type=\"button\" name=\"button-settings\" id=\"Merah4\" class=\"button button2\" value=\"off4\"
                    onClick=\"changeStatus(this.value)\">OFF</button>
        </div>
    </div>
</div>

<div class=\"copy\">
    <p>@Copyright by Departemen TI BBPPMPV BOE Malang 2024</p>
</div>


<!-- SCRIPT -->
<script src=\"https://cdn.jsdelivr.net/npm/moment@2.29.4/moment.min.js\"></script>
<script src=\"https://cdn.jsdelivr.net/npm/chart.js@4.3.3/dist/chart.umd.min.js\"></script>
<script src=\"/static/script.js\"></script>
<script src=\"/static/kontrol.js\"></script>

</body>
</html>


"""
