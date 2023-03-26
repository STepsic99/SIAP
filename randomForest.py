# Instantiate model with 1000 decision trees
import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('final_merged_file_categorized.csv')

X = df[['SCHEDULED_DEPARTURE', 'DESTINATION_WCODE', 'ORIGIN_WCODE' ,'SCHEDULED_ARRIVAL' ,'DESTINATION_PRECIPITATION_HOURS' ,'ORIGIN_PRECIPITATION_HOURS','DESTINATION_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDGUSTS_10M_MAX' ,'ORIGIN_WINDSPEED_10M_MAX'  ,'DESTINATION_WINDSPEED_10M_MAX' ,'ORIGIN_WINDDIRECTION_10M_DOMINANT_10M_MAX'  ,'ORIGIN_STATE' ,'DESTINATION_WINDDIRECTION_10M_DOMINANT_10M_MAX' ,'ORIGIN_TEMPERATURE_2M_MAX' ,'DESTINATION_TEMPERATURE_2M_MAX' ,'ORIGIN_AIRPORT_NAME' ,'DESTINATION_APPARENT_TEMPERATURE_MAX' ,'DAY' ,'FIRST_FLIGHT' ,'MONTH' ,'TYPE' ]] # select the features for prediction
y = df['ARRIVAL_DELAY_CATEGORY'] # select the target variable

for col in X:
    for val in X[col]:
        if np.isnan(val):
            print(val)
            print(col)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# # Train the model on training data
# rf.fit(X_train, y_train);
#
# # Use the forest's predict method on the test data
# predictions = rf.predict(X_test)
# # Calculate the absolute errors
# errors = abs(predictions - y_test)
# # Print out the mean absolute error (mae)
# print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
#
# # Calculate mean absolute percentage error (MAPE)
# mape = 100 * (errors / y_test)
# # Calculate and display accuracy
# accuracy = 100 - np.mean(mape)
# print('Accuracy:', round(accuracy, 2), '%.')

# Create a random forest classifier object
rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)

# Train the random forest classifier on the training data
rf.fit(X_train, y_train)

# Use the trained random forest classifier to make predictions on the test data
y_pred = rf.predict(X_test)

# Evaluate the performance of the algorithm using accuracy score
from sklearn.metrics import accuracy_score

print("Accuracy:", accuracy_score(y_test, y_pred))