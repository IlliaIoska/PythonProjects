class Track:
    def __init__(self, COBOL_time, pole_vault_time, doughnut_eating_time):
        self.COBOL_time = COBOL_time
        self.pole_vault_time = pole_vault_time
        self.doughnut_eating_time = doughnut_eating_time

    def getCOBOL(self):
        return self.COBOL_time
    
    def getPoleVault(self):
        return self.pole_vault_time

    def getDoughnutEating(self):
        return self.doughnut_eating_time

class TracksDB:
    def __init__(self):
        self.tracksDB = []
    
    def append(self, track):
        self.tracksDB.append(track)

    def getTracksDB(self):
        return self.tracksDB

    def __str__(self):
        for track in self.tracksDB:
            return f"{track.COBOL_time}"

def runApp():
    participants_num = int(input("Number of Participants: "))
    tracksDB = TracksDB()
    for i in range(participants_num):
        cobol_time = int(input("Time spent on COBOL: "))
        pole_vault_time = int(input("Time spent on pole vault: "))
        doughnut_eating_time = int(input("Time spent on doughtnut eating: "))
        track = Track(cobol_time, pole_vault_time, doughnut_eating_time)
        tracksDB.append(track)

    print(tracksDB)

runApp()

