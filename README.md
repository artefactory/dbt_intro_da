## SETUP:


### Requirements

- [Download and install Python 3.11.x](https://www.python.org/downloads/release/python-3116/)
- [Download and install Git](https://git-scm.com/downloads)
- [Download and install Nodejs](https://nodejs.org/en/download)
- [Download and install VScode](https://code.visualstudio.com/download)
- For windows: [Download and install windows terminal](https://learn.microsoft.com/en-us/windows/terminal/install)

### Get the code and install python environment

- Open a terminal
- Clone the repository: `git clone https://github.com/artefactory/dbt_intro_da.git`
- Change directory in the repository folder: `cd dbt_intro_da`
- Setup a python environment: 
    - MacOs: `python3 -m venv .venv`
    - Windows: `python -m venv .venv`
- Activate python environment:
    - MacOs: `source .venv/bin/activate`
    - Windows:
      - `Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`
      - `. .\.env\Scripts\activate`
- Install python packages `pip install -r requirements.txt`

<details>
  <summary>Additionnal setup to work with bigquery (optionnal)</summary>

### Additionnal setup to work with bigquery (optionnal)

In order to work with bigquery you need to change the target in the profiles to the bigquery target.
You also need to update the dataset used in the profile by changing `name` to your name.

```
dbt_intro_da:
  target: dev_bigquery
  outputs:
    duckdb:
      path: dbt.duckdb
      type: duckdb
      threads: 4
    dev_bigquery:
      type: bigquery
      method: oauth
      project: formation-sql-316408
      dataset: dbt_intro_da_name
      location: EU
      threads: 4

```

- [Download and install Gcloud](https://cloud.google.com/sdk/docs/install)
- Connect to gcloud:
```
gcloud auth application-default login \
--scopes=https://www.googleapis.com/auth/bigquery,\
https://www.googleapis.com/auth/drive.readonly,\
https://www.googleapis.com/auth/iam.test

```

</details>


### DBT Setup and test

- `dbt debug` should now tell you everything is OK
- `dbt deps` to install dbt packages used in this project
- `dbt run`

The first `dbt run` should create a file named `dbt.duckdb`.
This file will contains all the tables views we are creating.

<details>
  <summary>VScode extension (optionnal but nice to have)</summary>

### VScode extension (optionnal but nice to have):

To help us navigate the dbt project we are using the extension dbt power user:
- Install the extension: https://marketplace.visualstudio.com/items?itemName=innoverio.vscode-dbt-power-user

There is one setting that should be added
- Go in settings
    - ![](./assets/vs_code_extensions/dbt_power_user/01_open_settings.png)
- Add `*.sql` in the field *Item* and `jinja-sql` in the *Value*
    - ![](./assets/vs_code_extensions/dbt_power_user/02_add_in_settings.png)
- Clicks on *run dbt SQL*
    - ![](./assets/vs_code_extensions/dbt_power_user/03_query_model.png)
- View lineage
    - ![](./assets/vs_code_extensions/dbt_power_user/04_view_lineage.png)

</details>
