import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
            
if __name__ == "__main__" :

    parser = argparse.ArgumentParser()
    parser.add_argument("--result", required = True, help = "result file, usually result.csv in ../../tmp/")
    parser.add_argument("--verbose", action='store_true')
    args = parser.parse_args()
    arguments = args.__dict__
    
    result_file = arguments.pop("result")
    
    nutriments_list = ["energy", "protein", "carbohydrate", "sugar", "salt", "fat", "saturated_fat", "fiber"]
    
    df = pd.read_csv(result_file, sep = ";")
   
### Error repartition per nutrient    
    
    df_result = pd.DataFrame(index = nutriments_list, columns = ["correct", "incorrect", "not predicted", "not specified"]).fillna(0)

    for index, row in df.iterrows():
        if row["ground_truth"] == -1 :
            df_result["not specified"][row["nutriment"]] += 1
        elif row["predicted"] == -1 :
            df_result["not predicted"][row["nutriment"]] += 1
        else :              
            if row["ground_truth"] == row["predicted"] :
                df_result["correct"][row["nutriment"]] += 1
            else :
                df_result["incorrect"][row["nutriment"]] += 1
                
    
    df_result.plot.bar(stacked = True).legend()
    plt.show()

### metrics
    
    for nutriment in df_result.index.tolist():
        print(nutriment + ": Detectabilite : "+str(round((df_result.loc[nutriment].correct+df_result.loc[nutriment].incorrect)/(df_result.loc[nutriment]["not predicted"]+df_result.loc[nutriment].correct+df_result.loc[nutriment].incorrect), 2))+",  Accuracy :"+str(round((df_result.loc[nutriment].correct)/(df_result.loc[nutriment].correct+df_result.loc[nutriment].incorrect), 2)))