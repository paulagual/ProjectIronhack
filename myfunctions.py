# My functions
def desc_num(x, bins=100, name='column'):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import math
    '''
    Describe numerical vars and draw histogram and boxplot
    input= dataframe column, num of bins and name of the column
    outut= describe of the column values, histogram and boxplot
    '''
    null = x.isnull().sum()
    print("Numbers of Nulls: ", null)
    descript = x.describe()
    print("The description of this variable is:\n", descript)
    dist = x.hist(bins=bins).set_title(f'Histogram of {name} with bins={bins}')
    plt.show()

    box = sns.boxplot(x=x).set_title(f'Boxplot of {name}')
    plt.show()
    
    
def desc_cat(df,col, name='column'):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import math
    '''
    Describe categorical vars and draw bar chart
    input= dataframe column
    outut= describe of the column values, bar chart
    '''
    null = df[col].isnull().sum()
    print("Numbers of Nulls: ", null)
    values =  df[col].value_counts()
    print(values)
    plt.subplots(figsize=(10, 6))
    bar = df.groupby(col)['fullVisitorId'].count().reset_index()
    bar.columns = [col,'count']
    sns.barplot(x=col, y='count', data=bar)
    plt.title(f'Bar chart {name}')
    plt.xticks(rotation=90)
    plt.show()