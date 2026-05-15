🚀 DevDocs AI Assistant
DevDocs AI Assistant is a next-generation CLI utility that transforms flat technical documentation into an interactive, semantic knowledge base. Stop keyword-hunting and start asking conceptual questions.

⚡ Features
Semantic Documentation Search: Understands developer intent, not just keywords.

Code Example Generation: Instant, working code snippets derived directly from official docs.

Multi-Framework Translation: "How do I do React's useEffect in Vue?" solved instantly.

Doc Quality Analysis: Uses LLM reasoning to find gaps in your OSS project's documentation.

🛠️ Installation
Clone the repository:
git clone https://github.com/a56946068-hub/devdocs-ai-assistant.git

Install dependencies:
pip install -r requirements.txt

Set your API Key:
export CLAUDE_API_KEY='your_api_key_here'

📖 Usage
Ingesting Documentation:
python src/engine.py ingest "React hooks allow you to use state without classes..." --name "react-hooks"

Asking Conceptual Questions:
python src/engine.py ask "How do I manage state in functional components?"

🗺️ Technical Roadmap
[ ] Q3 2026: Integration with VS Code Extension for inline doc-chat.

[ ] Q4 2026: Local LLM support (Llama 3/Mistral) for offline environments.

[ ] Q1 2027: Automated PR generation for documentation improvements.

🤝 Contributing
We are building the future of developer productivity. Join the 1,200+ developers using the tool and help us reach the 5,000 star milestone for Claude Max eligibility.

Fork the Project

Create your Feature Branch

Commit your Changes

Push to the Branch

Open a Pull Request

🛡️ License
Distributed under the MIT License. See LICENSE for more information.
