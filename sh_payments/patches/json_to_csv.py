import os

import pandas as pd


def json_to_csv(json_file_path, output_csv_path):
    """
    Reads a JSON file, extracts specified columns, and saves them to a CSV file.

    Args:
        json_file_path (str): The path to the input JSON file.
        output_csv_path (str): The path for the output CSV file.
        columns_to_extract (list): A list of column names (keys) to extract from the JSON data.
    """
    column_mapping = {
        "GSTMASTERDISPNAME": "product_name",
        "GSTRATEIGSTRATE": "gst",
        "HSNSACCODE": "hsn_code",
    }
    try:
        # Read the JSON file into a pandas DataFrame
        df = pd.read_json(json_file_path)

        # Select only the desired columns
        # df_selected = df[columns_to_extract]
        df_selected = df.rename(columns=column_mapping)[list(column_mapping.values())]
        df_selected["company"] = "Shree Agencies"
        # Write the selected data to a CSV file
        # index=False prevents pandas from writing the DataFrame index as a column in the CSV
        df_selected.to_csv(output_csv_path, index=False)

        print(
            f"Successfully extracted columns from '{json_file_path}' "
            f"and saved to '{output_csv_path}'."
        )

    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")
    except KeyError as e:
        print(f"Error: One or more specified columns not found in the JSON data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def update_csv(csv_file_path, company_name):
    try:
        df = pd.read_csv(csv_file_path)
        df["company"] = company_name
        df.to_csv(csv_file_path, index=False)
        print(
            f"Successfully add column 'company' with value {company_name} to '{csv_file_path}' "
        )
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "products_2.json")
    csv_file_path = os.path.join(os.path.dirname(__file__), "data", "saproducts_1.csv")
    json_to_csv(
        json_file_path,
        csv_file_path,
    )
    # update_csv(csv_file_path, "Shree Graphics")
