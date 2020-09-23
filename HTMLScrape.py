import requests,openpyxl

print('What URL would you like to scrape?')
url = input()
#url = 'https://www.optus.com.au/mobile/plans/shop'
res = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})

res.raise_for_status()

##Format Source Code
print('Source Code received. Saving to file.')
final_source = []
source = ''
char_count = 0
for letter in res.text:
    source = source + letter
    char_count += 1
    if char_count >= 5000:
        final_source.append(source)
        source = ''
        char_count = 0
        
##WRITE TO EXCEL FILE AND SAVE
print('Source Code Formatted. Writing to Excel sheet')
wb = openpyxl.Workbook()

sheet = wb['Sheet']

row = 1
column = 1
for element in final_source:
    sheet.cell(row,column).value = element
    row += 1


print('What is the file name you would like to save to?(file extension will be .xlsx by default)')
filename = input()
wb.save(filename+'.xlsx')

print('Done')
