import json
import pandas as pd
import matplotlib.pyplot as plt



# Task 2
def create_scores_results(scores_file, skills_file, output_csv, output_image):
    with open(scores_file, 'r') as f:
        scores_data = json.load(f)
    
    # Assuming scores_data is a list of dictionaries with "skill" and "score" fields
    df_scores = pd.DataFrame(scores_data['scores']) 
    df_scores['score'] = pd.to_numeric(df_scores['score'], errors='coerce') 
        #some scores are not numbers, I see 'cat' and null, ive decided to coerce them to NaN for now (not ideal)
    print(df_scores)
    

create_scores_results(
        "scores.json",
        "skills.json",
        "results/scores-results.csv",
        "results/scores-visualization-results.png"
    )