![aidkit](https://www.neurocat.ai/wp-content/uploads/2018/11/addkit-hori.png)

aidkit is the quality gate between machine learning models and the deployment of those models.

## Installation

1. Activate your virtual environment with python 3.6, e.g. `source venv/bin/activate`
1. `pip install aidkit`

## Example Usage

### Authenticate

The only requirement for using aidkit is having a license for it.

To authenticate, you need to run the following once:
```bash
python -m aidkit.authenticate --url <subdomain>.aidkit.ai --token <your auth token>
```

### Model
You can upload a model to aidkit, or list the names of all models 
uploaded.

For uploading, you need a keras .h5 file, that contains a LSTM
architecture. Do the following to upload it:
```bash
python -m aidkit.model --file <path to your h5 file>
```

To list all uploaded models type:
```bash
python -m aidkit.model
```

### Data
You can upload a data set to aidkit, or list the names of all datasets
uploaded.

For uploading, you need a zip file. 
We expect a zip, containing a folder, that is named like the dataset 
should be called. This subfolder contains INPUT and OUTPUT folders 
that each contain csv files. Do the following to upload it:
```bash
python -m aidkit.data --file <path to your zip file>
```

To list all uploaded datasets type:
```bash
python -m aidkit.data
```

### Analysis

You can start a new quality analysis. For doing so, you need a toml file. 
This file will follow a specified toml standard. Do the following to upload it:
```bash
python -m aidkit.analysis --file <path to your toml file>
```

To list all uploaded datasets type:
```bash
python -m aidkit.analysis
```

### Visualization

After running an analysis you can observe the results in our web-GUI. to get the link type:

```bash
python -m aidkit.url
```

Just follow the link and authorize yourself with your credentials.