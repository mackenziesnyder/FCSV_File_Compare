from sklearn.metrics import mean_squared_error 
import pandas as pd

# compute the mean squared error between 2 fcsv
def compute_mse(t1w_fcsv, t2w_fcsv):
    
    # read the data
    read_t1w_fcsv = pd.read_csv(t1w_fcsv)
    read_t2w_fcsv = pd.read_csv(t2w_fcsv)

    # mean_squared_error function
    mse = mean_squared_error(read_t1w_fcsv , read_t2w_fcsv)
    
    return mse

if __name__ == "__main__":
    
    # File paths to fcsv files outputted from autoafids 
    t1w_fcsv = "data/"
    t2w_fcsv = "data/"

    try:
        # Calculate mse
        mse = compute_mse(t1w_fcsv, t2w_fcsv)

        print(f"mse: {mse:.4f}")
    except Exception as e:
        print(f"Error: {e}")