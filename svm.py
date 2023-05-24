import pandas as pd
import sklearn
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC

df = pd.read_csv('final_merged_file_categorized_outliers.csv')

X = df[['SCHEDULED_DEPARTURE', 'DESTINATION_WCODE', 'ORIGIN_WCODE' ,'SCHEDULED_ARRIVAL' ,'DESTINATION_PRECIPITATION_HOURS' ,'ORIGIN_PRECIPITATION_HOURS','DESTINATION_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDSPEED_10M_MAX'  ,'DESTINATION_WINDSPEED_10M_MAX' ,'ORIGIN_WINDDIRECTION_10M_DOMINANT_10M_MAX'  ,'ORIGIN_STATE' ,'DESTINATION_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_TEMPERATURE_2M_MAX' ,'DESTINATION_TEMPERATURE_2M_MAX' ,'ORIGIN_AIRPORT_NAME' ,'DESTINATION_APPARENT_TEMPERATURE_MAX' ,'DAY' ,'FIRST_FLIGHT' ,'MONTH' ,'TYPE' ]] # select the features for prediction
y = df['ARRIVAL_DELAY_CATEGORY'] # select the target variable


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, stratify=y_train)  # 0.25 x 0.8 = 0.2

param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
    'degree': [2, 3, 4],
    'gamma': ['scale', 'auto']
}

svm_clf = SVC(kernel='linear')


# Initialize GridSearchCV
# grid_search = GridSearchCV(estimator=svm_clf, param_grid=param_grid, cv=5, n_jobs=-1)
#
# # Train the model using GridSearchCV
# grid_search.fit(X_val, y_val)
#
# # Print the best hyperparameters
# print(grid_search.best_params_)

# Test the model using the best hyperparameters
# svm_clf = SVC(**grid_search.best_params_)
# svm_clf.fit(X_train, y_train)
# y_pred = svm_clf.predict(X_test)


# Train the SVM classifier on the training data
svm_clf.fit(X_train, y_train)

# Use the trained SVM classifier to make predictions on the test data
y_pred = svm_clf.predict(X_test)

# Evaluate the performance of the algorithm using accuracy score
print("Accuracy:", accuracy_score(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)


TP = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TN = cm[1][1]

Recall = TP / (TP + FN)
Precision = TP / (TP + FP)

f_measure = (2 * Precision * Recall) / (Precision + Recall)

Recall1 = sklearn.metrics.recall_score(y_test, y_pred, average='weighted')

Precision1 = sklearn.metrics.precision_score(y_test, y_pred, average='weighted')

f1 = f1_score(y_test, y_pred, average='weighted')

# print("Recall: ", Recall)
# print("Precision: ", Precision)
# print("F-measure:", f_measure)

print("F: ", f1)
print("Recall: ", Recall1)
print("Precision: ", Precision1)