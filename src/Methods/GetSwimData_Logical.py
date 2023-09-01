import statistics

def get_swim_data_logical(fn: str)-> tuple:
    """GIven the name of a swimmer's file, extract all the requird data, then return it to the caller as tuple"""
    FOLDER="assets\\swimdata"
    data = ""
    with open(FOLDER+'\\'+fn) as df:
        data = df.readlines()
        # print(data)

    swimmer,age, distance, stroke = fn.removesuffix('.txt').split('-')
    #Break the line apart by "," to produce a list of items
    times = data[0].strip().split(",")

    converts =[]
    for data in times:
        if ':' in data:
            minutes, rest = data.split(':')
            seconds, hundredths = rest.split('.')
        else:
            minutes = 0
            seconds, hundredths = data.split('.')
        converted_time = int(minutes)*60*100+int(seconds)*100+int(hundredths)
        converts.append(converted_time)

    # print(converts)
    avg= statistics.mean(converts)
    # print(avg)
    #Convert the result into mins:secs.hundreths format
    # Divide the avg by 100 will give seconds and hundredths
    # print(avg/100)
    rounded_avg = round(avg/100,2)
    # print(rounded_avg)
    min_sec,hundredths = str(rounded_avg).split('.')
    min = int(min_sec)//60
    sec =  int(min_sec) - min*60
    average_str = f"{minutes}:{seconds}.{hundredths}"

    # print(result)
    return swimmer, age, distance, stroke, avg, average_str, times, converts