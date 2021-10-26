# my_list = [None, 4, 'gsfggg', set()]
#
# for item in my_list: #my_list_iter = iter(my_list)
#     print(item)
#
# print('-----------')
#
# my_list_iter = iter(my_list)
# item = next(my_list_iter)
# print(item)
# item = next(my_list_iter)
# print(item)
# item = next(my_list_iter)
# print(item)
# item = next(my_list_iter)
# print(item)

# range(1,10)

# class MyIterator:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.cursor = None
#
#     def __iter__(self):
#         self.cursor = self.start - 1
#         return self
#
#     def __next__(self):
#         self.cursor += 1
#         if self.cursor == self.end:
#             raise StopIteration
#         return self.cursor
#
#
# my_iterator = MyIterator(1,10)
#
# for item in my_iterator:
#     print(item)
# import datetime
#
#
# class DateRange:
#
#     def __init__(self, start_date, end_date, interval=datetime.timedelta(days=1)):
#         self.start_date = start_date
#         self.end_date = end_date
#         self.interval = interval
#         self.cursor = None
#
#     def __iter__(self):
#         self.cursor = self.start_date - self.interval
#         return self
#
#     def __next__(self):
#         self.cursor += self.interval
#         if self.cursor >= self.end_date:
#             raise StopIteration
#         return self.cursor
#
#
# dates = DateRange(datetime.datetime(2021, 9, 1), datetime.datetime(2021, 10, 1))
#
# for item in dates:
#     print(item)
# import requests
# import re
#
# class HabrIterator:
#     host = 'https://habr.com'
#     post_regex = re.compile(r'<a href=\"(/en/post/\d+/)', re.MULTILINE)
#
#     def __iter__(self):
#         main_page = self.get_main_page()
#         self.links = set(self.post_regex.findall(main_page))
#         return self
#
#     def __next__(self):
#         if not self.links:
#             raise StopIteration
#         link = self.links.pop()
#         print((f'{self.host}{link}'))
#         return self.call_habr(f'{self.host}{link}')
#
#
#     def call_habr(self, link):
#         habr_data = requests.get(link)
#         return habr_data.text
#     def get_main_page(self):
#         return self.call_habr(self.host)
#
# for page in HabrIterator():
#     print(page)
# import datetime
# def my_range(start,end, interval=datetime.timedelta(days=1)):
#
#     while start < end:
#
#         yield start
#
#         start += interval
#
#
# for item in my_range(datetime.datetime(2021, 9, 1), datetime.datetime(2021, 10, 1)):
#     print(item)
# import datetime
#
# numbers = [4, 5, 8, 12]
# dates = []
# for number in numbers:
#     new_date = datetime.datetime(2021, 6 , number)
#     dates.append(new_date)
#
# dates_2 = (datetime.datetime(2021, 6, number) for number in numbers)
# print(dates_2)