from django.shortcuts import render
def fun1(request):
    bus_schedules ={ 'bus_schedules':[
    {'no': 1, 'startpoint': 'Dharmavaram', 'endpoint': 'SRIT', 'morningStartTime': '8:00 am', 'eveningStartTime': '5:00 pm'},
    {'no': 2, 'startpoint': 'Anantapur', 'endpoint': 'SRIT', 'morningStartTime': '8:30 am', 'eveningStartTime': '5:30 pm'},
    {'no': 3, 'startpoint': 'Hindupur', 'endpoint': 'SRIT', 'morningStartTime': '7:45 am', 'eveningStartTime': '4:45 pm'},
    {'no': 4, 'startpoint': 'Kadiri', 'endpoint': 'SRIT', 'morningStartTime': '8:15 am', 'eveningStartTime': '5:15 pm'},
    {'no': 5, 'startpoint': 'Tadipatri', 'endpoint': 'SRIT', 'morningStartTime': '8:00 am', 'eveningStartTime': '5:00 pm'},
    {'no': 6, 'startpoint': 'Penukonda', 'endpoint': 'SRIT', 'morningStartTime': '7:30 am', 'eveningStartTime': '4:30 pm'},
    {'no': 7, 'startpoint': 'Guntakal', 'endpoint': 'SRIT', 'morningStartTime': '8:00 am', 'eveningStartTime': '5:00 pm'},
    {'no': 8, 'startpoint': 'Uravakonda', 'endpoint': 'SRIT', 'morningStartTime': '8:45 am', 'eveningStartTime': '5:45 pm'},
    {'no': 9, 'startpoint': 'Rayadurg', 'endpoint': 'SRIT', 'morningStartTime': '8:00 am', 'eveningStartTime': '5:00 pm'},
    {'no': 10, 'startpoint': 'Puttaparthi', 'endpoint': 'SRIT', 'morningStartTime': '7:50 am', 'eveningStartTime': '4:50 pm'}
    ]}
    return render(request,'index.html',bus_schedules)