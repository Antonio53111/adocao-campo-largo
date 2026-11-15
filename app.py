from flask import Flask, render_template

app = Flask(__name__)

# Rota da Tela 1: Vitrine de Animais (Menu Inicial)
@app.route('/')
def index():
    # Dados fictícios para demonstrar o MVP na vitrine
    animais = [
        {"nome": "Thor", "especie": "Cachorro", "porte": "Médio", "status": "Disponível", "vacinado": True, "castrado": True},
        {"nome": "Luna", "especie": "Gato", "porte": "Pequeno", "status": "Disponível", "vacinado": True, "castrado": True}
    ]
    return render_template('index.html', animais=animais)

if __name__ == '__main__':
    app.run(debug=True)