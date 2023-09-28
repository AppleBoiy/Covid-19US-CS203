import os
import requests
import pandas as pd
import path


def fips_csv():
    file = 'country_fips.csv'
    data_folder = path.data()
    return os.path.join(data_folder, file)


def create_fips_csv():
    url = "https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*"
    with requests.get(url, timeout=10) as response:
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data[1:], columns=data[0])
            df.to_csv(fips_csv(), index=False)

            print(df.head())
        else:
            print(f"Error: {response.status_code}")


def get_fips(name):
    df = pd.read_csv(fips_csv())
    try:
        fips = df[df['NAME'] == name]
        return fips
    except IndexError:
        print(f'Error: {name} not found')
        return None


def get_data(file=None) -> pd.DataFrame:
    if file is None:
        file: str = fips_csv()
    df = pd.read_csv(file)
    return df


def sample():
    df = pd.read_csv(fips_csv())
    print(df.head())


if __name__ == '__main__':
    create_fips_csv()
