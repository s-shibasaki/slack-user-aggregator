# slack-user-aggregator

## Usage

### Prerequisites

Before using the aggregator script, ensure that you have the following installed:

- Python (3.6 or higher)
- Click (install via `pip install click`)
- Pandas (install via `pip install pandas`)

### Running the Aggregator Script

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/s-shibasaki/slack-user-aggregator.git
    cd slack-user-aggregator
    ```

2. Open a terminal and navigate to the project directory.

3. Run the aggregator script using the following command:

    ```bash
    python aggregator.py --input-dir /path/to/input/directory --output-dir /path/to/output/directory
    ```

    - `--input-dir`: Path to the directory containing CSV files to be aggregated.
    - `--output-dir` (optional): Path to the directory where the aggregated output will be saved. If not provided, the script will save the output in the same directory as the input.

4. Example:

    ```bash
    python aggregator.py --input-dir data/csv_files --output-dir output
    ```

### Notes

- Ensure that the input directory (`--input-dir`) contains CSV files for aggregation. The script will ignore files ending with "aggregator_output.csv".
- If the `--output-dir` option is not set, the script will save the aggregated output in the same directory as the input.
- The aggregated output will be saved as "aggregator_output.csv" in the specified or default output directory.
