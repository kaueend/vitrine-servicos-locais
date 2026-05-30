from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista inicial com os 3 profissionais para o teu MVP da UNIVALI
prestadores = [
    {
        "nome": "Carlos Andrade",
        "categoria": "Construção Civil",
        "bairro": "Bairro das Nações / Centro",
        "descricao": "Foco: Alvenaria e Reparos",
        "whatsapp": "47999999999"
    },
    {
        "nome": "Juliana Souza",
        "categoria": "Estética",
        "bairro": "Comunidade Novo Horizonte",
        "descricao": "Foco: Manicure e Designer de Unhas",
        "whatsapp": "47999999998"
    },
    {
        "nome": "Marcos Lima",
        "categoria": "Manutenção",
        "bairro": "Toda a Região Periférica",
        "descricao": "Foco: Eletricista Residencial",
        "whatsapp": "47999999997"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    # Sistema de busca por texto
    if request.method == "POST":
        termo = request.form.get("pesquisa", "").lower()
        resultados = [
            p for p in prestadores 
            if termo in p["nome"].lower() or termo in p["bairro"].lower() or termo in p["descricao"].lower()
        ]
        return render_template("index.html", prestadores=resultados)
    
    # Sistema de filtros por botões de categoria
    categoria_filtrada = request.args.get("categoria")
    if categoria_filtrada:
        resultados = [p for p in prestadores if p["categoria"] == categoria_filtrada]
        return render_template("index.html", prestadores=resultados)

    return render_template("index.html", prestadores=prestadores)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    # Recebe os dados enviados pelo formulário flutuante (Modal)
    novo_prestador = {
        "nome": request.form.get("nome"),
        "categoria": request.form.get("categoria"),
        "bairro": request.form.get("bairro"),
        "descricao": request.form.get("descricao"),
        "whatsapp": request.form.get("whatsapp")
    }
    # Adiciona o novo profissional na lista em memória
    prestadores.append(novo_prestador)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)