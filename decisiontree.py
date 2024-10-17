import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'StudyHours': [6, 8, 7, 5, 9, 10, 3, 2, 4, 12],
    'StudyGroup': ['A', 'B', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
    'HomeworkDone': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No'],
    'Pass': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

df['Pass'] = df['Pass'].map({'Yes': 1, 'No': 0})

def gini(subset):
    total = len(subset)
    if total == 0:
        return 0
    p = subset.mean()
    return 2 * p * (1 - p)

def weighted_gini(left, right):
    total = len(left) + len(right)
    return (len(left) / total) * gini(left) + (len(right) / total) * gini(right)

def evaluate_split(criteria, condition):
    if isinstance(condition, str):
        left_split = df[df[criteria] == condition]['Pass']
        right_split = df[df[criteria] != condition]['Pass']
    else:
        left_split = df[df[criteria] <= condition]['Pass']
        right_split = df[df[criteria] > condition]['Pass']
    
    return weighted_gini(left_split, right_split)

# Split criteria from Table 2
split_criteria = {
    'StudyHours <= 6': ('StudyHours', 6),
    'StudyHours <= 7': ('StudyHours', 7),
    'StudyHours <= 8': ('StudyHours', 8),
    'StudyGroup A': ('StudyGroup', 'A'),
    'StudyGroup B': ('StudyGroup', 'B'),
    'StudyGroup C': ('StudyGroup', 'C'),
    'HomeworkDone': ('HomeworkDone', 'Yes')
}

# Calculate Gini for each split
gini_results = {}
for criterion, (feature, threshold) in split_criteria.items():
    gini_value = evaluate_split(feature, threshold)
    gini_results[criterion] = gini_value

for criterion, gini_value in gini_results.items():
    print(f"Criterion: {criterion}, Weighted Gini: {gini_value:.4f}")

