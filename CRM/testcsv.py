blob = ['storage-tutorial/sample_csv.log-2020', 'storage-tutorial/sample_image.log', 'storage-tutorial/sample_text.txt', 'storage-tutorial/test.log-2020087']
ls = [f for f in blob if '.log' in f]
print(ls)