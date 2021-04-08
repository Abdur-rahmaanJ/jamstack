import os
from pathlib import Path
from jamstack.api.file import trycopytree

import click

package_folder = Path(__file__).parent.absolute()
sites_path = os.path.join(package_folder, 'sites')

@click.group(help="<Jamstack cli/>")
def cli():
    pass


@click.command(help="<Empty, plain repo/>")
@click.argument('project_name')
@click.option('--existing/--not-existing', default=False)
def plain(project_name, existing):
    path = '.'

    dirs_exist_ok = False
    if existing is True:
        dirs_exist_ok = True
    trycopytree(
        os.path.join(sites_path, 'plain'),
        os.path.join(path, project_name),
        dirs_exist_ok=dirs_exist_ok
        )


cli.add_command(plain)

def main():
    cli()

if __name__ == "__main__":
    cli()
