from flask import Flask, render_template

app = Flask(__name__)

# Dados simulados dos animais para a vitrine (MVP)
ANIMALS = [
    {
        "id": 1,
        "name": "Thor",
        "category": "Cachorro",
        "size": "Médio",
        "status": "DISPONÍVEL",
        "details": "✅ Vacinado ✅ Castrado",
    },
    {
        "id": 2,
        "name": "Luna",
        "category": "Gato",
        "size": "Pequeno",
        "status": "DISPONÍVEL",
        "details": "✅ Vacinado ✅ Castrado",
    },
]


@app.route("/")
def index():
  return render_template("index.html", animals=ANIMALS)


if __name__ == "__main__":
  app.run(debug=True)