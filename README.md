# 🧠 Habit Tracker

Um aplicativo simples para rastrear hábitos diários e ajudar no desenvolvimento pessoal por meio da consistência.

## 🚀 Funcionalidades

- ✅ Adicionar e remover hábitos
- 📅 Marcar hábitos como concluídos por dia
- 📊 Visualizar progresso diário/semanal
- 💾 Salvamento local dos dados via arquivo JSON
- 🌐 Uso de API para salvar e gerenciar os dados

## 🛠️ Tecnologias Utilizadas

- Python 3
- PySide6

## 📁 Estrutura do Projeto
 ```bash
habit-tracker/
│
├── files/                     # Pasta para arquivos adicionais (ex: logo, JSON de dados)
│   ├── habits.json            # Arquivo JSON para salvar os dados dos hábitos
│   └── logo.png               # Logo do aplicativo
│
├── telas/                     # Módulos das telas da aplicação
│   ├── calendar.py            # Tela/calendário para seleção e visualização das datas
│   └── habits.py              # Tela para gerenciar hábitos
│
├── utils/                     # Utilitários e funções auxiliares
│   ├── api_connection.py      # API para salvar e carregar dados
│   └── variables.py           # Variáveis globais e configurações
│
├── main.py                    # Arquivo principal que inicia a aplicação
├── main_window.py             # Define a janela principal e a navegação entre telas
├── README.md                  # Documentação do projeto
├── LICENSE                    # Licença do projeto
├── requirements.txt           # Dependências do projeto
```

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/edersoncruz/habit-tracker.git
   cd habit-tracker
   ```

2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o aplicativo:
   ```bash
   python main.py
   ```

## 📸 Capturas de Tela

<img width="350" height="300" alt="4" src="https://github.com/user-attachments/assets/192683e7-f1d9-4c3a-aecc-d13391e7ae3e" />
<img width="350" height="298" alt="5" src="https://github.com/user-attachments/assets/efda62be-68f0-4d2c-8842-45ea624e614c" />




## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a MIT License.
