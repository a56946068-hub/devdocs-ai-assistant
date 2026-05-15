import os
import click
import chromadb
from anthropic import Anthropic
from sentence_transformers import SentenceTransformer
from rich.console import Console
from rich.markdown import Markdown

# Director: Insert your key here
CLAUDE_API_KEY = "your_anthropic_api_key"
client = Anthropic(api_key=CLAUDE_API_KEY)
console = Console()
embed_model = SentenceTransformer('all-MiniLM-L6-v2')
chroma_client = chromadb.PersistentClient(path="./devdocs_db")
collection = chroma_client.get_or_create_collection(name="tech_docs")

class DevDocsEngine:
    def __init__(self):
        self.system_prompt = (
            "You are the DevDocs AI Assistant. Your goal is to provide semantic search, "
            "code example generation, and framework translation based on provided context."
        )

    def add_documentation(self, doc_id, text, metadata):
        vector = embed_model.encode(text).tolist()
        collection.add(
            ids=[doc_id],
            embeddings=[vector],
            documents=[text],
            metadatas=[metadata]
        )

    def query(self, user_input):
        query_vector = embed_model.encode(user_input).tolist()
        results = collection.query(query_embeddings=[query_vector], n_results=3)
        context = "\n".join(results['documents'][0])
        
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            system=self.system_prompt,
            messages=[{"role": "user", "content": f"Context:\n{context}\n\nQuestion: {user_input}"}]
        )
        return response.content[0].text

@click.group()
def cli():
    """DevDocs AI Assistant - Nexus Terminal Edition"""
    pass

@cli.command()
@click.argument('text')
@click.option('--name', help='Document name')
def ingest(text, name):
    engine = DevDocsEngine()
    engine.add_documentation(doc_id=name, text=text, metadata={"source": name})
    console.print(f"[green]Indexed: {name}[/green]")

@cli.command()
@click.argument('question')
def ask(question):
    engine = DevDocsEngine()
    with console.status("[bold blue]Querying..."):
        answer = engine.query(question)
    console.print(Markdown(answer))

if __name__ == "__main__":
    cli()