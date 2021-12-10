import click
from pathlib import Path

from app import current_location
from app import create_basic_config

@click.command()
@click.option('--path', '-p', default=current_location)
@click.option('--force', '-f', default=False)
def main(path, force):
    create_basic_config(Path(path), force)


if __name__ == '__main__':
    main()