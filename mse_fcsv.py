from sklearn.metrics import mean_squared_error 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# compute the mean squared error between 2 fcsv
def compute_mse(t1w_fcsv, t2w_fcsv):
    
    # read the data, skipping the first 2 lines (headers and metadata)
    t1w_data = pd.read_csv(t1w_fcsv, comment='#', header=None)
    t2w_data = pd.read_csv(t2w_fcsv, comment='#', header=None)
    
    # extract the columns for coordinates (x, y, z) from both files (columns 1, 2, 3)
    t1w_coords = t1w_data.iloc[:, 1:4].values
    t2w_coords = t2w_data.iloc[:, 1:4].values
    
    # make sure the files are the same shape
    if t1w_coords.shape != t2w_coords.shape:
        raise ValueError("The files have a different number of points. MSE computation requires equal data points.")
    
    # calculate the MSE for each coordinate (x, y, z)
    mse_x = np.mean((t1w_coords[:, 0] - t2w_coords[:, 0]) ** 2)
    mse_y = np.mean((t1w_coords[:, 1] - t2w_coords[:, 1]) ** 2)
    mse_z = np.mean((t1w_coords[:, 2] - t2w_coords[:, 2]) ** 2)
    
    # print mse for each coord
    print("mse_x: ", mse_x)
    print("mse_y: ", mse_y)
    print("mse_z: ", mse_z)

    # Create a bar plot to visualize the MSE for each coordinate
    mse_values = [mse_x, mse_y, mse_z]
    coordinates = ['X', 'Y', 'Z']

    plt.bar(coordinates, mse_values, color=['r', 'g', 'b'])
    plt.xlabel('Coordinate')
    plt.ylabel('MSE')
    plt.title('MSE for Each Coordinate (X, Y, Z)')
    plt.show()

    # compute total mse
    mse = mean_squared_error(t1w_coords, t2w_coords)
    
    return mse

if __name__ == "__main__":
    
    # File paths to fcsv files outputted from autoafids 
    t1w_fcsv = "data/t1w_fcsv.fcsv"
    t2w_fcsv = "data/t2w_fcsv.fcsv"

    try:
        # Calculate mse
        mse = compute_mse(t1w_fcsv, t2w_fcsv)

        print(f"mse: {mse:.4f}")
    except Exception as e:
        print(f"Error: {e}")