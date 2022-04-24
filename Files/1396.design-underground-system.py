#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        if id not in self.checkins:
            self.checkins[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        # get start point
        startStation = self.checkins[id][0]
        startTime = self.checkins[id][1]

        if (startStation, stationName) not in self.times:
            self.times[(startStation, stationName)] = [t-startTime]
        else:
            self.times[(startStation, stationName)].append(t-startTime)

        del self.checkins[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        # get all the times 
        times = self.times[(startStation, endStation)]

        return sum(times)/len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

