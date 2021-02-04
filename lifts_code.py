from datetime import datetime


# Job class contains details of job, will be called as customer name
class Job:
    def __init__(self, time, origin, destination):
        self.time = time
        self.origin = origin
        self.destination = destination
        now = datetime.now()
        self.job_added = now.strftime("%H:%M")

    def __repr__(self):
        return "Job from {origin} to {dest} at {time}".format(origin=self.origin, dest=self.destination, time=self.time)

# add a job to the list and return update
def add_job(name, joblist):
        time = input("What time do you need the lift?: hh:mm ")
        origin, destination = input("From: "), input("To: ")
        name = Job(time, origin, destination)
        joblist.append(name)
        return joblist, name


# create an empty list to hold the jobs in
job_list = []


job_list, name = add_job("Will", job_list)
print(job_list, name, name.)

