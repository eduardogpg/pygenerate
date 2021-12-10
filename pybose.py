import click
from pathlib import Path

from app import current_location
from app import create_basic_config

@click.command()
@click.option('--path', '-p', default=current_location)
@click.option('--force', '-f', default=False)
@click.option('--virtual', '-v', default=True)
def main(path, force, virtual):
    create_basic_config(Path(path), force, virtual)


if __name__ == '__main__':
    main()