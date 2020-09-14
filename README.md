# Stanford AI Module Notes

## Setup

Use python3 by default
```bash
sudo ln -sf /usr/bin/python3 /usr/bin/python
```


### Conda Setup
```bash
conda env create --file environment.yml
conda env create --file environment.yml --force  # if env already exists
conda activate stanford-ai

conda deactivate
conda env remove -n stanford-ai
```

## Installing Conda Packages
```bash
conda install -c conda-forge matplotlib
```
