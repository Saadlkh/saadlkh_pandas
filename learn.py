import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# تحميل البيانات من ملف CSV
data = pd.read_csv("test.csv")

# تعيين المدخلات والأهداف
X = data[['heur', 'exam']]
y = data["result"]

# تقسيم البيانات إلى مجموعة تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# إنشاء نموذج الانحدار اللوجستي
model = LogisticRegression(max_iter=600)
model.fit(X_train, y_train)

# التنبؤ على مجموعة الاختبار وحساب الدقة
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# أخذ مدخلات جديدة من المستخدم
value1 = float(input("Enter heur value: "))  # تحويل المدخل إلى float
value2 = float(input("Enter exam value: "))   # تحويل المدخل إلى float

# إنشاء بيانات جديدة للتنبؤ
new_data = np.array([[value1, value2]])

# التنبؤ بالنتيجة الجديدة
prediction = model.predict(new_data)
print(f"Prediction: {prediction[0]}")  # طباعة النتيجة