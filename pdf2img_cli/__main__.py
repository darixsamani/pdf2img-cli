import typer
from typing import Optional
from . import main

app = typer.Typer(help="This is CLI to transform pdf into images")

@app.command()
def cli(
    pdf: str = typer.Option(..., "--pdf", help="Path to pdf"),
    output_dir: str = typer.Option("images", "--output-dir", help="Output directory"),
    password: Optional[str] = typer.Option(None, "--password", help="PDF password"),
):
    """
    Transform PDF into images
    """
    main(pdf, output_dir, password)

def main_cli():
    app()

if __name__ == "__main__":
    main_cli()
