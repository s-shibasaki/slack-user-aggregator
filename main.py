import glob
import os

import click
import pandas as pd


@click.command()
@click.option("--input-dir")
@click.option("--output-dir")
def main(input_dir: str, output_dir: str = None):
    print(input_dir)
    if output_dir is None:
        print("Argument `output_dir` is not set, we will save to `input_dir`.")
        output_dir = input_dir
    files = glob.glob(os.path.join(input_dir, "*.csv"))
    files = list(filter(lambda x: not x.endswith("aggregator_output.csv"), files))
    print("Merging the files below...")
    for file in files:
        print(f"  - {file}")
    print("")
    df_list = []
    for path in files:
        df = pd.read_csv(path)
        df = df[~df.status.isin(["Bot", "Deactivated"])]
        df["workspace"] = "-".join(os.path.basename(path).split("-")[1:-1])[:-13]
        df_list.append(df)
    df = pd.concat(df_list, ignore_index=True)
    df = df.groupby("userid").agg(
        lambda x: " / ".join(x.fillna("").astype("str").unique())
    )
    df.to_csv(os.path.join(output_dir, "aggregator_output.csv"))


if __name__ == "__main__":
    main()
