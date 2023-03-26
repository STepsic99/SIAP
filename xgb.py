# evaluate xgboost algorithm for classification
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.model_selection import RepeatedStratifiedKFold
from xgboost import XGBClassifier
import pandas as pd


def model_training(X, y, n_trees, mdepth, gamma, lam):
    ##### Step 1 - Create training and testing samples
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    ##### Step 2 - Set model and its parameters
    model = XGBClassifier(use_label_encoder=False,
                          booster='gbtree',  # boosting algorithm to use, default gbtree, othera: gblinear, dart
                          n_estimators=n_trees,  # number of trees, default = 100
                          eta=0.3,  # this is learning rate, default = 0.3
                          max_depth=mdepth,  # maximum depth of the tree, default = 6
                          gamma=gamma,  # used for pruning, if gain < gamma the branch will be pruned, default = 0
                          reg_lambda=lam,  # regularization parameter, defautl = 1
                          # min_child_weight=0 # this refers to Cover which is also responsible for pruning if not set to 0
                          )

    # Fit the model
    clf = model.fit(X_train, y_train)

    ##### Step 3
    # Predict class labels on training data
    pred_labels_tr = model.predict(X_train)
    # Predict class labels on a test data
    pred_labels_te = model.predict(X_test)

    ##### Step 4 - Model summary
    # Basic info about the model
    print('*************** Tree Summary ***************')
    print('No. of classes: ', clf.n_classes_)
    print('Classes: ', clf.classes_)
    print('No. of features: ', clf.n_features_in_)
    print('No. of Estimators: ', clf.n_estimators)
    print('--------------------------------------------------------')
    print("")

    print('*************** Evaluation on Test Data ***************')
    score_te = model.score(X_test, y_test)
    print('Accuracy Score: ', score_te)
    # Look at classification report to evaluate the model
    print(classification_report(y_test, pred_labels_te))
    print('--------------------------------------------------------')
    print("")

    print('*************** Evaluation on Training Data ***************')
    score_tr = model.score(X_train, y_train)
    print('Accuracy Score: ', score_tr)
    # Look at classification report to evaluate the model
    print(classification_report(y_train, pred_labels_tr))
    print('--------------------------------------------------------')

    return clf, X_test, y_test


##### Step 5 - Select data for modelling and call the function to train the model

df = pd.read_csv('final_merged_file_categorized_outliers.csv')

X = df[['SEASON', 'SCHEDULED_DEPARTURE', 'DESTINATION_WCODE', 'ORIGIN_WCODE' ,'SCHEDULED_ARRIVAL' ,'DESTINATION_PRECIPITATION_HOURS' ,'ORIGIN_PRECIPITATION_HOURS','DESTINATION_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDSPEED_10M_MAX'  ,'DESTINATION_WINDSPEED_10M_MAX' ,'ORIGIN_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_STATE' ,'DESTINATION_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_TEMPERATURE_2M_MAX' ,'DESTINATION_TEMPERATURE_2M_MAX' ,'ORIGIN_AIRPORT_NAME' ,'DESTINATION_APPARENT_TEMPERATURE_MAX' ,'DAY' ,'FIRST_FLIGHT' ,'MONTH' ,'TYPE' ]] # select the features for prediction
y = df['ARRIVAL_DELAY_CATEGORY'] # select the target variable

# Train the model
clf, X_test, y_test = model_training(X, y, n_trees=500, mdepth=6, gamma=1, lam=1)