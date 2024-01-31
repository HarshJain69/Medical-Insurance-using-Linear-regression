import matplotlib.pyplot as plt
import datetime

# Define code sections and their start and end times
code_sections = {
    'Load Data': {'start': datetime.datetime.now(), 'end': None},
    'Preprocess Data': {'start': None, 'end': None},
    'Train Model': {'start': None, 'end': None},
    'Input New Customer': {'start': None, 'end': None},
    'Make Predictions': {'start': None, 'end': None},
    'Display Results': {'start': None, 'end': None}
}

# Simulate code execution time for each section (replace with actual execution times)
import time
time.sleep(2)  # Simulate load data
code_sections['Load Data']['end'] = datetime.datetime.now()

time.sleep(1)  # Simulate preprocess data
code_sections['Preprocess Data']['start'] = datetime.datetime.now()
time.sleep(3)
code_sections['Preprocess Data']['end'] = datetime.datetime.now()

time.sleep(1)  # Simulate train model
code_sections['Train Model']['start'] = datetime.datetime.now()
time.sleep(2)
code_sections['Train Model']['end'] = datetime.datetime.now()

time.sleep(1)  # Simulate input new customer
code_sections['Input New Customer']['start'] = datetime.datetime.now()
time.sleep(1)
code_sections['Input New Customer']['end'] = datetime.datetime.now()

time.sleep(1)  # Simulate make predictions
code_sections['Make Predictions']['start'] = datetime.datetime.now()
time.sleep(1)
code_sections['Make Predictions']['end'] = datetime.datetime.now()

time.sleep(1)  # Simulate display results
code_sections['Display Results']['start'] = datetime.datetime.now()
time.sleep(2)
code_sections['Display Results']['end'] = datetime.datetime.now()

# Create Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

for i, (section, times) in enumerate(code_sections.items()):
    start = times['start']
    end = times['end']
    
    if end is None:
        end = datetime.datetime.now()
    
    ax.barh(i, width=(end - start).total_seconds() / 60, left=start, color='skyblue', edgecolor='black', height=0.6)

ax.set_yticks(range(len(code_sections)))
ax.set_yticklabels(code_sections.keys())
ax.set_xlabel('Time (minutes)')
ax.set_title('Code Execution Gantt Chart')

plt.show()