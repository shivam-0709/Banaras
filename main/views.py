from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Varanasi Tourism</title>
    </head>

    <body style="
        background: linear-gradient(to right, skyblue, lightpink);
        font-family: Arial;
        text-align: center;
        padding: 30px;
    ">

        <h1>🌸 Welcome to Varanasi 🌸</h1>

        <p>
        Varanasi, also known as Banaras, is one of the oldest living cities in the world.
        It is located on the banks of the holy river Ganga and is a major spiritual center of India.
        </p>

        <h2>✨ Famous Places</h2>

        <p>🛕 Kashi Vishwanath Temple - One of the most important temples of Lord Shiva</p>
        <p>🌊 Dashashwamedh Ghat - Famous for Ganga Aarti</p>
        <p>🚤 Assi Ghat - Peaceful place for tourists and locals</p>
        <p>🏛️ Sarnath - Place where Buddha gave his first sermon</p>

        <h2>🎉 Things to Do</h2>

        <p>🌅 Watch sunrise on the Ganga river</p>
        <p>🕯️ Attend Ganga Aarti in evening</p>
        <p>🛶 Enjoy boat ride</p>
        <p>🍛 Taste Banarasi street food</p>

        <h2>🍲 Famous Food</h2>

        <p>🍲 Kachori Sabzi</p>
        <p>🥤 Lassi</p>
        <p>🍧 Rabri</p>
        <p>🌿 Banarasi Paan</p>

        <h2>💡 Why Visit?</h2>

        <p>
        Varanasi is not just a city, it's an experience of spirituality, culture, and tradition.
        Every street has a story, and every ghat has a history.
        </p>

        <button onclick="showMsg()">Click for Magic ✨</button>
        <p id="msg"></p>

        <script>
            function showMsg(){
                document.getElementById("msg").innerHTML =
                "✨ Welcome to the spiritual heart of India - Varanasi ✨";
            }
        </script>

    </body>
    </html>
    """)