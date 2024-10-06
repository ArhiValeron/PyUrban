
def apply_all_func(int_list, *functions):
    """
    Эта функция вызвает каждую функцию к переданному списку int_list
    Возвращать словарь, где ключом будет название вызванной функции,
     а значением - её результат работы со списком int_list.

    args:
    int_list - список из чисел (int, float)
    *functions - неограниченное
    кол-во функций (которые применимы к спискам, состоящим из чисел)

    returns:
    словарь, где ключом будет название вызванной функции,
    а значением - её результат работы со списком int_list
    """
    results = {}
    for function in functions:
        results.update({function.__name__: function(int_list)})
    return results


#######################################################################################
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))