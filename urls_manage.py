def add_url(new_add):
    with open('urls.txt','a') as f:
        f.write(new_add)
        f.write('\n')

def print_all():
    with open('urls.txt') as f:
        my_list=f.read().splitlines()
        print('\n')
        for url in my_list:           
            print(url)

def delete_url(url_index):
    with open('urls.txt') as f:
        my_list=f.read().splitlines()

    del my_list[int(url_index)]
    with open('urls.txt','w') as f:
        for url in my_list:           
            f.write(url)
            f.write('\n')