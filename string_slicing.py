#slicing = create a substring by extracting element from another string
#          indexing[] or slicing()
#          [start:stop:step]

name = "Nguyen Le"
#bắt đầu từ 0 và cắt ở trước vị trí thứ 6 trong 1 chuỗi
first_name = name[0:6]
last_name = name [7:9]
#first_name = name[:6]
#last_name = name [7:]

nick_name = name[::2]

reversed_name = name[::-1]

#print(first_name)
#print(last_name)
#print(first_name+" "+ last_name)
#print(nick_name)
#print(reversed_name)

website = "http://google.com"

slice = slice(7,-4) #-4 bắt đầu từ cuối đoạn link google.com

print(website[slice])