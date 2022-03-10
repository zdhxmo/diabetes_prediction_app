import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from joblib import dump

df = pd.read_csv("./diabetes.csv")

# drop all columns that's not the following ones
df.drop(df.columns.difference(['Glucose', 'Insulin', 'BMI', 'Age', 'Outcome']), axis=1, inplace=True)

X = df.drop(columns='Outcome', axis=1)
y = df.Outcome

std_sc = StandardScaler()
features = df.columns.values[:-1]

# features
X = pd.DataFrame(std_sc.fit_transform(df.drop(["Outcome"], axis=1), ), columns=features)
# target
y = df.Outcome

dump(std_sc, "scaler.joblib")

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, stratify=y, random_state=2)

svc = SVC(random_state=100, kernel='linear', gamma=1, degree=3, C=0.5, class_weight='balanced')
svc.fit(X_train, y_train)

dump(svc, 'model.joblib')