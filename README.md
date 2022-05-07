# Web scrape the local election results for Leeds 2019 into a csv format

These results will be published on datamillnorth in 2 weeks but before then you can use this jupyter notebook to either scrape them yourself or simply download the pre-scraped .csv.

Vote shares are included and calculated.

## Set up

To set up this notebook and run it you'll need a couple of things:
- An installation of the [conda package management](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) system
- An installation of chrome
- An installation of [chromedriver](https://chromedriver.chromium.org/downloads) that should be installed into the `tools` subdirectory of this repo

With these tools you next need to create a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) with the following steps using a shell:

```bash
$ cd leeds-localelc-scraper

$ conda env create -f environment.yml
```

To use the notebook you need to activate the environment and start jupyter lab:

```bash
$ conda activate nb-scraper

$ jupyter lab
```

## The data

The data is available from within the [`data/`](https://github.com/Sparrow0hawk/Leeds-localelc-scraper/tree/main/data) directory.
