import pandas as pd

file1 = pd.read_csv('daily_sales_data_0.csv')
file2 = pd.read_csv('daily_sales_data_1.csv')
file3 = pd.read_csv('daily_sales_data_2.csv')

combined = pd.concat([file1, file2, file3])
target = 'pink morsel'
filtering_pink_morsel = combined[combined['product'] == target].copy()

# Use .loc for assignment to avoid SettingWithCopyWarning
filtering_pink_morsel.loc[:, 'price'] = filtering_pink_morsel['price'].replace({'\$': ''}, regex=True).astype(float)

# Use .loc for assignment to avoid SettingWithCopyWarning
filtering_pink_morsel.loc[:, 'sales'] = filtering_pink_morsel['price'] * filtering_pink_morsel['quantity']
filtering_pink_morsel = filtering_pink_morsel.drop(['price', 'quantity', 'product'], axis=1)

# Use apply to round each element of the 'sales' column individually
filtering_pink_morsel['sales'] = filtering_pink_morsel['sales'].apply(lambda x: '${:.2f}'.format(x))

output_file = 'output.csv'
filtering_pink_morsel.to_csv(output_file, index=False)
