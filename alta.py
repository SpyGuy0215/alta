import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet you with!', default='World')
def hello(name):
    click.echo(f"Hello {name}!")