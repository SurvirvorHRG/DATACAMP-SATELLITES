# 1 - read in or download the data.
df_train = pd.read_csv(os.path.join('data', 'train.csv'))
df_test = pd.read_csv(os.path.join('data', 'test.csv'))

# 2 - Perform any data cleaning and split into private train/test subsets,
# if required. Neither steps required in this case.

# 3 - Split public train/test subsets. In this case the private training
# data will be used as the public data
df_public = df_train
df_public_train, df_public_test = train_test_split(
    df_public, test_size=0.2, random_state=57)
    # specify the random_state to ensure reproducibility
df_public_train.to_csv(os.path.join('data', 'public', 'train.csv'), index=False)
df_public_test.to_csv(os.path.join('data', 'public', 'test.csv'), index=False)