import json
import pandas as pd

# Task 1: Create a CSV with ordered data
def create_time_series_results(input_file, output_file):
        
    with open(input_file, 'r') as file:
        data = json.load(file)
        scores = data['scores']
        df = pd.DataFrame(scores)
        df = df.sort_values(by="timestamp")
        df.to_csv(output_file, index=False)
    print(f"Time-series results saved to {output_file}")

create_time_series_results('scores.json', 'time-series-results.csv')


