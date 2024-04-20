from sklearn.ensemble import RandomForestClassifier
import random
import csv
import numpy as np
import pickle

counter = 0

with open('distance_all.csv', 'r') as file:
	reader = csv.reader(file)
	data = list(reader)

total_l = len(data)
random.shuffle(data)

split_index = int(total_l * 0.8)

#a_train = data[:split_index]
#a_test = data[split_index:]

#train_l = int(total_l * 0.8)
#a_train = random.sample(data, train_l)
y_train = [row[0] for row in data]
x_train = [row[-8:] for row in data]

#test_l = int(total_l * 0.2)
#a_test = random.sample(data, test_l)
#y_test = [row[0] for row in a_test]
#x_test = [row[-8:] for row in a_test]

clf = RandomForestClassifier(n_estimators=100, random_state=42)

clf.fit(x_train, y_train)

#with open("Random_forest_model.pkl", 'wb') as file:
#	pickle.dump(clf, file)
#
#y_pred = clf.predict(x_test)
#
#errors = np.array([])
#for i in range(len(y_test)):
#	print("Prediction is : " + y_pred[i])
#	print("Actual is : " + y_test[i])
#	errors = np.append(errors, abs(int(y_test[i]) - int(y_pred[i])))
#erreur = np.mean(errors)
#print(erreur)
