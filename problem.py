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
_target_column_name = 'DECAY'  # Target variable to predict (date of decay)
_ignore_column_names = ['OBJECT_ID', 'OBJECT_NAME', 'NORAD_CAT_ID', 'LAUNCH']  # Identifiers, not useful for modeling

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
    rw.score_types.MAE(name='mae', precision=4)  # Mean Absolute Error
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
    
    # Extract target variable (convert DECAY date to number of days since launch)
    y_array = (pd.to_datetime(df[_target_column_name]) - pd.to_datetime(df['LAUNCH'])).dt.days.values

    # Drop unused columns
    X_df = df.drop(columns=[_target_column_name] + _ignore_column_names)

    return X_df, y_array

def get_train_data(path='.'):
    return _read_data(path, 'train.csv')

def get_test_data(path='.'):
    return _read_data(path, 'test.csv')