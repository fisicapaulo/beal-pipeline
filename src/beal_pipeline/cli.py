import click
from beal_pipeline.workflows.run_pipeline import run_pipeline

@click.group()
def cli():
    """CLI para o beal-pipeline."""
    pass

@cli.command()
@click.option("--config", type=click.Path(exists=True), default="config.yaml", help="Caminho do arquivo YAML de configuração.")
def run(config):
    """Executa o pipeline completo."""
    run_pipeline(config)

if __name__ == "__main__":
    cli()
