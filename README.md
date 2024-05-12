# Scrape Leeds Local Election results page

A CLI tool to scrape the [Leeds Local Election results page](https://www.leeds.gov.uk/your-council/elections/leeds-city-council-election-results).
Data is published as a tabular file on Data Mill North 2 weeks after the result, but in the meantime you can use
this tool to extract the data.

The structure of the final file is aimed to roughly align with the format of the file shared on Data Mill North.R

## Set up
- Python 3.12
- GNU Make

1. Create virtual environment
   ```bash
   python3.12 -m venv --prompt . .venv
   ```
2. Install project dependencies
   ```bash
   # activate virtual environment
   . .venv/bin/activate
   
   # install dependencies including dev dependencies
   pip install .[dev]
   ```
3. Run tests
   ```bash
   make test
   ```
4. Run CLI 
   ```bash
   election_scraper --url https://www.leeds.gov.uk/your-council/elections/leeds-city-council-election-results
   ```
   This writes the data to a `results.csv` file in your current directory.

## The data

The data is available from within the [`data/`](https://github.com/Sparrow0hawk/Leeds-localelc-scraper/tree/main/data) directory.
