def format_date(date):
  date_elements = date.split("/")
  date_elements.reverse()

  formatted_date = ""
  for el in date_elements:
    formatted_date += el
  
  return formatted_date

print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))