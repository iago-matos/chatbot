# --- 1. O Cardápio (Nossa "Base de Dados") ---
# Usamos uma lista de dicionários. Cada dicionário é um prato.
cardapio = [
    {
        'nome': 'Hambúrguer Clássico', 
        'tipo': 'carne', 
        'apimentado': False,
        'estilo': 'fast-food'
    },
    {
        'nome': 'Pizza Pepperoni', 
        'tipo': 'carne', 
        'apimentado': True,
        'estilo': 'fast-food'
    },
    {
        'nome': 'Salada Caesar Fit', 
        'tipo': 'vegetariano', 
        'apimentado': False,
        'estilo': 'saudavel'
    },
    {
        'nome': 'Curry de Legumes', 
        'tipo': 'vegetariano', 
        'apimentado': True,
        'estilo': 'exotico'
    },
    {   
        'nome': 'Frango Grelhado com Brócolis', 
        'tipo': 'carne', 
        'apimentado': False,
        'estilo': 'saudavel'
    },
    {
        'nome': 'Tacos de Carne Apimentados', 
        'tipo': 'carne', 
        'apimentado': True,
        'estilo': 'exotico'
    }
]

# --- 2. A Entrevista (Coletando preferências) ---
print("--- Bem-vindo ao Assistente de Pedidos! ---")
print("Vou te ajudar a encontrar o prato perfeito. Responda algumas perguntas:")

# Pergunta 1: Tipo de comida
# Usamos .strip() para remover espaços e .lower() para padronizar a resposta
pref_tipo = input("Você prefere 'carne' ou 'vegetariano'? ").strip().lower()

# Pergunta 2: Apimentado
pref_apimentado_raw = input("Você gosta de comida apimentada? (s/n) ").strip().lower()

# Pergunta 3: Estilo
pref_estilo = input("Qual estilo de comida você busca? ('fast-food', 'saudavel', 'exotico') ").strip().lower()


# --- 3. A Lógica (Filtrando as recomendações) ---

# Convertendo a resposta 's/n' para True/False
gosta_apimentado = True if pref_apimentado_raw == 's' else False

# Começamos com uma lista vazia de pratos que batem com as preferências
recomendacoes = []

# Usamos um loop 'for' para checar cada prato do cardápio
for prato in cardapio:
    if (prato['tipo'] == pref_tipo and 
        prato['apimentado'] == gosta_apimentado and 
        prato['estilo'] == pref_estilo):
        
        # Se o prato bater com TUDO, adicionamos na lista
        recomendacoes.append(prato)

# --- 4. O Resultado (Apresentando a recomendação) ---
print("\n--- Pratos recomendados para você: ---")

if not recomendacoes: # Checa se a lista 'recomendacoes' está vazia
    print("Puxa, não encontrei nenhum prato com essa combinação exata.")
    print("Tente outras preferências!")
else:
    # Se a lista não estiver vazia, mostramos os pratos
    for prato in recomendacoes:
        print(f" {prato['nome']}")

print("\n--- Bom apetite! ---")