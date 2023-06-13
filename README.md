## dbt project

This porject we are using dbt for the transformation pipeline.
For a more detail description of the pipeline you can look at the docs generate by dbt or directly by reading
the [owerview](models/overview.md)


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


## SETUP:


### Requirements

- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/downloads
- Gibash (on windows): https://gitforwindows.org/
- Gcloud: https://cloud.google.com/sdk/docs/install


### Clone the repo and setup python and dbt

- install python packages `pip install -r requirements.txt`

### Change the {name} in profiles.yml

```
dbt_intro_da:
  target: demo
  outputs:
    demo:
      type: bigquery
      method: oauth
      project: formation-sql-316408
      dataset: dbt_intro_da_{name}
      location: EU
      threads: 4

```

### Setup gcloud for oauth

- Download gcloud cli: https://cloud.google.com/sdk/docs/install?hl=fr
- unzip and install it (it comes with an install.sh script) more instruction on: https://cloud.google.com/sdk/docs/install?hl=fr
- connect to gcloud:
```
gcloud auth application-default login \
--scopes=https://www.googleapis.com/auth/bigquery,\
https://www.googleapis.com/auth/drive.readonly,\
https://www.googleapis.com/auth/iam.test

```

### DBT Setup and test

- `dbt debug` should now tell you everything is OK
- `dbt deps` to install dbt packages used in this project


### Using dbt

- `dbt run`
- `dbt docs generate` and` dbt docs serve` to get the project documentation



