import pandas as pd
import numpy as np

# إنشاء بيانات وهمية لموظفين ومبيعاتهم
np.random.seed(42)
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 30, np.nan, 45, 22, 150, 38, np.nan],  # يحتوي قيم مفقودة وقيمة شاذة (150)
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', None],  # بيانات نصية ومفقودة
    'Salary': [50000, 60000, 55000, 80000, 48000, 120000, 75000, 62000],
    'Experience_Years': [2, 5, 3, 15, 1, 20, 10, 7],
    'Target_Met': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)
df.to_csv('raw_data.csv', index=False)
print("تم إنشاء ملف raw_data.csv بنجاح!")