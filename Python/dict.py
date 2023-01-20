#!/usr/bin/python3

dict1 = {"timestamp":"2022-12-22 09:01:50.552 +09:00","level":"info","msg":"SimpleWorker: Job is complete","caller":"jobs/base_workers.go:88","worker":"ExpiryNotify","job_id":"ifbj35ycmtr57rxnb5izauj3xe"}
dict2 = {"timestamp":"2022-12-22 09:11:50.658 +09:00","level":"info","msg":"SimpleWorker: Job is complete","caller":"jobs/base_workers.go:88","worker":"ExpiryNotify","job_id":"19bxt7u5jfn8f8oc75xdg8ntny"}
dict3 = {"timestamp":"2022-12-22 09:21:50.751 +09:00","level":"info","msg":"SimpleWorker: Job is complete","caller":"jobs/base_workers.go:88","worker":"ExpiryNotify","job_id":"hdcw9rn7ef86zjicjynordbb7o"}
dict4 = {"timestamp":"2022-12-22 09:31:50.857 +09:00","level":"info","msg":"SimpleWorker: Job is complete","caller":"jobs/base_workers.go:88","worker":"ExpiryNotify","job_id":"968nh15gk3brzpk8s8yc6nzuie"}

print(dict1.values())
print(dict2.values())
print(dict3.values())
print(dict4.values())
print(dict4.keys())



