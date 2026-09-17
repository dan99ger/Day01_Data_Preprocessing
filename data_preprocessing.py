import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def clean_and_preprocess(file_path):
    # 1. تحميل البيانات
    df = pd.read_csv(file_path)
    print("--- البيانات الأولية ---")
    print(df)
    
    # 2. معالجة القيم الشاذة (Outliers) في العمر
    # استبدال أي عمر غير منطقي (> 100) بقيمة مفقودة لتتولى الخوارزمية معالجته
    df.loc[df['Age'] > 100, 'Age'] = np.nan

    # 3. فصل الخصائص (Features) عن الهدف (Target)
    X = df.drop(columns=['Employee_ID', 'Target_Met'])
    y = df['Target_Met'].map({'Yes': 1, 'No': 0})  # ترميز ثنائي للهدف

    # 4. تحديد الأعمدة الرقمية والنصية
    num_cols = ['Age', 'Salary', 'Experience_Years']
    cat_cols = ['Department']

    # 5. بناء معالجة الأعمدة الرقمية (المعالجة بالوسط الحسابي + التحجيم القياسي)
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # 6. بناء معالجة الأعمدة النصية (معالجة بالمنوال + الترميز الأحادي One-Hot)
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # 7. دمج الأنابيب عبر ColumnTransformer
    preprocessor = ColumnTransformer(transformers=[
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ])

    # 8. تطبيق المعالجة
    X_processed = preprocessor.fit_transform(X)
    
    # الحصول على أسماء الأعمدة الجديدة بعد الترميز
    cat_encoder = preprocessor.named_transformers_['cat'].named_steps['encoder']
    encoded_cat_cols = cat_encoder.get_feature_names_out(cat_cols).tolist()
    all_feature_names = num_cols + encoded_cat_cols

    # تحويل الناتج إلى DataFrame نظيف
    df_clean = pd.DataFrame(X_processed, columns=all_feature_names)
    df_clean['Target'] = y.values

    print("\n--- البيانات بعد التنظيف والتحويل ---")
    print(df_clean)

    # 9. حفظ البيانات المعالجة
    df_clean.to_csv('processed_data.csv', index=False)
    print("\nتم حفظ البيانات المعالجة في processed_data.csv")

if __name__ == '__main__':
    clean_and_preprocess('raw_data.csv')