# 🤖 Chatbot de Recomendação de Pratos

Este é um projeto de chatbot simples desenvolvido em Python, inspirado pela cultura de inovação e IA do iFood. O objetivo é demonstrar a lógica de programação e o desenvolvimento de software para criar um "agente inteligente" capaz de filtrar um cardápio e recomendar pratos com base nas preferências do usuário.

---

## 🎯 Objetivo

O projeto foi criado para atender aos requisitos da vaga de estágio em IA [Ref. 100129], que valoriza a "fome de construir" e a demonstração prática de habilidades.

Em vez de focar em modelos complexos de ML, este projeto foca nos fundamentos:

* **Lógica de Programação:** Uso de condicionais (`if/else`) e loops (`for`) para filtrar dados.
* **Estrutura de Dados:** Utilização de listas e dicionários Python para simular um cardápio (uma base de dados).
* **Interação com Usuário:** Captura e tratamento de inputs do usuário (`.lower()`, `.strip()`) para tornar o agente funcional.

---

## 🚀 Como Executar

Este projeto usa apenas bibliotecas nativas do Python. Não é necessário criar ambientes virtuais ou instalar pacotes.

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd nome-da-pasta
    ```
3.  Execute o script:
    ```bash
    python chatbot.py
    ```
4.  O chatbot começará a rodar no seu terminal e fará as perguntas.

---

## 💡 O que eu aprendi / Próximos Passos

Este projeto reforçou minha habilidade em traduzir regras de negócio (as preferências do usuário) em lógica de código funcional.

Como próximos passos, este projeto poderia evoluir para:

* Integrar uma biblioteca de NLP (como spaCy ou NLTK) para entender frases mais complexas, em vez de apenas respostas "s/n".
* Conectar-se a um banco de dados real (como SQL ou MongoDB) para escalar o cardápio.
* Implementar um sistema de "fuzzy matching" para lidar com erros de digitação do usuário.