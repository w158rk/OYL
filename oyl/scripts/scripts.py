import click
from oyl.compiler import compile

def run_body(filename):
    warehouse = compile(filename)
    df_map = warehouse.to_df_map()
    return df_map

@click.group()
def cli():
    pass

@click.command()
@click.argument("filename")
def run(filename):
    df_map = run_body(filename)
    print(df_map)

cli.add_command(run)

def main():
    cli()

if __name__ == "__main__":
    main()

