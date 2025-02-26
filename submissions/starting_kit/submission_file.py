
import numpy as np
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor


class RF_regressor(RandomForestRegressor):
    def fit(self, X, y):
        return super().fit(X, y)


cols = [
    "CCSDS_OMM_VERS", "MEAN_MOTION", "ECCENTRICITY", "INCLINATION", 
    "RA_OF_ASC_NODE", "ARG_OF_PERICENTER", "MEAN_ANOMALY", "EPHEMERIS_TYPE",
    "NORAD_CAT_ID", "ELEMENT_SET_NO", "REV_AT_EPOCH", "BSTAR", 
    "MEAN_MOTION_DOT", "MEAN_MOTION_DDOT", "SEMIMAJOR_AXIS", "PERIOD",
    "APOAPSIS", "PERIAPSIS", "GP_ID"
]

transformer = make_column_transformer(
    ('passthrough', cols)
)

pipe = make_pipeline(
    transformer,
    RF_regressor(n_estimators=10)
)


def get_estimator():
    return pipe