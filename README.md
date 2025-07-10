# 🧠 Habbit Tracker

Um aplicativo simples para rastrear hábitos diários e ajudar no desenvolvimento pessoal por meio da consistência.

## 🚀 Funcionalidades

- ✅ Adicionar e remover hábitos
- 📅 Marcar hábitos como concluídos por dia
- 📊 Visualizar progresso diário/semanal
- 💾 Salvamento local dos dados

## 🛠️ Tecnologias Utilizadas

- Python 3
- PySide6

## 📁 Estrutura do Projeto
 ```bash
habbit-tracker/
│
├── files/                     # Pasta para arquivos adicionais (ex: logo, etc)
│
├── telas/                     # Módulos das telas da aplicação
│   ├── calendar.py            # Tela/calendário para seleção e visualização das datas
│   ├── habbits.py             # Tela para gerenciar hábitos
│   └── habits.json            # Arquivo JSON para salvar dados dos hábitos
│
├── main.py                    # Arquivo principal que inicia a aplicação
├── main_window.py             # Define a janela principal e a navegação entre telas
├── variables.py               # Variáveis globais e configurações usadas no projeto
├── requirements.txt           # Dependências do projeto para instalação via pip
└── README.md                  # Documentação do projeto
```

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/edersoncruz/habbit-tracker.git
   cd habbit-tracker
   ```

2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale o Pyside6:
   ```bash
   pip install pyside6
   ```

4. Execute o aplicativo:
   ```bash
   python main.py
   ```

## 📸 Capturas de Tela

<img width="416" height="340" alt="1" src="https://github.com/user-attachments/assets/a81df3e7-c237-482e-ad8b-939f8aad93a6" />
<img width="415" height="340" alt="2" src="https://github.com/user-attachments/assets/341d89d7-fa89-45cb-9b93-94a6ad7b43c0" />



## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a MIT License.
