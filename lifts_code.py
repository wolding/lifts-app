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
        return joblist

# function to reorder jobs list by job time
def sort_list(unsorted_list):
    # set lowest value index = to [0]
    for i in range(len(unsorted_list)):
        lvi = i
        for j in range(i+1, len(unsorted_list)):
            # search for lowest time and swap it to index[0] on the list
            if unsorted_list[j].time < unsorted_list[lvi].time:
                lvi = j
        unsorted_list[i], unsorted_list[lvi] = unsorted_list[lvi], unsorted_list[i]
    return unsorted_list


# removes completed job from front of the list
def complete_job(joblist):
    joblist.pop(0)
    return joblist


# create an empty list to hold the jobs in
job_list = []
job_list= add_job("Will", job_list)
job_list= add_job("Kev", job_list)
print(sort_list(job_list))
print(job_list)

