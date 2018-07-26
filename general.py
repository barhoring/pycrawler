import os

# each project you crawl is a different project/dir/file
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)



# create the queue and crawled files/ cache
def create_data_files(project_name, start):
    print('1')
    queue_path = project_name + '/queue.txt'
    crawled_path = project_name + '/crawled.txt'
    if not os.path.isfile(queue_path):
        write_file(queue_path, start)
    if not os.path.isfile(crawled_path):
        write_file(crawled_path, '')

def write_file(path, data):
    f = open(path,'w')
    f.write(data)
    f.close()

#create_project_dir('barhoring')
# create_data_files('barhoring', 'https://www.youtube.com/user/thenewboston') 

# add data to the queue file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_file_contents(path):
    with open(path, 'w'):
        pass

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, file): # links are the sets
    delete_file_contents(file)
    for link in sorted(links):
        # append to cached
        append_to_file(file, link)
    