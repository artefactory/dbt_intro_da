## SETUP:


### Requirements

- [Download and install Python](https://www.python.org/downloads/)
- [Download and install Git](https://git-scm.com/downloads)
- For windows: [Download and install windows terminal](https://learn.microsoft.com/en-us/windows/terminal/install)

### Get the code and install python environment

- Open a terminal
- Clone the repository: `git clone https://github.com/artefactory/dbt_intro_da.git`
- Change directory in the repository folder: `cd dbt_intro_da`
- Setup a python environment: `python -m venv .venv`
         <details>
              <summary> in case of error `zsh: command not found: python` </summary>     

              Providing you know Python is already installed on you device,
              run this command in Terminal / your C.L.I. (Command Line Interface)

                  echo "alias python=/usr/bin/python3" >> ~/.zshrc

              Then, fully restart your C.L.I.
              and run:
  
                  which python

              The result should be
  
                  python: aliased to /usr/bin/python3

              if you have python3.
              Rechange directory in the repository folder:

                  cd dbt_intro_da

              And setup your python environment with
  
                  python -m venv .venv
      
              You can proceed with the next steps.
  </details>     
- Activate python environment:
    - MacOs: `source .venv/bin/activate`
    - Windows:
      - `. .\.env\Scripts\activate`
      - `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force`
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

### Using dbt

- `dbt run`
- `dbt docs generate` and` dbt docs serve` to get the project documentation

### Checking the database

- duckdb: `duckdb dbt.duckdb -s "select * from local_sales;"`
- bigquery: check on bigquery

