import lzma
import shutil

input_line = 9


with open('/SS970evo/datasets/dataset_overlap/overlap_D4j_MegaDiff/overlap_result.txt', 'r') as f2:
    log_file_lines = f2.readlines()

log_file_line = log_file_lines[input_line-1]
D4j_project = log_file_line.split('; ')[0]
D4j_project = D4j_project.split(' ')[1]
print(D4j_project)


D4j_file = '/SS970evo/datasets/defects4j-master/framework/projects/' + D4j_project.split('-')[0][3:] + '/patches/' + D4j_project.split('-')[1] + '.src.patch'
print(D4j_file)

with open(D4j_file, 'r') as D4j_f:
    # D4j_lines = D4j_f.readlines()
    with open('overlap_d4j.patch', 'w') as output1:
        shutil.copyfileobj(D4j_f, output1)
    
# print(D4j_lines)

overlap_project = log_file_line.split('; ')[1][8:]
overlap_file = '/SS970evo/datasets/MegaDiff_dataset/megadiff-master/'+overlap_project
print(overlap_project)

with lzma.open(overlap_file, 'rb') as f:
    # overlap_lines = f.readlines()
    with open('overlap_mega.patch', 'wb') as output:
        shutil.copyfileobj(f, output)
    




