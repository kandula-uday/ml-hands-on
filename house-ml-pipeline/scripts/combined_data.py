import os
import pandas as pd

def combine_area_wise_csvs(data_dir="../data", output_file="data/toronto_combined.csv"):
    all_dfs = []

    # Walk through all subfolders inside 'data/'
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".csv"):
                full_path = os.path.join(root, file)
                try:
                    df = pd.read_csv(full_path)
                    all_dfs.append(df)
                except Exception as e:
                    print(f"⚠️ Error reading {full_path}: {e}")

    # Combine all dataframes
    if not all_dfs:
        print("❌ No CSV files found.")
        return

    combined_df = pd.concat(all_dfs, ignore_index=True)

    # Remove duplicate rows
    combined_df.drop_duplicates(inplace=True)

    # Optional: reset index
    combined_df.reset_index(drop=True, inplace=True)

    # Save to single file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    combined_df.to_csv(output_file, index=False)
    print(f"✅ Combined CSV saved to {output_file}")


# ...existing code...

if __name__ == "__main__":
    combine_area_wise_csvs(
        data_dir="../data",
        output_file="../data/toronto_combined.csv"
    )