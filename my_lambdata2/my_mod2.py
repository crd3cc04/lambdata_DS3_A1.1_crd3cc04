
def wk_birthday(X):
    X['Year']= X['wk_birthday'].dt.year
    X['Month']= X['wk_birthday'].dt.month
    X['Day']= X['wk_birthday'].dt.day 
    return X