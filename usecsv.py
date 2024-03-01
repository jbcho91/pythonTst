import csv

# CSV 파일 읽기
with open("", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

# CSV 파일 쓰기
#with open('example.csv', 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerow(['Name', 'Age', 'City'])
#    writer.writerow(['John', '25', 'New York'])
#    writer.writerow(['Emma', '30', 'Los Angeles'])