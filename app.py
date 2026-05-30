from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de dados simulada na memória (Tabela provisória para o MVP)
profissionais = [
    {
        "nome": "Carlos Andrade",
        "categoria": "Construção Civil",
        "localizacao": "Bairro das Nações / Centro",
        "especialidade": "Alvenaria e Reparos",
        "telefone": "5547999999999"
    },
    {
        "nome": "Juliana Souza",
        "categoria": "Estética",
        "localizacao": "Comunidade Novo Horizonte",
        "especialidade": "Manicure e Designer de Unhas",
        "telefone": "5547988888888"
    },
    {
        "nome": "Marcos Lima",
        "categoria": "Manutenção",
        "localizacao": "Toda a Região Periférica",
        "especialidade": "Eletricista Residencial",
        "telefone": "5547977777777"
    }
]


@app.route('/', methods=['GET', 'POST'])
def index():
    # Se o método for POST, significa que o formulário de cadastro foi enviado
    if request.method == 'POST':
        novo_profissional = {
            "nome": request.form.get('nome').strip(),
            "categoria": request.form.get('categoria'),
            "localizacao": request.form.get('localizacao').strip(),
            "especialidade": request.form.get('especialidade').strip(),
            "telefone": request.form.get('telefone').strip().replace(' ', '').replace('-', '')
        }
        
        # Validação simples para garantir que campos obrigatórios foram preenchidos
        if novo_profissional["nome"] and novo_profissional["telefone"]:
            profissionais.append(novo_profissional)
            
        # Redireciona para a mesma página (limpa o formulário e atualiza a lista)
        return redirect(url_for('index'))

    # Tratamento da busca (Método GET)
    busca = request.args.get('search', '').strip().lower()
    
    if not busca:
        return render_template('index.html', profissionais=profissionais, busca=busca)
    
    profissionais_filtrados = []
    for p in profissionais:
        if (busca in p['nome'].lower() or 
            busca in p['categoria'].lower() or 
            busca in p['localizacao'].lower() or 
            busca in p['especialidade'].lower()):
            profissionais_filtrados.append(p)
            
    return render_template('index.html', profissionais=profissionais_filtrados, busca=busca)


if __name__ == '__main__':
    app.run(debug=True)