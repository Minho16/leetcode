class UndergroundSystem:
    def __init__(self):
        self.average_time_dict = (
            {}
        )  # Key = Str "startStation-endStation" // Value = List[time_diffs]
        self.checked_in_pax = (
            {}
        )  # Key = Int PAX id // Value = List[startStationName, checkInTime]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in_pax[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checked_in_pax.keys():
            stations_str = self.checked_in_pax[id][0] + "-" + stationName
            time_diff = t - self.checked_in_pax[id][1]
            if stations_str in self.average_time_dict.keys():
                self.average_time_dict[stations_str].append(time_diff)
            else:
                self.average_time_dict[stations_str] = [time_diff]
            del self.checked_in_pax[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations_str = startStation + "-" + endStation
        return sum(self.average_time_dict[stations_str]) / len(
            self.average_time_dict[stations_str]
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
