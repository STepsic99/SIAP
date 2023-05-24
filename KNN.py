import pandas as pd
import sklearn
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('final_merged_file_categorized_outliers.csv')

X = df[
    ['SCHEDULED_DEPARTURE', 'DESTINATION_WCODE', 'ORIGIN_WCODE', 'SCHEDULED_ARRIVAL', 'DESTINATION_PRECIPITATION_HOURS',
     'ORIGIN_PRECIPITATION_HOURS', 'DESTINATION_WINDGUSTS_10M_MAX', 'ORIGIN_WINDGUSTS_10M_MAX',
     'ORIGIN_WINDSPEED_10M_MAX', 'DESTINATION_WINDSPEED_10M_MAX', 'ORIGIN_WINDDIRECTION_10M_DOMINANT_10M_MAX',
     'ORIGIN_STATE', 'DESTINATION_WINDDIRECTION_10M_DOMINANT_10M_MAX', 'ORIGIN_TEMPERATURE_2M_MAX',
     'DESTINATION_TEMPERATURE_2M_MAX', 'ORIGIN_AIRPORT_NAME', 'DESTINATION_APPARENT_TEMPERATURE_MAX', 'DAY',
     'FIRST_FLIGHT', 'MONTH', 'TYPE']]  # select the features for prediction
y = df['ARRIVAL_DELAY_CATEGORY']  # select the target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, stratify=y_train)  # 0.25 x 0.8 = 0.2

param_grid = {'n_neighbors': [3, 5, 7, 9], 'weights': ['uniform', 'distance']}

knn = KNeighborsClassifier()

grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, cv=5, n_jobs=-1)

# Train the model using GridSearchCV
grid_search.fit(X_val, y_val)

# Print the best hyperparameters
print(grid_search.best_params_)

knn = KNeighborsClassifier(**grid_search.best_params_)
clf = knn.fit(X_train, y_train)
y_pred = clf.predict(X_test)



# Train the KNN classifier on the training data
#knn.fit(X_train, y_train)

# Use the trained KNN classifier to make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the performance of the algorithm using accuracy score
print("Accuracy:", accuracy_score(y_test, y_pred))

f1 = f1_score(y_test, y_pred, average='weighted')

cm = confusion_matrix(y_test, y_pred)

print(cm)

TP = 0
FP = 0
TN = 0
FN = 0

TP = cm[0][0]
FN = cm[0][1]
FP = cm[1][0]
TN = cm[1][1]

Recall = TP / (TP + FN + cm[0][2])
Precision = TP / (TP + FP + cm[0][2])
ACCURACY = (cm[0][0] + cm[1][1] + cm[2][2])/(1269+5+188+1+118+3+1)

Recall1 = sklearn.metrics.recall_score(y_test, y_pred, average='weighted')

Precision1 = sklearn.metrics.precision_score(y_test, y_pred, average='weighted')

f_measure = (2 * Precision * Recall) / (Precision + Recall)

#print("Accuracy: ", ACCURACY)
#print("Recall: ", Recall)
print("Recall(original): ", Recall1)
#print("Precision: ", Precision)
print("Precision(orginal): ", Precision1)
print("F-measure(original):", f1)
#print("F-measure:", f_measure)
