from flask import Flask
import time, faker, csv, random, itertools, seaborn, math

app = Flask(__name__)
fake = faker.Faker()

def gen_categories_list():
    # Generate categories
    with open("categories.csv") as file:
        categories = list(csv.DictReader(file))

    # Generate a barcode param for each category that represent the probability of having a barcode in this category
    random.seed(0)
    for cat in categories:
        cat["barcode_ean13_param"] = random.random()
    return categories

def gen_sample_data(categories):
    sample = []
    for _ in range(100):
        for cat in random.sample(categories, len(categories)//20):
            for _ in range(1 + int(100 * math.exp(-10*cat["barcode_ean13_param"]))):
                sample.append({
                    "product_category": cat["product_category"],
                    "pdt_SUB_CATEGORY": cat["pdt_SUB_CATEGORY"],
                    "barcode_ean13": fake.ean13(),
                    "CA": round(1 + random.random()*50, 2),
                    "date": str(fake.date_this_year()),
                    "grp": random.choice([None, "hyp", "sup", "prx"]),
                })
    return sample

CATEGORIES = gen_categories_list()
DATA = gen_sample_data(CATEGORIES)

LAST_GET_TIME = time.time()


@app.route("/crf_sales_group_data.csv")
def all_sales():
    global LAST_GET_TIME, DATA
    if time.time() - LAST_GET_TIME > 10:
        # add new data
        DATA += gen_sample_data(CATEGORIES)
        # duplicate 10% of the data randomly
        DATA += random.sample(DATA, len(DATA)//10)
        #remove 10% of the data randomly
        DATA = random.sample(DATA, len(DATA) - len(DATA)//10)
        # change CA to None for 10% of the data randomly
        for row in random.sample(DATA, len(DATA)//10):
            row["CA"] = None
        # change date to None for 10% of the data randomly
        for row in random.sample(DATA, len(DATA)//10):
            row["date"] = None
        # change CA to ramdom value for 10% of the data randomly
        for row in random.sample(DATA, len(DATA)//10):
            row["CA"] = round(1 + random.random()*50, 2)
        # change date to ramdom value for 10% of the data randomly
        for row in random.sample(DATA, len(DATA)//10):
            row["date"] = str(fake.date_this_year())
    LAST_GET_TIME = time.time()
    cols = [col for col in DATA[0].keys() if col != "grp"]
    data_list = []
    for row in DATA:
        data_list.append(",".join(str(row[col]) for col in cols))
    return "\n".join(data_list)

@app.route("/crf_<grp>_sales_fr_data.csv")
def grp_sales(grp):
    global LAST_GET_TIME
    LAST_GET_TIME = time.time()
    cols = [col for col in DATA[0].keys() if col != "grp"]
    data_list = []
    for row in DATA:
        if row["grp"] == grp:
            data_list.append(",".join(str(row[col]) for col in cols))
    return "\n".join(data_list)
