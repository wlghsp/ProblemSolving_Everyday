import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    in_records = {}
    total_times = {}

    for record in records:
        time_str, car_num, status = record.split()
        hour, minute = map(int, time_str.split(":"))
        time = hour * 60 + minute

        if status == "IN":
            in_records[car_num] = time
        else:
            in_time = in_records.pop(car_num)
            total_times[car_num] = total_times.get(car_num, 0) + (time - in_time)

    for car_num, in_time in in_records.items():
        total_times[car_num] = total_times.get(car_num, 0) + ((23 * 60 + 59) - in_time)

    def calculate(time):
        if time <= base_time:
            return base_fee
        return base_fee + math.ceil((time - base_time) / unit_time) * unit_fee

    return [calculate(total_times[car_num]) for car_num in sorted(total_times)]


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN",
                "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) # [14600, 34400, 5000]
