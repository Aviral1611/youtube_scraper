import pandas as pd

def save_to_csv(data, filename="output.csv"):
    df = pd.DataFrame(data)
    # Ensure captions are sanitized (remove any extra whitespace or line breaks)
    if "Caption Text" in df.columns:
        df["Caption Text"] = df["Caption Text"].str.replace("\n", " ").str.strip()
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
