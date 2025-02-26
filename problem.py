import os
import pandas as pd
import rampwf as rw
from sklearn.model_selection import ShuffleSplit

# -----------------------
# Problem title
# -----------------------
problem_title = 'Satellite decay date prediction'

# -----------------------
# Define target variable and ignored columns
# -----------------------
_target_column_name = 'DECAY_DATE'  # Target variable to predict (date of decay)
# _ignore_column_names = ['OBJECT_ID', 'OBJECT_NAME', 'NORAD_CAT_ID', 'TLE_LINE0', 'TLE_LINE1', 'TLE_LINE2']  # Identifiers and non-structured features

# -----------------------
# Define prediction type (Regression)
# -----------------------
Predictions = rw.prediction_types.make_regression()

# -----------------------
# Define workflow
# -----------------------
workflow = rw.workflows.Estimator()

# -----------------------
# Define scoring metrics
# -----------------------
score_types = [
    rw.score_types.RMSE(name='rmse', precision=4)  # Root Mean Squared Error
]


# -----------------------
# Cross-validation strategy
# -----------------------
def get_cv(X, y):
    """ Use ShuffleSplit for cross-validation """
    cv = ShuffleSplit(n_splits=8, test_size=0.2, random_state=42)
    return cv.split(X, y)

# -----------------------
# Data reading functions
# -----------------------
def _read_data(path, filename):
    """ Helper function to read and process CSV data """
    df = pd.read_csv(os.path.join(path, 'data', filename))
    
    # Convert DECAY_DATE and LAUNCH_DATE to datetime format
    df['DECAY_DATE'] = pd.to_datetime(df['DECAY_DATE'], errors='coerce')
    df['LAUNCH_DATE'] = pd.to_datetime(df['LAUNCH_DATE'], errors='coerce')
    
    # Extract target variable (convert DECAY_DATE to number of days since launch)
    y_array = (df['DECAY_DATE'] - df['LAUNCH_DATE']).dt.days.values
    
    # Garde toutes les colonnes, y compris LAUNCH_DATE
    X_df = df.drop(columns=[_target_column_name])
    
    # Handle missing values in target
    valid_idx = ~pd.isna(y_array)
    return X_df.loc[valid_idx], y_array[valid_idx]


def get_train_data(path='.'):
    return _read_data(path, 'train.csv')


def get_test_data(path='.'):
    return _read_data(path, 'test.csv')
