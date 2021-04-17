def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="john", age=25)


"""
def post(url, data=None, json=None, **kwargs):  --> essa função é chamada apenas para que a proxima função seja possivel
    return request('post', url, data=None, json=None, **kwargs) ---> acrescente 'post', para chamar a função request()
"""