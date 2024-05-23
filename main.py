from flask import Flask, request
import bs4, requests

app = Flask(__name__)

@app.route("/")
def get_universe():
    game_id = request.args.get("game_id")
    
    if game_id == None or (isinstance(game_id, str) and not game_id.isdigit()):
        game_id = 12519560096
    game_id = str(game_id)
    req = requests.get(f"https://www.roblox.com/games/{str(game_id)}")

    soup = bs4.BeautifulSoup(req.text, "html.parser")
    metadata = soup.find(id="game-detail-meta-data")
    universe_id = metadata.get("data-universe-id") # type: ignore

    return {
        "universe_id": universe_id,
        "places": requests.get(f"https://develop.roblox.com/v1/universes/{str(universe_id)}/places?isUniverseCreation=false&limit=100&sortOrder=Asc").json()["data"]
    }

if __name__ == "__main__":
    app.run()
