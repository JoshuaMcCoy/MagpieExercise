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
    
    # Group by skill and calculate count and mean
    grouped = df_scores.groupby("skill").agg(
        count=("score", "count"),
        score_average=("score", "mean")
    ).reset_index()
    
    # Sort by skill ascending
    grouped = grouped.sort_values(by="skill", ascending=True)
    grouped.to_csv(output_csv, index=False)
    print(f"Scores results saved to {output_csv}")


    #-----------------------------------------------------begin visualization
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    grouped['skill_numeric'] = pd.factorize(grouped['skill'])[0]
    ax.scatter(grouped['skill_numeric'], grouped['count'], grouped['score_average'], c='b', marker='o')
    
    plt.savefig(output_image)
    print(f"Visualization saved to {output_image}")

create_scores_results(
        "scores.json",
        "skills.json",
        "results/scores-results.csv",
        "results/scores-visualization-results.png"
    )