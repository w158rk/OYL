import click
from oyl.compiler import compile

@click.group()
def cli():
    pass

@click.command()
@click.argument("filename")
def run(filename):
    warehouse = compile(filename)
    df_map = warehouse.to_df_map()
    for k,v in df_map.items():
        print(k)
        print(v)

cli.add_command(run)

def main():
    cli()

if __name__ == "__main__":
    main()

