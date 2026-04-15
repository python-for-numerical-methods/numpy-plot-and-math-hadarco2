import numpy as np

def normalized_array(input_array):
    arr = np.asarray(input_array, dtype=float)  # מבטיח עבודה עם NumPy ו־float
    min_val = arr.min()
    max_val = arr.max()
    
    # מקרה קצה: כל הערכים שווים
    if max_val == min_val:
        return np.zeros_like(arr)
    
    # נרמול וקטורי
    new_array = (arr - min_val) / (max_val - min_val)
    return new_array
    # חשוב לזכור להחליף את pass ב- return

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
