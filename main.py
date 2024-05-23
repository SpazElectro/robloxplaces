from flask import Flask

import bs4, requests

app = Flask(__name__)

@app.get("/<game_id>")
def get_universe(game_id):
    if game_id == None:
        game_id = 12519560096

    game_id = str(game_id)
    req = requests.get(f"https://www.roblox.com/games/{game_id}")

    soup = bs4.BeautifulSoup(req.text, "html.parser")
    metadata = soup.find(id="game-detail-meta-data")
    universe_id = metadata.get("data-universe-id") # type: ignore

    return {
        "universe_id": universe_id,
        "places": requests.get(f"https://develop.roblox.com/v1/universes/{str(universe_id)}/places?isUniverseCreation=false&limit=100&sortOrder=Asc").json()["data"]
    }
