weather_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
weather_data_fix = []
for i in weather_data:
 if i.replace("+", "").replace("-", "").isdigit():
  # print("1", i)
  if i.isdigit():
   weather_data_fix.append(f"'{int(i):02}'")
   # print("2", weather_data_fix)
  else:
    weather_data_fix.append(f"'{i[0]}'")
    # print("3", weather_data_fix)
    weather_data_fix.append(f"'{int(i[1:]):02}'")
    # print("4", weather_data_fix)
 else:
  weather_data_fix.append(i)
print(" ".join(weather_data_fix))
