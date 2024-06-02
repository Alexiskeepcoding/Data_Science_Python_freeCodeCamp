import numpy as np

def calculate(list):
    
    if(len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    

    array_np = np.array(list)
    print(array_np)
    
    mean_rows = ([array_np[[0,1,2]].mean(), array_np[[3,4,5]].mean(), array_np[[6,7,8]].mean()])
    mean_columns =([array_np[[0,3,6]].mean(), array_np[[1,4,7]].mean(), array_np[[2,5,8]].mean()])

    var_row = ([array_np[[0,1,2]].var(), array_np[[3,4,5]].var(), array_np[[6,7,8]].var()])
    var_columns =([array_np[[0,3,6]].var(), array_np[[1,4,7]].var(), array_np[[2,5,8]].var()])

    std_row = ([array_np[[0,1,2]].std(), array_np[[3,4,5]].std(), array_np[[6,7,8]].std()])
    std_columns =([array_np[[0,3,6]].std(), array_np[[1,4,7]].std(), array_np[[2,5,8]].std()])


    max_row = ([array_np[[0,1,2]].max(), array_np[[3,4,5]].max(), array_np[[6,7,8]].max()])
    max_columns =([array_np[[0,3,6]].max(), array_np[[1,4,7]].max(), array_np[[2,5,8]].max()])

    min_row = ([array_np[[0,1,2]].min(), array_np[[3,4,5]].min(), array_np[[6,7,8]].min()])
    min_columns =([array_np[[0,3,6]].min(), array_np[[1,4,7]].min(), array_np[[2,5,8]].min()])

    sum_row = ([array_np[[0,1,2]].sum(), array_np[[3,4,5]].sum(), array_np[[6,7,8]].sum()])
    sum_columns =([array_np[[0,3,6]].sum(), array_np[[1,4,7]].sum(), array_np[[2,5,8]].sum()])


    return {
        'mean': [mean_columns, mean_rows, array_np.mean()],
        'variance': [var_columns, var_row, array_np.var()],
        'standard deviation': [std_columns, std_row, array_np.std()],
        'max': [max_columns, max_row, array_np.max()],
        'min': [min_columns, min_row, array_np.min()],
        'sum': [sum_columns, sum_row, array_np.sum()]
    }